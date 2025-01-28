def number_to_strings(argument, a ,b):
    switcher = {
        '+': print(a+b),
        '-': print(a-b),
        '/': print(a/b),
        '%': print(a%b),
        '*': print(a*b),
    }

    return switcher.get(argument,"NOT FOUND")

#DRIVER PROGRAM
if __name__ == "__main__":
    argument='+'
    a = 4
    b=5
    print(number_to_strings(argument, a ,b ))
