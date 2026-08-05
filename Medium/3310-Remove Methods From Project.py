class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
         # Build graph
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)

        # Find all suspicious methods
        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        # Check if any outside method invokes a suspicious one
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        # Return remaining methods
        ans = []
        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans