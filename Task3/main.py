"""
Розробити скрипт, який приймає шлях до директорії в якості аргументу командного рядка 
і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. 
"""
# імпортуємо бібліотеки
import sys
from pathlib import Path
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Функція для виведення структури директорії
def print_folder_tree(folder_path: Path, indent: str = ""):
    try:
        # Отримуємо список усіх файлів і директорій у поточній директорії
        names = folder_path.iterdir()
        # Виводимо структуру директорії
        for x in names:

            if x.is_dir():
                print(f"{indent}{Fore.GREEN + Style.BRIGHT + str(x.name)}/")
                print_folder_tree(x, indent + "    ")

            else:
                print(f"{indent}{Fore.YELLOW + str(x.name)}")
    # Обробляэмо помилки
    except Exception as e:
        print(f"{Fore.RED} Помилка: {e}")
        return

# функція, яка взаємодіє з командним рядком
def main():
    if len(sys.argv) <= 1:
        print(f"{Style.BRIGHT}{Back.LIGHTRED_EX}Будь ласка, вкажіть вірний шлях до директорії.")
        sys.exit(1)
    else:
        folder_path = Path(sys.argv[1])

    # Перевіряємо, чи існує директорія
    if not folder_path.exists():
        print(f"{Style.BRIGHT}{Back.LIGHTRED_EX}Директорії {folder_path} не існує")
        sys.exit(1)

    # Перевіряємо, чи шлях вказує на директорію
    if not  folder_path.is_dir():
        print(f"{Style.BRIGHT}{Back.LIGHTRED_EX} {folder_path} не є директорією")
        sys.exit(1)

    # Виводимо структуру директорії
    print_folder_tree(folder_path)

if __name__ == "__main__":
    main()