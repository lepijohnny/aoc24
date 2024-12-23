import re
import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.read().strip()

    conn = [tuple(line.split("-")) for line in data.splitlines()]

    adj = defaultdict(set)
    for c in conn:
        n1, n2 = c
        adj[n1].add(n2)
        adj[n2].add(n1)

    tgl = set()
    for k, v in adj.items():
        for n1 in [n for n in v if n != k]:
            for n2 in [n for n in adj[n1] if n != n1 and n != k]:
                if k in adj[n2]:
                    t = "".join(sorted([k, n1, n2]))
                    if "t" in t[0 : len(t) : 2]:
                        tgl.add(t)

    print(len(tgl))


if __name__ == "__main__":
    main()
