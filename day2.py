'''Zadanie 1.

Z pliku tekstowego wypisz w konsoli, tylko linie ze słowem Python.'''

file = open('content.txt', 'r')
lines = file.readlines()
text = 'Python'

new_list = []
idx = 0
print("It reads only  lines with a prefer word:")
for line in lines:
    if text in line:
        new_list.insert(idx, line)
        idx += 1
        print(line)

'''Zadanie 2.

Z pliku tekstowego wypisz w konsoli, słowa rozpoczynające się na literę podaną przez użytkownika.'''

file = open('content.txt','r')
text = file.read()
print("\nThis is our text: \n", text)
while True:
    letter = input("Do you want to find a word in our text? Please, enter a first letter: ")
    list_of_words = []
    for word in text.split():
        if word.startswith(letter.lower() or letter.upper()):
            print(word.replace('.', ''))
            list_of_words.append(word)
    if len(list_of_words) == 0:
        print(f"We don't have words in which the first letter is {letter}")










