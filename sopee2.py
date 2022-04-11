def main():
    s = input()
    s = list(s)
    n = len(s)
    for i in reversed(range(n)):
        if s[i] == "0":
            continue
        for j in reversed(range(i)):
            if int(s[i] < s[j]):
                s[i], s[j] = s[j], s[i]
                print("".join(s))
                return
    print(0)


if __name__ == '__main__':
    main()
