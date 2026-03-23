import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_tree(path, indent=""):
    try:
        base_path = Path(path)
        
        if not base_path.exists():
            print(Fore.RED + "Помилка: Шлях не існує.")
            return

        items = sorted(base_path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for item in items:
            if item.name in ["venv", ".git", "__pycache__"]:
                continue

            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}")
                visualize_tree(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")

    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.YELLOW + "Будь ласка, вкажіть шлях до директорії.")
        print("Приклад: python3 task3.py .")
    else:
        target_path = sys.argv[1]
        visualize_tree(target_path)