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
        print("2 - Посмотреть все задания")
        print("3 - Удалить задание")
        print("4 - Добавить задание")
        print("6 - Отметить задачу как завершенную")
        print("7 - Очистить завершенные")
        print("0 - Выйти")
        print(" ")
        choice = input("Введите номер действия: ").strip()
        if choice == "4":
            task = input("Введите описание: ").strip()
            if task: 
                add_tasks(task)
            else:
                print("Описание не может быть пустым")
        if choice == "1":
            view_tasks(show_complited = False)
        if choice == "2":
            view_tasks(show_complited = True)
        if choice == "6":
            try:
                task_id = int(input("Введите ID: ").strip())
                complete_task(task_id)
            except ValueError:
                print("Нужно ввести число! ")
        if choice == "3":
            try:
                task_id = int(input("Введите ID: ").strip())
                delete_task(task_id)
            except ValueError:
                print("Нужно ввести число! ")
        if choice == "7":
            clear_completed()




def ensure_todo_list():
    if not os.path.exists(TODO_LIST):
        with open(TODO_LIST, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Задача", "Статус", "Дата создания", "Дата выполнения"])



def get_next_id():
    try:
        with open(TODO_LIST, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            rows = list(reader)
            if not rows:
                return 1
            return max(int(row[0]) for row in rows) + 1
    except:
        return 1



def read_all_tasks():
    ensure_todo_list()
    tasks = []
    with open(TODO_LIST, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        tasks = list(reader)
    return tasks



def write_all_tasks(tasks):
    with open(TODO_LIST, "w", newline="", encoding="utf-8") as file:
         writer = csv.writer(file)
         writer.writerow(["ID", "Задача", "Статус", "Дата создания", "Дата выполнения"])
         writer.writerows(tasks)



def add_tasks(task_description):
    task_id = get_next_id()
    carrent_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks = read_all_tasks()
    tasks.append([task_id, task_description, "Активно", carrent_date, " "])
    write_all_tasks(tasks)
    print("Успешное сохранение")


def view_tasks(show_complited = False):
    tasks = read_all_tasks()
    print(tasks)
    if not tasks:
        print("Список дел пуст")
        return
    active_tasks = [task for task in tasks if task[2] == "Активно"]
    completed_tasks = [task for task in tasks if task[2] == "Завершено"]
    print(f"Активные задачи: ({len(active_tasks)})")
    if active_tasks:
        for task in active_tasks:
            status = "[Активно]" if task[2] == "Активно" else "[Завершено]"
            print(f"{task[0]}, {status}, {task[1]}, создано: {task[3]}")
    else:
        print("Нет активных задач")
    if show_complited and completed_tasks:
        print(f"Выполненные задачи: ({len(completed_tasks)})")
        for task in completed_tasks:
            status = "[Активно]" if task[2] == "Активно" else "[Завершено]"
            print(f"{task[0]}, {status}, {task[1]}, выполнено: {task[4]}")        



def complete_task(task_id):
    tasks = read_all_tasks()
    completed=False
    for task in tasks:
        if task[0] == str(task_id):
            if task[2] == "Активно":
                task[2] = "Завершено"
                task[4] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                completed = True
                print("Задача завершена")
        else:
            print("Задача уже завершена")
        if completed:
            write_all_tasks(tasks)
        else:
            print("Задача с таким ID не найдена")



def delete_task(task_id):
    tasks = read_all_tasks()
    original_count = len(tasks)
    tasks = [task for task in tasks if task[0]!=str(task_id)]
    if len(tasks) < original_count:
        write_all_tasks(tasks)
        print("Успешно удалено")
    else:
        print("Такой задачи нет")



def clear_completed():
    tasks = read_all_tasks()
    active_tasks = [task for task in tasks if task[2]=="Активно"]
    if len(active_tasks) < len(tasks):
        write_all_tasks(active_tasks)
        print("Очищены")
    else:
        print("Уже очищены")



if __name__ == "__main__":
    main()