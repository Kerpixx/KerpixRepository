# TODO  Напишите функцию count_letters
def count_letters(text):
    clone = []

    text = text.lower()
    for i in range(len(text)):
        if text[i].isalpha():
            clone.append(text[i])
    return clone


# TODO Напишите функцию calculate_frequency

def calculate_frequency(text, count):
    text_not_duplicate = "".join(set(text))
    qustuon = {}
    for i in range(len(text_not_duplicate)):
        l = 0
        probability = 0
        for k in range(count):
            if text_not_duplicate[i] == text[k]:
                l += 1
        probability = l/count
        qustuon[text_not_duplicate[i]] = round(probability, 2)
    return qustuon




main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

full = calculate_frequency(count_letters(main_str),len(count_letters(main_str)))
for key in full:
    print(key, ":", full[key])
# TODO Распечатайте в столбик букву и её частоту в тексте
