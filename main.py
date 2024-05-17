import os
import platform
import shutil
import tempfile
import asyncio
import aiosqlite
import requests
import subprocess

async def create_database():
    async with aiosqlite.connect('mydatabase.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                begin_date TEXT,
                end_date TEXT
            );
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                priority INTEGER,
                status_id INTEGER NOT NULL,
                project_id INTEGER NOT NULL,
                begin_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            );
        ''')
        await db.commit()
    print("База данных создана.")

logo = r"""
  _   _                  _               _____ _                            
 | \ | |                | |             / ____| |                           
 |  \| | ___  ___  _ __ | |_ _____  __ | |    | | ___  __ _ _ __   ___ _ __ 
 | . ` |/ _ \/ _ \| '_ \| __/ _ \ \/ / | |    | |/ _ \/ _` | '_ \ / _ \ '__|
 | |\  |  __/ (_) | |_) | ||  __/>  <  | |____| |  __/ (_| | | | |  __/ |   
 |_| \_|\___|\___/| .__/ \__\___/_/\_\  \_____|_|\___|\__,_|_| |_|\___|_|   
                  | |                                                       
                  |_|                                                      
"""

def clear_cache():
    if platform.system() == "Windows":
        os.system('del /f /s /q %temp%\\*')
    else:
        # Для Unix-подобных систем, таких как Linux и MacOS
        os.system('rm -rf ~/.cache/*')
    print("Кэш очищен.")

def clear_temp_files():
    temp_dir = tempfile.gettempdir()
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Не удалось удалить {file_path}. Причина: {e}')
    print("Временные файлы очищены.")

def clear_browser_cache():
    print("Жди во второй версии добавлю!")

def clear_dns_cache():
    # Очистка кэша DNS зависит от операционной системы
    if platform.system() == "Windows":
        subprocess.run(['ipconfig', '/flushdns'], shell=True)
    elif platform.system() == "Linux":
        subprocess.run(['sudo', 'systemd-resolve', '--flush-caches'], shell=True)
    else:
        print("Не удалось определить операционную систему для очистки DNS кэша.")

def clean_system():
    if platform.system() == "Windows":
        os.system('cleanmgr /sageset:1')
    else:
        # Для Unix-подобных систем, таких как Linux и MacOS
        print("Для очистки системы используйте встроенные средства операционной системы.")
  
def clear_os_cache():
    # Очистка кэша операционной системы зависит от операционной системы
    if platform.system() == "Windows":
        subprocess.run(['cleanmgr.exe'], shell=True)
    elif platform.system() == "Linux":
        subprocess.run(['bleachbit'], shell=True)
    else:
        print("Не удалось определить операционную систему для очистки кэша операционной системы.")   
        
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
    
def main():
    print(logo)
    print("Выберите опцию очистки:")
    print_color("1. Очистка кэша", 31)         
    print_color("2. Очистка временных файлов", 32) 
    print_color("3. Очистка системы", 33)   
    print_color("4. Очистка кэша DNS", 34)
    print_color("5. Очистка кэша браузера", 35)
    print_color("6. Очистка кэша операционной системы", 36)

    choice = input("Введите номер опции: ")

    if choice == "1":
        clear_cache()
    elif choice == "2":
        clear_temp_files()
    elif choice == "3":
        clean_system()
    elif choice == "4":
        clear_dns_cache()
    elif choice == "5":    
        clear_browser_cache()
    elif choice == "6":
        clear_os_cache()
    else:
        print("Некорректный выбор.")

if __name__ == "__main__":
    asyncio.run(create_database())
    main()