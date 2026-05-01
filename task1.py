def total_salary(path):
    total = 0.0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка у форматі даних рядка: {line}")
        
        if count == 0:
            return 0.0, 0.0
            
        average = total / count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0.0, 0.0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0.0, 0.0

if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")