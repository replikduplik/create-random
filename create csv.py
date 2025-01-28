import csv
import random

# Random names and surnames
isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Zeynep", "Hasan", "Emine", "Burak", "Elif"]
soyisimler = ["Yılmaz", "Kaya", "Demir", "Çelik", "Şahin", "Aydın", "Öztürk", "Arslan", "Koç", "Bulut"]

# Ensure unique phone numbers
unique_phone_numbers = set()

# Data generation
data = [["first_name", "last_name", "bar_id", "phone_number"]]

for _ in range(20):
    first_name = random.choice(isimler)
    last_name = random.choice(soyisimler)
    bar_id = random.randint(10000, 50000)

    # Generate unique phone numbers
    while True:
        phone_number = f"555-{random.randint(100, 999)}-{random.randint(10, 99)}"
        if phone_number not in unique_phone_numbers:
            unique_phone_numbers.add(phone_number)
            break

    data.append([first_name, last_name, bar_id, phone_number])

# Save to CSV file
file_name = "unique_phone_numbers.csv"
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{file_name}' created successfully!")
