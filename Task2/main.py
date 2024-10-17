"""
розробляємо функцію, яка читає файл та 
повертає список словників з інформацією про кожного кота.

"""
def get_cats_info(path):
    try:
        # Відкриваємо файл з вказаним шляхом
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            # Читаємо кожен рядок
            for line in file:
                # Розділяємо рядок на id, name, age
                id, name, age = line.strip().split(',')
                cats_info.append({"id" : id, "name" : name, "age" : age})

 

            # Повертаємо словник з ключами "id", "name", "age" для кожного кота
            return cats_info

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

# Приклад виклику функції
path_to_file = 'cats.txt'
cats_info = get_cats_info(path_to_file)
if cats_info:
    print(cats_info)
    