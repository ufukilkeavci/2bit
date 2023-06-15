

# Function takes string as input splits characters and put another string sep(patrameter) between them with spaces
def split_and_join(line, bits):
    # write your code here
    result = ""

    for i in range(0, len(line)):
        result += line[i]
        result += f" Cheer{bits} "

    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line, 2)
    print(result)