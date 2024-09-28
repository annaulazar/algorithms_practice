from collections import defaultdict


def dfs(graph, start, end, visited):
    visited[start] = True
    if start == end:
        return True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, end, visited):
                return True
    return False


def main():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        U, V, T = map(int, input().split())
        graph[U].append((V, T))
        graph[V].append((U, T))

    K = int(input())
    proposals = []
    for _ in range(K):
        U, V, T, C = map(int, input().split())
        proposals.append((U, V, T, C))

    P = int(input())
    requirements = [tuple(map(int, input().split())) for _ in range(P)]

    existing_lines = set((min(u, v), max(u, v)) for u in graph for v, _ in graph[u])

    # Check if all requirements are already met
    requirements_met = all(dfs(graph, A, B, [False] * (N + 1)) for A, B, _ in requirements)
    if requirements_met:
        print(0)
        return

        # Check if requirements can be met without building new lines
    for A, B, T in requirements:
        if (min(A, B), max(A, B)) not in existing_lines:
            print(-1)
            return

            # Sort proposals by cost in ascending order
    proposals.sort(key=lambda x: x[3])

    # Find the minimum cost required to satisfy all requirements
    min_cost = float('inf')
    for proposal in proposals:
        U, V, T, C = proposal
        new_graph = graph.copy()
        new_graph[U].append((V, T))
        new_graph[V].append((U, T))

        # Check if all requirements are met with this proposal
        requirements_met = all(dfs(new_graph, A, B, [False] * (N + 1)) for A, B, _ in requirements)
        if requirements_met:
            min_cost = min(min_cost, C)

    if min_cost == float('inf'):
        print(-1)
    else:
        print(1)
        print(min_cost)


if __name__ == "__main__":
    main()