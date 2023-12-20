students = [
    {
        'name': 'Anna',
        'class': '10b',
        'grade': {"Matemātika": 9,
                   "Bioloģija": 10,
                   "Fizika": 8
        }
    },
    {
        'name': 'Oskars',
        'class': '10a',
        'grade': {"Matemātika": 6,
                   "Bioloģija": 10,
                   "Fizika": 8,
                   "Programēšana": 9
        }
    }
]

for student in students:
    print(f"{student['name']} ({student['class']}) {student ['grade']}")

# Anna (10b) 9
