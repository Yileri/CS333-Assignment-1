import heapq as pq

def subprime_path(capacity_graph, load_graph, start, end):
    city_length = len(capacity_graph)
    final_graph = [[] for x in range(city_length)]

    # compute ratios for edges and fill the graph with it
    for city in range(city_length):
        for truck in range(len(capacity_graph[city])):
            final_graph[city].append((load_graph[city][truck][0], (load_graph[city][truck][1]/capacity_graph[city][truck][1]) * 100))

    cost_graph = {}
    for city in range(city_length):
        # make the default percentage higher than possible which is 100
        # and set initial way to a node as empty
        cost_graph[city] = {"cost": 105, "way": []}

    # create visit list
    visit = []

    # set the beginning node's cost to 0
    cost_graph[start]["cost"] = 0

    temp = start

    # for loop for every city except start city
    for city in range(city_length-1):
        if temp not in visit:
            visit.append(temp)

            # create heap for determining min capacity way for this city
            heap = []

            for neighbor in final_graph[start]:
                if neighbor[0] not in visit:
                    print(neighbor[0])


    print(cost_graph)
    print(load_graph)
    print(capacity_graph)
    print(final_graph)

def main():
    c = int(input())
    adjl_capacities = [[] for i in range(c)]
    adjl_loads = [[] for i in range(c)]
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_capacities[i].append((int(pair[0]),int(pair[1])))
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_loads[i].append((int(pair[0]),int(pair[1])))
    start = int(input())
    end=int(input())
    subprime_path(adjl_capacities,adjl_loads,start,end)

main()