'''Magiczne kwadraty

Napisz program, który sprawdzi, czy podany w pliku tekstowym kwadrat, jest kwadratem magicznym.

To znaczy czy w każdej kolumnie, wierszu i po obu przekątnych suma wartości jest taka sama.

Załóż, że w podanym pliku tekstowym znajduje się tylko 1 magiczny kwadrat.

Dodatkowo niech program sprawdzi czy wszystkie wartości w kwadracie są unikalne.'''

def magic_squares(line):
    if sum(line[0:2:-1]) == sum(line[1:3:-1]) == sum(line[2:4:-1]):
        if sum(line[3:5:-1]) == sum(line[4:6:-1]) == sum(line[5:7:-1]):
            if sum(line[6:8:-1]) == sum(line[7:9:-1]) == sum(line[8:10:-1]):
                return "It's magical"
            else:
                return"Not magical"
        else:
            return "Not magical"
    else:
        return "Not magical"




sample_square = open('magic_square_1.txt','r')

square = sample_square.read()

test_square = list(map(int, ','.join(square.split('\n')).replace(' ', '').split(',')))

if magic_squares(test_square) == "It's magical":
    print(f"This square: \n{square}\nis magical! ")
else:
    print("It  isn't a magic square")

