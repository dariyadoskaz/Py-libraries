# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd

#Задание 1
#Импортируйте библиотеку Numpy и дайте ей псевдоним np.
#Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. 
#Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. 
#Будем считать, что каждый столбец - это признак, а строка - наблюдение. 
#Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. 
#Результат запишите в массив mean_a, в нем должно быть 2 элемента

a = np.array([[1, 2, 3, 3, 1], [6, 8, 11, 10, 7]])
print(a)

mean_a = a.mean(axis=1)
print(mean_a)

a = a.transpose()
print(a)

#Задание 2
#Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

a_centered = a - mean_a
#a_centered = a_centered.transpose()
print(a_centered)

#Задание 3
#Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.

a_centered_sp = a_centered.T[0] @ a_centered.T[1]
print(a_centered_sp)

a_centered_sp / (a_centered.shape[0] - 1)

###Тема “Работа с данными в Pandas”

#Задание 1

authors = pd.DataFrame({'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']},
                       columns = ['author_id', 'author_name'])

authors

book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price':[450, 300, 350, 500, 450, 370, 290]},
                    columns=['author_id', 'book_title', 'price'])

book

#Задание 2
#Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

authors_price=pd.merge(authors, book, on='author_id', how='outer')
authors_price

#Задание 3
#Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

top5 = authors_price.nlargest(5, 'price')
top5

#Задание 4
#Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
#author_name, min_price, max_price и mean_price,
#в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
authors_stat

