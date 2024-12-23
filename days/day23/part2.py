import sys
from collections import defaultdict


def search(node, adj, graph) -> set:

    longest = graph

    for x in adj[node]:
        if x in longest:
            continue

        valid = True
        for m in graph:
            if m not in adj[x]:
                valid = False
                break

        if valid:
            longest = max([search(x, adj, set([*graph, x])), graph], key=len)

    return longest


def main() -> None:
    data = sys.stdin.read().strip()

    conn = [tuple(line.split("-")) for line in data.splitlines()]

    adj = defaultdict(set)
    for c in conn:
        n1, n2 = c
        adj[n1].add(n2)
        adj[n2].add(n1)

    pwd = ""
    for k, _ in adj.items():
        pwd = max([",".join(sorted(search(k, adj, set([k])))), pwd], key=len)
    print(pwd)


if __name__ == "__main__":
    main()
