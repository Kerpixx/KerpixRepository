# TODO решите задачу
f = open('input.json', 'r', encoding="utf-8")
String = []
clone1 = 0
clone2 = 0
i = 0
summ = 0
for line in f:
    String.append(line.rstrip())
    if line.rstrip().find('"score":') >= 0:
        clone_score = []
        for k in range(len(line.rstrip())):
            if String[i][k].isdigit():
                clone_score.append(String[i][k])
            if String[i][k].find('.') >= 0:
                clone_score.append(String[i][k])
        clone_score = float(''.join(map(str, clone_score)))
        clone1 = clone_score
    if line.rstrip().find('"weight":') >= 0:
        clone_weight = []
        for k in range(len(line.rstrip())):
            if String[i][k].isdigit():
                clone_weight.append(String[i][k])
            if String[i][k].find('.') >= 0:
                clone_weight.append(String[i][k])
        clone_weight = float(''.join(map(str, clone_weight)))
        clone2 = clone_weight
        summ += clone1*clone2
    i+=1
print(round(summ,3))
