from typing import List


class Solution:
    def networkDelayTimeFloyd(self, times: List[List[int]], n: int, m: int) -> int:
        # Floyd's method：
        w = [[float('inf') for i in range(0, n + 1)] for i in range(0, n + 1)]
        for i in range(0, n + 1):
            w[i][i] = 0
        for list in times:
            w[list[0]][list[1]] = list[2]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    w[j][k] = min(w[j][k], w[j][i] + w[i][k])

        result = 0

        for i in range(1, n + 1):
            result = max(result, w[m][i])

        return result

    # Enhanced： Floyd's algorithm to get not only the shortest length but also the paths of graph
    def networkDelayTimeFloydEnhanced(self, times: List[List[int]], n: int, m: int) -> int:
        w = [[float('inf') for i in range(0, n + 1)] for j in range(0, n + 1)]
        route = [[[] for i in range(0, n + 1)] for j in range(0, n + 1)]
        for i in range(0, n + 1):
            w[i][i] = 0
            route[i][i].append(i)
        print(route[m])
        for list in times:
            w[list[0]][list[1]] = list[2]
            route[list[0]][list[1]].append(list[1])
        print(route)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    if w[j][k] > w[j][i] + w[i][k]:
                        w[j][k] = w[j][i] + w[i][k]
                        # the path from j to k: copy the path from j to i firstly, 
                        # then copy the path from i to k
                        route[j][k] = route[j][i][:]
                        for x in route[i][k]:
                            route[j][k].append(x)

        result = 0
        print(route[m])

        for i in range(1, n + 1):
            result = max(result, w[m][i])

        return result

    def networkDelayTimeDjstra(self, times: List[List[int]], n: int, m: int) -> int:
        # Dijstra’s method：
        w = [[float('inf') for i in range(0, n + 1)] for i in range(0, n + 1)]
        for i in range(0, n + 1):
            w[i][i] = 0
        for list in times:
            w[list[0]][list[1]] = list[2]

        dist = [float('inf') for i in range(0, n + 1)]
        dist[m] = 0
        isVisited = [False for i in range(0, n + 1)]
        for i in range(1, n + 1):
            cur = -1
            for j in range(1, n + 1):
                if not isVisited[j] and (cur == -1 or dist[j] < dist[cur]):
                    cur = j

            isVisited[cur] = True
            for j in range(1, n + 1):
                dist[j] = min(dist[j], dist[cur] + w[cur][j])

        result = max(dist[1:])
        result = -1 if result == float('inf') else int(result)
        return result

    # Enhanced： Dijstra's algorithm to get not only the shortest length but also the paths of graph
    def networkDelayTimeDijstraEnhanced(self, times: List[List[int]], n: int, m: int) -> int:
        w = [[float('inf') for i in range(0, n + 1)] for i in range(0, n + 1)]
        for i in range(0, n + 1):
            w[i][i] = 0
        for list in times:
            w[list[0]][list[1]] = list[2]

        dist = [float('inf') for i in range(0, n + 1)]
        routes = [[] for i in range(0, n + 1)]
        dist[m] = 0
        routes[m] = [m]
        isVisited = [False for i in range(0, n + 1)]
        for i in range(1, n + 1):
            cur = -1
            for j in range(1, n + 1):
                if not isVisited[j] and (cur == -1 or dist[j] < dist[cur]):
                    cur = j

            isVisited[cur] = True
            for j in range(1, n + 1):
                if dist[cur] + w[cur][j] < dist[j]:
                    dist[j] = dist[cur] + w[cur][j]
                    # the path to j: copy the path to cur firstly, 
                    # then copy the path from cur to j
                    routes[j] = routes[cur][:]
                    routes[j].append(j)

        for route in routes:
            print(route)

        result = max(dist[1:])
        result = -1 if result == float('inf') else int(result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTimeFloydEnhanced([[2, 1, 1], [2, 3, 1], [3, 4, 1]],
                                          4,
                                          2))
