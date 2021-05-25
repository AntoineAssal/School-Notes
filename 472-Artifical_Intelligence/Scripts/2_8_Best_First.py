def search(start, goal, next_states, heurestic):
    PrioQueue = [(heurestic(start, goal), [start])]
    while len(PrioQueue) > 0:
        _, Path = heapq.heappop(PrioQueue)
        state = Path[-1]
        if state == goal:
            return Path
        for ns in next_states(state):
            if ns not in Path:
                d = heurestic(ns, goal)
                heapq.heappush(PrioQueue, (d, Path+[ns]))
