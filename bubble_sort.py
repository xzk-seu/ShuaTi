
def bubble_sort(s: list):
    n = len(s)
    for i in range(n):
        for j in range(n-i-1):
            if s[j] > s[j+1]:
                s[j], s[j + 1] = s[j+1], s[j]


if __name__ == '__main__':
    a = [3, 4, 5, 1, 3]
    bubble_sort(a)
    print(a)
