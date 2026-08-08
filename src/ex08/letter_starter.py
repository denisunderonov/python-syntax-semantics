import sys

def main():
    email = sys.argv[1]
    name = email.split('.')[0].capitalize()
    
    with open('employees.tsv', 'r', encoding="utf-8") as employee:
        for line in employee:
            line_tuple = line.split('\t')
            found_name = line_tuple[0]
            if found_name == name:
                with open('emails.txt', 'r', encoding="utf-8") as emails:
                    for em in emails:
                        if em.strip() == email.strip():
                            print(f'{name}, добро пожаловать в нашу команду! Мы уверены, что работать вместе с тобой будет очень приятно. Для нас это важно - мы стремимся, чтобы в компании работались именно такие люди.')
                emails.close()
    employee.close()
            
if __name__ == "__main__":
    main()
          
