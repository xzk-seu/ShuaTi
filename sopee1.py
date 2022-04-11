def main():
    s = input()
    res = ""
    first_char = True
    first_word = True
    for c in s:
        if c.isalpha() or c.isdigit():
            if first_char and not first_word:
                res += c.upper()
            else:
                res += c.lower()
            first_char = False
        else:
            if not first_char:
                first_word = False
            first_char = True
    print(res)


if __name__ == '__main__':
    main()
