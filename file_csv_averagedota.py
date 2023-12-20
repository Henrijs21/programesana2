import csv

# Specify the path to your CSV file
csv_file_path = "vps_ce_rezultati_vsk_2022_2023.csv"

# Open the CSV file in read mode
with open(csv_file_path, mode='r', encoding='utf-8') as file:

    # Create a CSV reader object
    csv_reader = csv.reader(file, delimiter=';')

    # Read and print each row from the CSV file
    for row in csv_reader:
        print("Pārbaudījums:", row[1])
        print("Izglītības iestādes nosaukums:", row[2])
        print("Kopvērtējums, procentos:", row[9])
        print("-" * 20)
