letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getItemType(first: str, second: str, third: str):

    for c in letters:
        if c in first or second and c in second and c in third:
            return (ord(c) - 96) if c.islower() else (ord(c) - 64 + 26)
    return 0


with open("input", "r") as file:
    lines = file.readlines()
    sum = 0
    i = 0
    while i in range (0, len(lines) - 2):
        print(lines[i].strip() + " " + lines[i+1].strip() + " " + lines[i+2].strip() )
        sum += getItemType(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip())
        i = i + 3
    print(sum)

# Second part

