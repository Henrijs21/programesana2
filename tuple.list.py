phonebook_with_tuple =[('Annna','525415351'),('Oskars','46375752')]
name_to_add = input ('Ivadi vārdu:  ')
number_to_add = input ('ievadi numuru')
phonebook_with_tuple.append(name_to_add, number_to_add)
print(phonebook_with_tuple)


name_to_delete = input("kuru gribi izdzēst")

index_delete= phonebook_with_tuple.index(name_to_delete)
print(phonebook_with_tuple)