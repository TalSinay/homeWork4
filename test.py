def Q11(x):
    numbers='123456789' * x
    new_numbers=iter(numbers)
    columns=int(x / 2)+1
    for row in range(columns+1):
        print(" "*(columns-row),end='')
        for col in range(row*2-1):
            print(next(new_numbers),end='')
        print('')
    for row in range(columns-1,0,-1):
        print(" " * (columns - row), end='')
        for col in range(row * 2 - 1):
            print(next(new_numbers), end='')
        print('')




Q11(11)