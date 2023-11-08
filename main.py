names = ['Anna', 'Oskars', 'Jennifer']
numbers = ['123456789', '987654321', '852123674']
name = input('pievieno vārdu: ')
number = input("pievieno numuru; ")
names.append(name)
numbers.append(number)
for i in range(len(names)):
    print(f"{names[i]}: {numbers[i]}")

name_to_delete = input('Nmae to delete: ')
index_to_remove = names.index(name_to_delete)
names.pop(index_to_remove)
numbers.pop(index_to_remove)


for i in range(len(names)):
    print(f"{names[i]}: {numbers[i]}")
