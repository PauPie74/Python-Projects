def square_digits(num):
    squares = ""
    for digit in str(num):
        number = int(digit)**2
        squares+=str(number)
    result = int(squares)
    return result