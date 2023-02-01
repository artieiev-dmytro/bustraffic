from buses.models import Bus


def dfs_paths(graph, start, goal):
    stack =[(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    grh = {}
    for q in qs:
        grh.setdefault(q.from_city_id, set())
        grh[q.from_city_id].add(q.to_city_id)
    return grh


def get_routes(request, form) -> dict:
    context = {'form': form}
    qs = Bus.objects.all().select_related('from_city', 'to_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    time = data['time']
    cities = data['cities']
    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))
    if not len(all_ways):
        raise ValueError('Routes not')
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Routes not --')
    else:
        right_ways = all_ways

    routes = []
    all_buses = {}
    for q in qs:
        all_buses.setdefault((q.from_city_id, q.to_city_id), [])
        all_buses[(q.from_city_id, q.to_city_id)].append(q)

    for route in right_ways:
        tmp = {}
        tmp['buses'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qss = all_buses[(route[i], route[i + 1])]
            q = qss[0]
            total_time += q.bus_time
            tmp['buses'].append(q)
        tmp['total_time'] = total_time

        if total_time <= time:
            routes.append(tmp)

    if not routes:
        raise ValueError('Time mini')

    sort_routes = []
    if len(routes) == 1:
        sort_routes = routes
    else:
        times = sorted(set(r['total_time'] for r in routes))
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sort_routes.append(route)

    context['routes'] = sort_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    
    return context 