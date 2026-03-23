class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stops_to_busses = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stops_to_busses[stop].append(bus)
        
        queue = deque([source])
        visited_stops = {source}
        visited_buses = set()
        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                curr_stop = queue.popleft()
                for bus in stops_to_busses[curr_stop]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)
                    
                    for next_stop in routes[bus]:
                        if next_stop in visited_stops:
                            continue
                        if next_stop == target:
                            return res
                        visited_stops.add(next_stop)
                        queue.append(next_stop)
        return -1
