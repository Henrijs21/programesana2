new_file = open('fails.txt', 'w', encoding = 'utf-8')
new_file.write('python')
new_file.close()

new_file = open('fails.txt', 'r', encoding = 'utf-8')
file_content = new_file.read()
print(file_content)

new_file.close()

new_file = open('failss.txt', 'w')
new_file.write = input('what do you want to write?: ')

content = input('ko velies rakstit?: ')
amount = int(input('cik velies rakstit?: '))

file = open('loop.txt', 'w', encoding = 'utf-8')

for i in range(amount):
    file.write(content + '\n')

file.close()