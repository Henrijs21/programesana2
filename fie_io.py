f = open("demofile.txt", "a")
f.write("100\n")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
f.close()

f = open('counter.txt', 'w') 
for i in range(101):
    f.write(f"{str(i)}\n")
f.close()


with open('counter.txt', 'w') as file:
  for i in range(1, 101):
      file.write(str(i) + '\n')



data = [
    {'name': 'John', 'surname': 'Doe', 'email': 'john.doe@example.com'},
    {'name': 'Jane', 'surname': 'Smith', 'email': 'jane.smith@example.com'},
  
]


with open('dati.txt', 'w') as file:
    for entry in data:
        file.write(f"{entry['name']}, {entry['surname']}, {entry['email']}\n")



with ("contacts.txt", "w") as file:
    for i in range(1, 11):
        f.write(f"name{i}, surname{i}, email{i}\n")