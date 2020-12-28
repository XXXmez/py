#Начало
message_Hello_p = "Hello Puthon world!"
print (message_Hello_p)

message_Hello_p = "Hello Python Crash Course world!"
print(message_Hello_p)

#Строки
name_ada = "ada lovelace"
print(name_ada.title()) #Ada Lovelace
print(name_ada.upper()) #ADA LOVELACE
print(name_ada.lower()) #ada lovelace

#Конкатенация
first_name_ada = "ada"
last_name_ada = "lovelace"
full_name_ada = first_name_ada + " " + last_name_ada
print(full_name_ada)
print("Hello, " + full_name_ada.title() + "!") #Hello, Ada Lovelace!
massage_ada_lovelace = "Hello, " + full_name_ada.title() + "!"
print(massage_ada_lovelace) #Hello, Ada Lovelace!

#Табуляции и разрывы строк
print("\tHello\tworld") #	Hello	world
print("Hello\nworld") #Hello
#                      world
print("1 one \n\t1.1 two\n\t1.2 free\n\t1.3 for")

#Удаление пропусков
delete_prop_one = "            Ruslan            "
delete_prop_right = delete_prop_one.rstrip()
delete_prop_left = delete_prop_one.lstrip()
delete_prop_two = delete_prop_one.strip()
print(delete_prop_right)
print(delete_prop_left)
print(delete_prop_two)

#Предотвращение синтаксических ошибок в строках
message_one_of_pyt_1 = "One of Python's strengths is its diverse community."
print(message_one_of_pyt_1)
#message_one_of_pyt_2 = 'One of Python's strengths is its diverse community.'
#print(message_one_of_pyt_2)   #SyntaxError: invalid syntax


#Числа
#Целые числа
#целыми числами можно выполнять операции
print(2 + 6)
print(6 - 2)
print(6 / 2)
#операции возведения в степень
print(2 ** 6)
#Python также существует определенный порядок операций
print(2 + 2 * 2)
print((2 + 2) * 2)

#Вещественные числа
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
#Однако
print(0.2 + 0.1) #0.30000000000000004
print(3 * 0.1)   #0.30000000000000004


#Предотвращение ошибок типов с использованием функции str()
age_error_str = 23
message_error_str = "Happy " + str(age_error_str) + "rd Birthday!"
print (message_error_str)

#деление
print(3/2)   #1.5
print(3.0/2)   #1.5
print (3/2.0)   #1.5
print(3.0/2.0)   #1.5

#Комментарии
# Say hello to everyone.
print("Hello Python people!")

#Философия Python
import this

#конец 2 главы
#начало 3 главы


#3 Списки
bicycles_one = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles_one)
#Обращение к элементам списка
print(bicycles_one[2].title())
print(bicycles_one[-1].title())

#Использование отдельных элементов из списка
bicycles_two = ['trek', 'cannondale', 'redline', 'specialized']
message_bicycles_two = "My first bicycle was a " + bicycles_two[0].title() + "."
print(message_bicycles_two)

#Изменение, добавление и удаление элементов
#Изменение элементов в списке
#стр 51