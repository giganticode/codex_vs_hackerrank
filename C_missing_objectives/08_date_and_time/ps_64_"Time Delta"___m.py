"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. 
"""


class Solution:
    def __init__(self):
        self.visited = {}

    def dfs(self, node, graph):
        if node not in self.visited:
            self.visited[node] = True
            for n in graph[node]:
                self.dfs(n, graph)

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {i: [] for i in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        count = 0
        for i in range(n):
            if i not in self.visited:
                self.dfs(i, graph)
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countComponents(5, [[0, 1], [1, 2], [3, 4]]))