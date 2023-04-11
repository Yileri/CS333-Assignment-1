import heapq as pq

def subprime_path(capacity_graph, load_graph, start, end):
    final_graph = [[] for x in range(len(capacity_graph))]

    # compute ratios for edges and fill the graph with it
    for city in range(len(capacity_graph)):
        for truck in range(len(capacity_graph[city])):
            final_graph[city].append((load_graph[city][truck][0], (load_graph[city][truck][1]/capacity_graph[city][truck][1]) * 100))

    cost_graph = {}
    for city in range(len(final_graph)):
        # make the default percentage higher than possible which is 100
        # and set initial way to a node as empty
        cost_graph[city] = {"cost": 105, "way": []}

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