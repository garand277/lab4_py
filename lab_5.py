def reader(path):
    with open(path, encoding='utf-8', mode='r') as file:
        for line in file:
            if len(line) > 20:
                line = line[:21]
                yield line.strip()
            else:
                yield line.strip()

def reverse(str):
    words = str.split(' ')
    return ' '.join(reversed(words))

line = map(reverse, reader('C:/Users/andru/lab4_py/file.txt'))

for x in line:
    print(x)