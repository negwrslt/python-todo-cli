"""
ToDo List CLI
A simple, robust, object-oriented Command-Line To-Do List Manager with CSV persistence.
"""

import csv
import os


class Task:
    """
    مدل‌سازی هر کار در لیست وظایف
    Represents an individual task in the to-do list.
    """
    def __init__(self, name: str, description: str, priority: str):
        self.name = name.strip()
        self.description = description.strip()
        self.priority = priority.strip().capitalize()

    def __str__(self) -> str:
        return f"{self.name} | {self.description} | اولویت: {self.priority}"

    def to_row(self) -> list:
        return [self.name, self.description, self.priority]


class ToDoList:
    """
    مدیریت تسک‌ها شامل افزودن، حذف، نمایش و همگام‌سازی با فایل CSV
    Manages task list operations and CSV persistence.
    """
    def __init__(self, filename: str = "todolist.csv"):
        self.filename = filename
        self.tasks: list[Task] = []
        self.load_from_csv()

    def add_task(self, task: Task) -> bool:
        """افزودن تسک جدید به لیست و ذخیره در فایل"""
        if not task.name:
            print("خطا: نام کار نمی‌تواند خالی باشد.")
            return False
        self.tasks.append(task)
        print(f"کار '{task.name}' با موفقیت اضافه شد.")
        self.save_to_csv()
        return True

    def remove_task(self, index: int) -> bool:
        """حذف تسک بر اساس شماره ایندکس (0-based) با بررسی محدوده معتبر"""
        if index < 0 or index >= len(self.tasks):
            print("شماره وارد شده نامعتبر است.")
            return False
        removed = self.tasks.pop(index)
        print(f"کار '{removed.name}' حذف شد.")
        self.save_to_csv()
        return True

    def show_tasks(self) -> list[Task]:
        """نمایش لیست کارها و بازگرداندن آرایه تسک‌ها"""
        if not self.tasks:
            print("لیست خالی است.")
        else:
            print("\n" + " لیست کارها ".center(32, "-"))
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        return self.tasks

    def save_to_csv(self) -> None:
        """ذخیره کارها در فایل CSV با فرمت استاندارد UTF-8-SIG"""
        with open(self.filename, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["نام", "توضیحات", "اولویت"])
            for task in self.tasks:
                writer.writerow(task.to_row())

    def load_from_csv(self) -> None:
        """بارگذاری کارها از فایل CSV با مدیریت عدم وجود فایل یا ساختار ناقص"""
        if not os.path.exists(self.filename):
            return

        self.tasks = []
        try:
            with open(self.filename, "r", encoding="utf-8-sig") as file:
                reader = csv.reader(file)
                next(reader, None)  # رد کردن هدر جدول
                for row in reader:
                    if row and len(row) >= 3:
                        self.tasks.append(Task(row[0], row[1], row[2]))
        except Exception as e:
            print(f"خطا در خواندن فایل CSV: {e}")


def create_task_from_user() -> Task | None:
    """دریافت اطلاعات تسک جدید از کاربر با اعتبارسنجی اولیه"""
    name = input("نام کار: ").strip()
    if not name:
        print("خطا: نام کار نمی‌تواند خالی باشد.")
        return None
    description = input("توضیحات: ").strip()
    priority = input("اولویت (بالا / متوسط / پایین): ").strip()
    if not priority:
        priority = "متوسط"
    return Task(name, description, priority)


def main():
    """حلقه اصلی اجرای منوی برنامه"""
    todo_list = ToDoList()

    while True:
        print("\n=== منوی مدیریت کارها ===")
        print("1. نمایش کارها")
        print("2. اضافه کردن کار جدید")
        print("3. حذف کار")
        print("0. خروج")

        choice = input("انتخاب کنید: ").strip()

        if choice == "1":
            todo_list.show_tasks()

        elif choice == "2":
            new_task = create_task_from_user()
            if new_task:
                todo_list.add_task(new_task)

        elif choice == "3":
            if not todo_list.tasks:
                print("لیست خالی است و کاری برای حذف وجود ندارد.")
                continue
            todo_list.show_tasks()
            try:
                number = int(input("شماره کار برای حذف: ")) - 1
                todo_list.remove_task(number)
            except ValueError:
                print("لطفاً عدد وارد کنید.")

        elif choice == "0":
            print("خروج از برنامه...")
            break

        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")


if __name__ == "__main__":
    main()
