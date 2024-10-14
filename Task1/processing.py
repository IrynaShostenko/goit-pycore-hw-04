def calculate_salaries(cleaned_data):
    """
    Функція для обчислення загальної та середньої зарплат.
    
    """
    total_salary = 0
    count = len(cleaned_data)
    
    for name, salary in cleaned_data:
        total_salary += salary
        average_salary = total_salary / count if count > 0 else 0
        
    return int(total_salary), round(float(average_salary), 2)