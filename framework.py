# framework in python.

MENU_FILE = "menu.cfg"
FIELDS_FILE = "field_names.cfg"
RECORDS_FILE_NAME = "details.dat"

field_names = []
records = []
user_option = 1
fields_count = 0

def main():
    global records
    records = load_records()
    global field_names
    field_names = get_field_names()

    while user_option == 1:
        with open(MENU_FILE, "r") as fp_menu:
            print(fp_menu.read())
        choice = int(input("Enter your choice: "))
        options = [create, show, update, delete, exit]
        options[choice - 1]()

def get_field_names():
    with open(FIELDS_FILE, "r") as fp_field_names:
        field_names = eval(fp_field_names.read())
    global fields_count
    fields_count = int(len(field_names))
    return field_names

def load_records():
    with open(RECORDS_FILE_NAME, "r") as records_file:
        records =  records_file.read()
        if records:
            return eval(records)
        return []

def save_records(records):
    with open(RECORDS_FILE_NAME, "w") as records_file:
        records_file.write(str(records))

def create():
    record = []
    for counter in range(fields_count):
        record.append(input("Enter " + field_names[counter] + ": "))
    record.append('A')
    records.append(record)
    save_records(records)
    print_acknowledgement("created")

def show():
    if records:
        field_values_count = fields_count + 1
        for counter in range(fields_count):
            print(f"{field_names[counter]:20}", end = "")
        print("\tstatus\n")
        for record in records:
            for counter in range(field_values_count):
                print(f"{record[counter]:20}", end = "")
            print("\n")
    else:
        print("No records found! ")

def find_record(key):
    for record in records:
        if record[0] == key:
            return record
    print("Record not found")
    return []

def update():
    key = input("Enter key to update: ")
    record = find_record(key)
    if record:  
        record[fields_count - 1] = input("Enter " + field_names[fields_count - 1] + " to update: ")
        save_records(records)
        print_acknowledgement("updated")

def delete():
    key = input("Enter key to delete: ")
    record = find_record(key)
    if record:  
        record[fields_count] = 'C'
        save_records(records)
        print_acknowledgement("deleted")

def print_acknowledgement(operation):
    print("Record ", operation, "successfully")

def exit():
    global user_option
    user_option = 0
        
if __name__ == "__main__":
    main()