def santa_sort(items):
    for _ in range(2):
        for i in range(len(items)):
            minimum = i

            for j in range(i + 1, len(items)):
                if items[j] < items[minimum]:
                    minimum = j

            items[minimum], items[i] = items[i], items[minimum]

    return items
