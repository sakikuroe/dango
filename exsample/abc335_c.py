from dango.dango import Dango


def main():
    n, q = map(int, input().split())

    deq = Dango()

    for i in range(n):
        deq.append((i + 1, 0))

    for _ in range(q):
        f, x = input().split()

        if f == "1":
            a, b = deq.popleft()
            deq.appendleft((a, b))
            match x:
                case "R":
                    deq.appendleft((a + 1, b))
                case "L":
                    deq.appendleft((a - 1, b))
                case "U":
                    deq.appendleft((a, b + 1))
                case "D":
                    deq.appendleft((a, b - 1))
            deq.pop()
        else:
            print(*deq[int(x) - 1])


if __name__ == "__main__":
    main()
