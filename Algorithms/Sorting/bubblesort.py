def bubbleSort(dataset):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp
        print("Sorted dataset -", dataset)

list1 = [6, 10, 45, 2, 90, 20, 11]
bubbleSort(list1)
