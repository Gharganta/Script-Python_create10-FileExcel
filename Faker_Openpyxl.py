from faker import Faker
from openpyxl import Workbook

fake = Faker()

workbook = Workbook()

foglio = workbook.active
foglio.title = "Utenti"  

foglio.append(["Nome", "Cognome", "Email", "Numero di Telefono"])

for _ in range(10):
    nome = fake.first_name()  
    cognome = fake.last_name()  
    email = fake.email()  
    numero_telefono = fake.phone_number()  
    
    
    foglio.append([nome, cognome, email, numero_telefono])

workbook.save("dati_utenti.xlsx")

print("File Excel 'dati_utenti.xlsx' generato con successo!")