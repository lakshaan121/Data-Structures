class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def f(key):
            visited.add(key)
            for keys in rooms[key]:
                if keys not in visited:
                    visited.add(keys)
                    f(keys)
        f(0)
        return len(visited)==len(rooms)

        