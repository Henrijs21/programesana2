file = open('gbp.txt', 'r', encoding='utf-8')
rate = float(file.read())
file.close()

amount = float(input('Ievadi naudas daudzumu EUR: '))
new_amount = amount * rate

print(f'{amount} EUR = {new_amount} GBP')