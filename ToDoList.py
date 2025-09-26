import csv 
import os
from datetime import datetime, date

TODO_LIST = "todo_list.csv"
LAST_RESET_FILE = "last_reset.txt"

def main():
    print("="*30)
    print("ToDoList")
    print("="*30)
    while True:
        print("1 - Посмотреть активные задания")
        print("2 - Посмотреть выполненные задания")
        print("3 - Удалить задание")
        print("4 - Добавить задание")
        print("5 - Посмотреть статистику")
        print("0 - Выйти")




def ensure_todo_list():
    if not os.path.exists(TODO_LIST):
        with open(TODO_LIST, "w", newline="", encode = "utf-8") as file:
            writer = csv.writer()
            writer.writerow(["ID", "Задача", "Статус", "Дата создания", "Дата выполнения"])



def get_next_id():
    try:
        with open(TODO_LIST, "r", encode = "utf-8") as file:
            reader = csv.reader()
            next(reader)
            rows = list(reader)
            if not rows:
                return 1
            return max(int(row[0]) for row in rows) + 1
    except:
        return 1



def read_all_tasks():
    ensure_todo_list()
    task = []
    try:
        with open(TODO_LIST, "r", encode = "utf-8") as file:
            reader = csv.reader()
            next(reader)
            tasks = list(reader)
    except:
        pass
    return tasks



def write_all_tasks(tasks):
    with open(TODO_LIST, "w", newline="", encode = "utf-8") as file:
         writer = csv.writer()
         writer.writerow(["ID", "Задача", "Статус", "Дата создания", "Дата выполнения"])
         writer.writerows(tasks)



def add_tasks(task_description):
    task = get_next_id()
    carrent_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



def view_tasks():




def complete_task():



def delete_tasks():



def clear_completed():



def reset_deily():



def show_ststistics():