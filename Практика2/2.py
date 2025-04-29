import os
import time

# Путь к директории с файлами
directory = '/Users/blooomy/Desktop/slice'  # Замените на ваш путь

def cleanup_old_files():
    current_time = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Проверка, является ли файл старше 1 минуты (60 секунд)
        if os.path.isfile(file_path) and (current_time - os.path.getmtime(file_path)) > 60:
            os.remove(file_path)
            print(f"Удален файл: {file_path}")

if __name__ == "__main__":
    while True:
        cleanup_old_files()
        time.sleep(120)  # 2 минуты