import sys


def main(str1, str2):
    if not str1 or not str2 or len(str1) < len(str2):
        return 0
    mapping = [0 for _ in range(256)]
    for i in range(len(str2)):
        mapping[ord(str2[i])] += 1
    left = 0
    right = 0
    match = len(str2)
    minlength = sys.maxsize
    while right < len(str1):
        mapping[ord(str1[right])] -= 1
        if mapping[ord(str1[right])] >= 0:
            match -= 1
        if match == 0:
            while mapping[ord(str1[left])] < 0:
                mapping[ord(str1[left])] += 1
            minlength = min(minlength, right - left + 1)
            match += 1
            mapping[ord(str1[left])] += 1
            left += 1
        right += 1
    return minlength if minlength != sys.maxsize else 0


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    res = main(s1, s2)
    print(res)
