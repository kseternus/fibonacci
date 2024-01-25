def fibonacci(seq, gen):
    a, c, n = 0, 0, 0
    b = 1
    while n <= seq:
        if gen == 'A':
            print(f'F{n}: {a}')
        c = a + b
        a, b = b, c
        n += 1
    if gen == 'O':
        print(f'F{n-1}: {c-a}')


print('Fibonacci Calculator')
while True:
    try:
        sequence = int(input('What Fn?: '))
        if sequence < 0:
            print('Please enter a positive number!')
            continue
        break
    except ValueError:
        print('Please enter a valid number!')

while True:
    try:
        generate = input('Generate One number or All? (O/A): ').upper()
        if generate not in ['A', 'O']:
            print('Please enter if you want All numbers or just One (A/O):')
            continue
        break
    except AttributeError:
        print('Something went wrong')


fibonacci(sequence, generate)
exit = input()
