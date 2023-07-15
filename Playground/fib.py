def fib(number):
    if(number == 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return fib(number-1) + fib(number - 2)

def main():
    print("5 pierwszych liczb ciągu fibonacciego wygląda następująco:")
    for number in range(1,6):
        print(fib(number),end=" ")

main()