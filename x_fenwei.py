def get_result():
    records = list()
    with open("response_time", 'r') as fr:
        for line in fr.readlines():
            records.append(int(line))

    records = sorted(records)
    pos = int(0.8 * len(records))
    return records[pos]


def main():
    res = get_result()
    print(res)


if __name__ == '__main__':
    main()
