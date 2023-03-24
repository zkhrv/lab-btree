from BtreeMap import btree_map
from prettytable import PrettyTable

t=3
bt_map = btree_map(t)

bt_map.AddElement(1, "One")
bt_map.AddElement(2, "Two")
bt_map.AddElement(3, "Three")
bt_map.AddElement(4, "Four")
bt_map.AddElement(5, "Five")

table = PrettyTable()
table.field_names = ["Действие", "Результат"]

table.add_row(["Элемент с ключом 1:", bt_map.find(1)])
table.add_row(["Элемент с ключом 2:", bt_map.find(2)])
table.add_row(["Элемент с ключом 3:", bt_map.find(3)])
table.add_row(["Элемент с ключом 4:", bt_map.find(4)])
table.add_row(["Элемент с ключом 5:", bt_map.find(5)])
table.add_row(["------------------------------","--------------"])
table.add_row(["Число элементов в дереве:", bt_map.count()])

bt_map.correction(1, "я новенький")

table.add_row(["Измененный элемент с ключом 1:", bt_map.find(1)])
table.add_row(["Число элементов в дереве:", bt_map.count()])
table.add_row(["------------------------------","--------------"])
table.add_row(["Удаляем элемент с ключом 3:", bt_map.remove(3)])
table.add_row(["Число элементов в дереве:", bt_map.count()])
table.add_row(["------------------------------","--------------"])
table.add_row(["Элемент с ключом 1:", bt_map.find(1)])
table.add_row(["Элемент с ключом 2:", bt_map.find(2)])
table.add_row(["Элемент с ключом 3:", bt_map.find(3)])
table.add_row(["Элемент с ключом 4:", bt_map.find(4)])
table.add_row(["Элемент с ключом 5:", bt_map.find(5)])
table.add_row(["------------------------------","--------------"])
table.add_row(["Число элементов в дереве:", bt_map.count()])
table.add_row(["------------------------------","--------------"])
table.add_row(["Удаляем все элементы в дереве:", bt_map.remove_all()])
table.add_row(["Число элементов в дереве:", bt_map.count()])

print(table)




