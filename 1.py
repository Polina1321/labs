file = open('C:/Users/Mi/Desktop/1 лаба.txt', "r" , encoding="utf-8")
text = file.read()
file.close()

text = text.lower()

letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
letter_counts = {letter: 0 for letter in letters}

total_letters = 0
for char in text:
    if char in letter_counts:
        letter_counts[char] += 1
        total_letters += 1

for letter in sorted(letter_counts):
    chastota = letter_counts[letter] / total_letters if total_letters > 0 else 0
    print(f"{letter}: {chastota:.4f}")



