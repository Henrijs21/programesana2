phonebook = [('Rihards', '27857748'), ('Maija', '17593772')]
dzest = input('Ievadi vārdu, kuru izdzēst: ')

for i in phonebook:
    if dzest  in i:
        phonebook .remove(i)

print(phonebook)