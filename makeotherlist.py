import csv


def num_to_tuple(num):
    temp = []
    i = 4
    while (i >= 0):
        x = num//(3**i)
        temp.append(x)
        num = num-(x*(3**i))
        i -= 1
    return tuple(temp)


def tuple_to_num(tup):
    first = tup[0]*(3**4)
    second = tup[1]*(3**3)
    third = tup[2]*(3**2)
    fourth = tup[3]*(3)
    fifth = tup[4]
    return (first+second+third+fourth+fifth)


f = open("percentages.csv", "r")
data = list(csv.reader(f))
f.close()

totals = {}
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    totals[(a, b, c, d, e)] = 0

while ([] in data):
    data.remove([])


for i in range(len(data)):
    if i == 0:
        continue
    for j in range(len(data[i])):
        if j == 0:
            continue
        totals[num_to_tuple(j-1)] += float(data[i][j])


with open("relative_percentages.csv", "w") as file:
    writer = csv.writer(file)
    first_row = []
    first_row.append("tuples")
    first = True
    for row in data:
        if first:
            first = False
            continue
        first_row.append(row[0])

    writer.writerow(first_row)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        new_row = []
                        new_row.append((a, b, c, d, e))

                        first = True
                        for row in data:
                            if first:
                                first = False
                                continue
                            if totals[((a, b, c, d, e))] == 0:
                                new_row.append(0)
                            else:
                                value = float(row[tuple_to_num(
                                    (a, b, c, d, e))+1])/totals[((a, b, c, d, e))]
                            new_row.append(value)
                        writer.writerow(new_row)
    file.close()
