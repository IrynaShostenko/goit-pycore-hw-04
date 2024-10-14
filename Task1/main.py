"""розробляємо функцію total_salary(path), яка аналізує цей файл 
і повертає загальну та середню суму заробітної плати всіх розробників."""

# імпортуємо функції
from data import load_data, clean_data
from processing import calculate_salaries

def main():
    path = 'salary.txt'
    raw_data = load_data(path)
    
    if raw_data is None:
        print("Помилка при читанні файлу.")
        return
    
    # очищуємо дані
    cleaned_data = clean_data(raw_data)
    
    # обчислюємо загальну та середню зарплату
    total, average = calculate_salaries(cleaned_data)
    
    # виводимо результати
    print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# перевіряємо чи
if __name__ == '__main__':
    main()