"""Пишемо консольного бота помічника, який розпізнаватиме команди, 
що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
"""

def parse_input(user_input):
    """
    Парсер команд. Повертає команду і список аргументів.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника.
    """
    if len(args) < 2:
        return "Недостатньо аргументів. Використовуйте формат: add [ім'я] [номер телефону]"
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} додано."

def change_contact(args, contacts):
    """
    Змінює існуючий контакт.
    """
    if len(args) < 2:
        return "Недостатньо аргументів. Використовуйте формат: change [ім'я] [новий номер телефону]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Контакт {name} оновлено."
    else:
        return f"Контакт {name} не знайдено."

def show_phone(args, contacts):
    """
    Показує номер телефону за ім'ям контакту.
    """
    if len(args) < 1:
        return "Недостатньо аргументів. Використовуйте формат: phone [ім'я]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Контакт {name} не знайдено."

def show_all(contacts):
    """
    Виводить усі контакти.
    """
    if not contacts:
        return "Контакти відсутні."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Ласкаво просимо до бот-асистента!")
    
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break

        elif command == "hello":
            print("Як я можу допомогти?")
        
        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))
        
        else:
            print("Невірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
