import sys

def call_center(recipients, clients):
    # Клиенты, которые еще не видели рекламное письмо
    recip_set = set()
    clients_set = set()
    for item in recipients:
        recip_set.add(item)
    
    for item in clients:
        clients_set.add(item)
    
    result = clients_set - recip_set
    print("Передать в колл-центр список клиентов:", result)
    
def potential_clients(clients, participants):
    # Не клиенты
    particip_set = set()
    clients_set = set()
    for item in participants:
        particip_set.add(item)
    
    for item in clients:
        clients_set.add(item)
    
    result = particip_set - clients_set
    print("Отправить вводное письмо участникам:", result)
    
def loyalty_program(clients, participants):
    # Клиенты, которые не участвовали в мероприятии
    particip_set = set()
    clients_set = set()
    for item in participants:
        particip_set.add(item)
    
    for item in clients:
        clients_set.add(item)
    
    clients_particip = particip_set - (particip_set - clients_set) # Клиенты, которые участвовали в мероприятии
    result = clients_set - clients_particip
    print("Отправить видео и слайды клиентам:", result)
    
    
def main(): 
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
    'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
    'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    task = sys.argv[1]
    if task == "call_center":
        call_center(recipients, clients)
    elif task == "potential_clients":
        potential_clients(clients, participants)
    elif task == "loyalty_program":
        loyalty_program(clients,participants)
    else:
        pass
    
if __name__ == "__main__":
    main()
          
