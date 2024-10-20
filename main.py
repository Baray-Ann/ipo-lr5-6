text=open('text.txt', 'r', encoding="utf-8")
str1=text.read().split(" ")
words=open('output.txt', 'w', encoding="utf-8")
str2=list()
for word in str1:
    if word not in str2:
        words.write(word)
    str2.append(word)