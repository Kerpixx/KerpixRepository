numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
Nomemumber = None
Counts = len(numbers)
i=0
while type(numbers[i]) == int:
    i += 1
Average = (sum(numbers[:i])+ sum(numbers[i+1:])) / (Counts)
numbers[i] = Average
print("Измененный список:", numbers)
