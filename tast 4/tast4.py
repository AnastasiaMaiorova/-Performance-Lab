def tast4():
    m = 'numbers.txt'
    with open(m, 'r') as file:
        number = file.readlines()
        numbers = [int(num.strip()) for num in number]
    numbers.sort()
    meredian = numbers[len(numbers) // 2]
    result = sum(abs(n - meredian) for n in numbers)
    return result

print(tast4())