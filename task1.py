
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def search (list,item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return None

for find_item in ['банан', 'груша', 'персик']:
    index_item = search(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
