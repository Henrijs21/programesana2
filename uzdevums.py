day = input("ievadi skaļumu")
loudness = int(input("Ievadi sakļumu no 0 līdz 100: "))

if day == "pirmdiena" or day == "svētdiena" and loudness > 40:
    print("ļoti skaļi vajag klusāk ")
else:
    print ("chill")   