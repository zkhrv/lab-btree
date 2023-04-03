class BTreeNode: #Класс для узла
    def __init__(self, N, leaf):
        self.N = N #количество ключей
        self.leaf = leaf #для проверки на лист (крайний элемент в дереве)
        self.keys = [] #ключи
        self.values = [] #значения
        self.children = [] #ссылки на потомков

class btree_map: #Класс для ассациативного массива
    def __init__(self, N):
        self.N = N #кол-во ключей в каждом узле
        self.root = None #корень дерева

    def find(self, key):# получение знаения по ключу
        if self.root is None: # если ключ не связан с значением
            return None
        else:
            return self.Find(key, self.root) #возвращаем найденное значенине

    def Find(self, key, node):# метод поиска значения по ключу
        i = 0
        while i < len(node.keys) and key > node.keys[i]: # пока есть ключ и искомый ключ не больше чем требуется
            i += 1
        if i < len(node.keys) and key == node.keys[i]: # если искомый ключ найден, возвращаем соответсвующее значение
            return node.values[i]
        elif node.leaf: # если ключ является листом, возвращаем None
            return None
        else:
            return self.Ffind(key, node.children[i]) # если ключ не найден в данном узле, ищем его в следующем

    def AddElement(self, key, value):
        # Проверяем, есть ли корневой узел в дереве, иначе создаем новый объект узла, делаем его листом и добавляем ключ и значение
        if self.root is None:
            self.root = BTreeNode(self.N, True)  # Создаем новый объект узла, делаем его листом
            self.root.keys.append(key)  # Добавляем ключ
            self.root.values.append(value)  # Добавляем значение
        else:
            node = self.root  # Присваиваем переменной node корневой узел

            # Проверяем, является ли текущий узел листовым. Если нет, то создаем новый дочерний узел, добавляем в него текущий узел и разделяем его
            if len(node.keys) == 2 * self.N - 1:
                new_root = BTreeNode(self.N, False)  # Создаем новый дочерний узел
                new_root.children.append(node)  # Добавляем текущий узел в новый дочерний узел
                self.Split(new_root, 0, node)  # Разделяем текущий узел и добавляем ключ из него в новый дочерний узел
                node = new_root  # Перемещаемся на новый дочерний узел
                self.root = new_root  # Обновляем корневой узел

            self.Set(key, value, node)  # Добавляем ключ и значение в узел с помощью метода Set


    def Set(self, key, value, node):
        i = 0 #инициализация счетчика цикла
        while i < len(node.keys) and key > node.keys[i]: #  пока индекс счетчика меньше длины списка ключей и текущий ключ больше i-го ключа
            i += 1 # увеличиваем счетчик цикла
        if node.leaf: # если узел - лист
            node.keys.insert(i, key) # добавляем значение ключа
            node.values.insert(i, value) # добавляем значение по ключу
        else:
            if len(node.children[i].keys) == 2 * self.N - 1: # если количество ключей в i-м дочернем узле равно удвоенному значению N - 1
                self.Split(node, i, node.children[i]) # разделяем i-й дочерний узел на два
                if key > node.keys[i]: # если вставляемый ключ больше i-го ключа
                    i += 1 # увеличиваем индекс счетчика
            self.Set(key, value, node.children[i]) # рекурсивно вызываем метод Set для i-го узла

    def Split(self, parent, i, child):
        new_child = BTreeNode(child.N, child.leaf) # дублируем узел
        parent.children.insert(i + 1, new_child) # вставляем новый узел
        parent.keys.insert(i, child.keys[self.N - 1]) # записывем текущий ключ в прошлый узел
        parent.values.insert(i, child.values[self.N - 1]) # записываем текущее значение в прошлый узел
        new_child.keys = child.keys[self.N:] # присваеваем прошлый клчю
        new_child.values = child.values[self.N:] # присваеваем прошлое значение
        child.keys = child.keys[:self.N - 1] # переписываем ключи
        child.values = child.values[:self.N - 1] # переписываем значения
        if not child.leaf: # если узел не лист, помещаем узел в конец
                new_child.children = child.children[self.N:] # добавляем новый дочерний узел в нового родителя 
                child.children = child.children[:self.N] # оставляем только первые N дочерних узлов у родительского узла 


    def correction(self, key, value):
        node = self.root # присваеваем начало дерева
        while node is not None: # пока дерево не закончено
            i = 0
            while i < len(node.keys) and key > node.keys[i]: # пока есть ключ
                i += 1
            if i < len(node.keys) and key == node.keys[i]: # если ключ найден
                node.values[i] = value # заменяем значение
                return
            if i > self.N: # если текущий ключ больше числа всех, выводим ошибку
                print("Ошибка ключа. Значение не было перезаписано. Такого ключа не существует", self.N)
                return
            else:
                node = node.children[i] # переходим к следующему узлу

    def remove(self, key):
        if self.root is None: # если дерево пусто
            return None
        else:
            self.Remove(key, self.root) # вызываем вспомогательный метод

    def Remove(self, key, node):
        i = 0
        while i < len(node.keys) and key > node.keys[i]: # пока есть ключ и искомый ключ не больше чем требуется
            i += 1
        if i < len(node.keys) and key == node.keys[i]: # если искомый ключ найден
            if node.leaf: # если узел лист
                node.keys.pop(i) # удаляем ключ
                node.values.pop(i) # удаляем значение
                node.N -= 1 # уменьшаем количество ключей на 1
            else:
                if len(node.children[i].keys) >= self.N: # если узел потомок имеет достаточно ключей
                    node.keys[i], node.values[i], child_key, child_value = self.get_predecessor(node.children[i]) # меняем значения местами
                    self.Remove(child_key, node.children[i]) # удаляем узел
                    node.keys[i] = child_key # обновляем ключ
                    node.values[i] = child_value # обновляем значение
                elif len(node.children[i+1].keys) >= self.N: # если правый узел потомок имеет достаточно ключей
                    node.keys[i], node.values[i], child_key, child_value = self.get_successor(node.children[i+1]) # меняем значения местами
                    self.Remove(child_key, node.children[i+1]) # удаляем узел
                    node.keys[i] = child_key # обновляем ключ
                    node.values[i] = child_value # обновляем значение
                else: # иначе объединяем два узла
                    self.merge_nodes(node, i)
        else: # иначе продолжаем поиск по дочерним узлам
            if node.leaf: # если узел является листом, значит ключа нет в дереве
                return None
            else:
                if len(node.children[i].keys) < self.N: # если количество ключей в узле меньше чем требуется
                    self.fix_shortage(node, i) # восстанавливаем баланс дерева
                self.Remove(key, node.children[i]) # и продолжаем поиск в дочерних узлах

    def remove_all(self):
        self.root = None # удаляем корневой узел

    def count(self):
        return self.count_elements(self.root) # вызываем вспомогательный метод
    
    def count_elements(self, node):
        count = 0 
        if node is not None: # если узел не пустой
            for i in range(len(node.keys)):
                count += 1 # увеличиваем счетчик на 1
            if not node.leaf: # если узел не является листом, рекурсивно перебираем все дочерние узлы
                for i in range(len(node.children)):
                    count += self.count_elements(node.children[i])
        else:
            return 0 # если узел пустой, возвращаем 0
        return count
    







