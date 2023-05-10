def direct_flights(graph, locations):
    def find_node(value):
        nodes = graph.get_nodes()
        for node in nodes:
            if node.value == value:
                return node

    cost = 0
    direct = True
    while len(locations) > 1 and direct:
        start = locations[0]
        end = locations[1]
        neighbors = graph.get_neighbors(find_node(start))
        for location in neighbors:
            if location.vertex.value == end:
                cost += location.weight
                direct = True
                break
            else:
                direct = False
        locations.remove(start)

    if not direct or cost == 0:
        cost = 0
        direct = False

    return direct, cost
