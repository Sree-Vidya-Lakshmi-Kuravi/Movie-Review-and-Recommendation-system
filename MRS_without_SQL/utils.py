import csv

def get_headers(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return reader.fieldnames

def generate_id(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        id = list(reader)[-1].get('id')
        return str(int(id) + 1)

def read_csv(filename):
    with open(filename) as f:
        csv_data = csv.DictReader(f)
        return list(csv_data)

def write_row(filename, data):
    with open(filename, 'a', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = get_headers(filename))
        writer.writerow(data)
        return "Single row has been added successfully"

def write_rows(filename, data):
    headers = get_headers(filename)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = headers)
        writer.writeheader()
        writer.writerows(data)
        return "Multiple rows has been added successfully"


# path = r"MRS_without_SQL\data\users.csv"
# user = {'id' : generate_id(path), 'username' : 'anirudh', 'password':'ani', 'email':'ani.r@example.com'}
# users = read_csv(path)
# users.append(user)
# print(users)
# write_rows(path, users)


