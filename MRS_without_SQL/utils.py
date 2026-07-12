import csv

def read_csv(path):
    with open(path, 'r', newline = '') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            data.append(row)
    return data
        

def write_row(path, data):
    with open(path, 'a', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = get_headers(path))
        writer.writerow(data)

def write_rows(filename, data):
    headers = get_headers(path)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = headers)
        writer.writeheader()
        writer.writerows(data)


def get_headers(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return reader.fieldnames


def generate_id(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        id = list(reader)[-1].get('id')
        return int(id) + 1


# path = r"MRS_without_SQL\data\users.csv"
# user = {'id' : generate_id(path), 'username' : 'anirudh', 'password':'ani', 'email':'ani.r@example.com'}
# users = read_csv(path)
# users.append(user)
# print(users)
# write_rows(path, users)


