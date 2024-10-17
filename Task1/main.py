"""розробляємо функцію total_salary(path), яка аналізує цей файл 
і повертає загальну та середню суму заробітної плати всіх розробників."""

def total_salary(path):
    try:
        # Відкриваємо файл з вказаним шляхом
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            # Читаємо кожен рядок
            for line in file:
                # Розділяємо рядок на прізвище та зарплату
                name, salary = line.strip().split(',')
                total += int(salary)  # Додаємо зарплату до загальної суми
                count += 1  # Збільшуємо лічильник кількості розробників

            # Обчислюємо середню зарплату
            average = total / count if count != 0 else 0

            # Повертаємо загальну та середню зарплату
            return total, round(average, 2)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

# Приклад виклику функції
path_to_file = 'salary.txt'
total, average = total_salary(path_to_file)
if total and average:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    