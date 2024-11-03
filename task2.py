# TODO Напишите функцию find_common_participants
def find_common_participants (str1, str2, arg):
    str1 = str1.split(arg)
    str2 = str2.split(arg)
    clone = []
    for i in range(len(str1)):
        for k in range(len(str2)):
            if str1[i] == str2[k]:
                clone.append(str1[i])
    clone.sort()
    return clone

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
clone = find_common_participants(participants_first_group, participants_second_group, '|')
for i in range(len(clone)):
    print(clone[i])
