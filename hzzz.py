content = input('ko velies rakstit?: ')
amount = int(input('cik velies rakstit?: '))

file = open('loop.txt', 'w', encoding = 'utf-8')

for i in range(amount):
    file.write(content + '\n')

file.close()