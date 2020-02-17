class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        ans = 0

        for i in range(len(stones)):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False for _ in range(len(stones))]

        # stack = [0]
        for i in range(len(stones)):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()

                    visited[node] = True
                    for nei in graph[node]:
                        if not visited[nei]:
                            stack.append(nei)
                            visited[nei] = True
                ans -= 1

        return ans



