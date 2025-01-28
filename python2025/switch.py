def number_to_strings(argument):
    switcher = {
        0: "ZERO",
        1: "ONE",
        2: "TWO"
    }

    return switcher.get(argument,"NOT FOUND")

#DRIVER PROGRAM
if __name__ == "__main__":
    argument=10
    print(number_to_strings(argument))
