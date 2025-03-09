#В заданном тексте определить частоту, с которой встречаются в тексте различные буквы русского алфавита (в долях от общего количества букв)
text = "я учусь в лучшем вузе в мире!"

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



