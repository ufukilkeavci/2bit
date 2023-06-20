

# Function takes string as input splits characters and put another string sep(patrameter) between them with spaces
def split_and_join(line, bits):
    # write your code here
    result = ""

    for i in range(0, len(line)):
        result += line[i]
        if bits != 0 and i != len(line) - 1:
            result += f" Cheer{bits} "
        else:
            result += " "

    return result

if __name__ == '__main__':
    line = input()
    bit_amount = None
    while bit_amount is None:
        try:
            bit_amount = int(input("Enter bit amount: "))
        except ValueError:
            bit_amount = None
    result = split_and_join(line, bit_amount)
    print(result)