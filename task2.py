def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats_list.append({
                        "id": cat_id,
                        "name": name,
                        "age": int(age)  # Перетворення віку на ціле число
                    })
                except ValueError:
                    continue # Пропускаємо некоректні рядки
        return cats_list
    except FileNotFoundError:
        print("Файл із даними про котів не знайдено.")
        return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)