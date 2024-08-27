import csv


def get_pattern(word, answer):
    pattern = [0, 0, 0, 0, 0]
    remaining = list(answer)
    for i in range(5):
        if word[i] == answer[i]:
            pattern[i] = 2
            remaining.remove(word[i])
    for i in range(5):
        if word[i] != answer[i] and word[i] in remaining:
            pattern[i] = 1
            remaining.remove(word[i])
    return tuple(pattern)


f = open("valid-wordle-words.txt", "r")
valid_words = f.read().split("\n")
f.close()

g = open("wordle-nyt-answers-alphabetical.txt", "r")
possible_answers = g.read().split("\n")
g.close()

with open("percentages.csv", "w") as file:
    writer = csv.writer(file)
    toprow = []
    toprow.append("word")
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        index = (a, b, c, d, e)
                        toprow.append(index)
    writer.writerow(toprow)

    for ans in possible_answers:
        if len(ans) != 5:
            continue
        newrow = []
        newrow.append(ans)
        patdict = {}
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        for e in range(3):
                            patdict[(a, b, c, d, e)] = 0

        for word in valid_words:
            if len(word) != 5:
                continue
            pat = get_pattern(word, ans)
            patdict[pat] += 1

        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        for e in range(3):
                            newrow.append(
                                patdict[(a, b, c, d, e)]/len(valid_words))

        writer.writerow(newrow)

    file.close()
