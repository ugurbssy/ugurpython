file = open("C:\\Users\ASUS\Desktop\wt.txt", "r")
text = file.read()

for char in '?+-.,\n':
    text = text.replace(char, ' ')
text = text.lower()
word_list = text.split()

d = {}
for word in word_list:
   d[word] = d.get(word, 0) + 1

print(d,sep = '\n')