records = []

me = {'Name': 'Kris', 'Age': 20}

records.append(me)
records.append( {'Name': 'Joe', 'Age': 23})

print(records)
for rec in records:
    print(rec['Name'])

