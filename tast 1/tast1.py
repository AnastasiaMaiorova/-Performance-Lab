def tast1(n, m):

    numbers = list(range(1, n + 1))
    list_numbers = []
    start = 0

    for circle in range(m):
        circle_m = []
        if circle < m - 1:
            for step in range(m):
                position = (start + step) % n
                circle_m.append(str(numbers[position]))
            list_numbers.append(circle_m[0])
            start = (start + m) % n - 1
        else:
            circle_m = list_numbers
        print(''.join(circle_m))

import sys

if len(sys.argv) != 3:
    print('Введите: python tast1.py n m')
    sys.exit(1)

n = int(sys.argv[1])
m = int(sys.argv[2])

#n = 4
#m = 3
tast1(n, m)