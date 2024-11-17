# TODO импортировать необходимые молули
import csv
import json
new_array = []
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]# TODO считать содержимое csv файла
        for line in lines[:]:
            new_array.append(line)
        print(json.dumps((new_array), indent=4), end='')# TODO Сериализовать в файл с отступами равными 4



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
