contacts = [
   {
     'name': 'Anna',
     'age': 17,
     'phone': '654987321',
     'car' : [
        {
        'brand' : 'Audi',
        'year' : 2020,
        'color' : 'Red',
        'engine' : 2.0
        },
        {
         'brand' : 'Tesla',
         'year'  : 2022,
         'color' : 'Red',
         'engine': 50
        }
        ]
   },
   {
     'name': 'Oskars',
     'age': 22,
     'phone': '1234679654'
     'cars' : [
         {
          'brand' : 'BMW',
          'year' : 2012,
          'color' : 'engine',
          'engine' : 45
        }
        ]

   },
   {
     'name': 'Jenifer',
     'age': 18,
     'phone': '6547852147'
   }
]

print(contacts[0]['car_year'])

for contact in contacts:
    print(contact['name'])
    print(contact['age'])
    print(contact['phone'])