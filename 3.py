import csv
class Contour:

    def __init__(self, initial_file):
        self.initial_file = initial_file
        self.list = None # для перетаскивания матрицы между методами

    def read_and_clean (self):
        with open (self.initial_file, encoding='UTF8') as file_obj:
            reader = csv.reader(file_obj)
            next(reader)
            self.list = []
            for row in reader:
                del row[0:2] # сразу выкинуть 1,2,3 и столбцы Z
                del row[2]
                del row[4]
                self.list.append(row)
        print (self.list)
        print (len(self.list))

    def filtration_zeros(self):
        filtr_list =[]
        for row in self.list:
            if not (row [0] == row [2] and row [1] == row [3]):  # сравнение строк по индексам элементов
                filtr_list.append(row)
        self.list = filtr_list
        print (self.list)
        print(len(self.list))

    def filtration_doubles (self):
        filtr_list = []
        unic_rows = set() # уникальные значения для add и touple потому что append не работает
        for row in self.list:
            row_to_tuple = tuple(row) # вкинуть строку в неизменяемый кортеж что бы сравнивать
            if row_to_tuple not in unic_rows:  # проверка на присутствие среди уникальных строк
                unic_rows.add(row_to_tuple) # доброс в множесво уникальных строк
                filtr_list.append(row)
        self.list = filtr_list
        print(self.list)
        print(len(self.list))


    def assembling (self): # 3,4 за 1, 2 по индексу
        filtr_list = []
        for row in self.list:
            filtr_list.append([row[2], row[3]]) # по индексу  1 и 2 под 3 и 4
            filtr_list.append([row[0],row[1]])
        self.list = filtr_list
        print(self.list)
        print(len(self.list))

    def to_txt (self):
        with open('export', 'w') as file:
            for row in self.list:
                file.write(f"{row[0]},{row[1]}\n") # как писать в файл



kont_1 = Contour (r'Контур работ 2.csv')

r_a_c_1 = kont_1.read_and_clean()
f_z_1 = kont_1.filtration_zeros()
a_1 = kont_1.assembling()
f_z_2 = kont_1.filtration_doubles()
t_t_1 = kont_1.to_txt()


