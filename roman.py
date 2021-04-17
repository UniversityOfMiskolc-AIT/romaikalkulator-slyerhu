__author__ = "Szilveszter Rafael Szabo"
__version__ = "1.0.0"
__email__ = "ssrofficial@gmail.com"
__neptun__ = "YTBR1C"

def int_to_roman(input):
    """ Convert an integer to a Roman numeral.
    
    Keyword arguments: 
    input -- integer numeral
    """

    if not isinstance(input, type(1)):
        raise TypeError("expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


def roman_to_int(input):
    """ Convert a Roman numeral to an integer.
    
    Keyword arguments: 
    input -- roman numeral
    """

    if not isinstance(input, type("")):
        raise TypeError("expected string, got %s" % type(input))
    input = input.upper(  )
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value
        except KeyError:
            raise ValueError('input is not a valid Roman numeral: %s' % input)

    if int_to_roman(sum) == input:
        return sum
    else:
        raise ValueError('input is not a valid Roman numeral: %s' % input)


def add(x, y):
    '''This function adds two number'''
    x = roman_to_int(x)
    y = roman_to_int(y)
    sum = x + y
    return int_to_roman(sum)


def subtract(x, y):
    '''This function substracts two numbers'''
    x = roman_to_int(x)
    y = roman_to_int(y)
    substract = x - y
    return int_to_roman(substract)


def multiply(x, y):
    ''' This function multiplies two numbers'''
    x = roman_to_int(x)
    y = roman_to_int(y)
    multiply = x * y
    return int_to_roman(multiply)


def divide(x, y):
    '''This function divides two numbers'''
    x = roman_to_int(x)
    y = roman_to_int(y)
    divide = int(x / y)
    return int_to_roman(divide)


def main():
    #Print metadata
    print("Author: " + __author__)
    print("Neptun: " + __neptun__)
    print("Version: " + __version__)
    print("E-mail: " + __email__)

    #Printing operations
    print("\nSelect operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        # Take input from the user
        choice = input("\nEnter choice(1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = input("\nEnter first number: ")
            num2 = input("Enter second number: ")
            num1 = num1.upper()
            num2 = num2.upper()

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
