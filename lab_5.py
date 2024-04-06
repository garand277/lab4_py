def reverse(line):
    words = line.split(' ')
    return ' '.join(reversed(words))
    

def reader(path):
    with open(path, 'r') as file:
        for line in file:
            if len(line) > 10:
                line = line[:11]
                yield line.strip()
            else:
                yield line.strip()
            
 
for line in reader('/home/maslenok/Рабочий стол/дыд/file.txt'):
    print(line)

print(reverse('как у кати'))