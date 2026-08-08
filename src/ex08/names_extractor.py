import sys

def main():
    file_path = sys.argv[1]
    
    with open('employees.tsv', 'w', encoding="utf-8") as employee:
        employee.write('Name\tSurname\tE-mail\n')
        with open(file_path, 'r', encoding="utf-8") as file:
            for email in file:
                name_surname = email.split('@')[0]
                name = name_surname.split('.')[0]
                surname = name_surname.split('.')[1]
                employee.write(f"{name.capitalize()}\t{surname.capitalize()}\t{email}")
        file.close()
    employee.close()
    
if __name__ == "__main__":
    main()
          
