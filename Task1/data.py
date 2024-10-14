# функції для роботи з даними

def load_data(filename):
    # обробляємо помилки
    try:
        # відкриваємо файл
        with open(filename, 'r', encoding='utf-8') as file:
            # читаємо дані
            return file.readlines()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдений!")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None
    
# функція для очищення даних
def clean_data(raw_data):
    # обробляємо помилки
    if raw_data is None:
        return None
    else:
        # створюємо порожній список
        cleaned_data = []
        # формуємо список кортежів
    for line in raw_data:
        name, salary = line.strip().split(',')
        cleaned_data.append((name, int(salary)))

    return cleaned_data