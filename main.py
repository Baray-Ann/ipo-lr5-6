text=open('text.txt', 'r', encoding="utf-8") #Открытие файла text.txt для чтения с помощью режима 'r', кодировки utf-8 и присваивание его переменной text
str1=text.read().split(" ") #Создание списка, содержащего слова текста из файла
words=open('output.txt', 'w', encoding="utf-8") #Открытие файла output.txt для записи с помощью режима 'w', кодировки utf-8 и присваивание его переменной words
str2=list() #Создание пустого списка
for word in str1: #Цикл for для перебора элементов(word) в списке str1
    if word not in str2: #Цикл if для проверки отсутствия элемента(word) в списке str2
        words.write(word) #Добавлениие уникального элемента в файл output.txt
    str2.append(word) #Добавление элемента(word) в список str2
