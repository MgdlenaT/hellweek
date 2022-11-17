'''Użytkownik podaje liczbę w zakresie od 101 - 99999.
Napisz program, który zamieni kolejnością cyfry w podanej liczbie.'''

number = int(input("Enter a number: "))
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print("Reversed Number: " + str(reversed_number))