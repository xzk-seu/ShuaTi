
def main():
    n = int(input("input: "))
    f = [1000 for _ in range(n+1)]
    p = [i for i in range(n + 1)]
    for i in range(3, 6):
        f[i] = 1
    for i in range(6, n+1):
        m = 1000
        m_t = None
        for t in range(i-5, i-2):
            if f[t] < m:
                m = f[t]
                m_t = t
        f[i] = m + 1
        p[i] = m_t

    print(f[-1])
    print("+=====================+")

    i = n
    t = p[i]
    res = list()
    while t != i:
        res.append(i-t)
        i = t
        t = p[i]
    s = "%d = " % n
    for i in res:
        s += "%d+" % i
    s += "%d" % t
    print(s)


if __name__ == '__main__':
    main()
