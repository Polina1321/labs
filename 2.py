file = open("C:/Users/Mi/Desktop/2 лаба.txt", "r")
numbers = list(map(int, file.read().split()))
file.close()

if numbers:
    min_znach = min(numbers)
    min_index = numbers.index(min_znach)
    numbers[min_index] *= 2

new_file = open("C:/Users/Mi/Desktop/результат.txt", "w")
new_file.write(" ".join(map(str, numbers)))
new_file.close()