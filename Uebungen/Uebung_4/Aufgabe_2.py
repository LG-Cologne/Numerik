for iter in range(len(a)):
    if (a[iter][iter] == 0):
        for row in range(iter + 1, len(a)):  # zieht zeile mit höhestem pivot element auf die jetzige Zeile
            highestRow = 0
            if a[row][iter] > a[row][highestRow]:
                highestRow = row

            a[[iter, highestRow]] = a[[highestRow, iter]]
