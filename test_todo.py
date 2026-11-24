"""
Unit tests for ToDoList CLI
"""

import os
import unittest
from todo import Task, ToDoList


class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.test_csv = "test_todolist.csv"
        self.todo = ToDoList(filename=self.test_csv)

    def tearDown(self):
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_task_creation(self):
        task = Task("خرید کتاب", "خرید کتاب پایتون", "بالا")
        self.assertEqual(task.name, "خرید کتاب")
        self.assertEqual(task.description, "خرید کتاب پایتون")
        self.assertEqual(task.priority, "بالا")
        self.assertEqual(task.to_row(), ["خرید کتاب", "خرید کتاب پایتون", "بالا"])

    def test_add_task_and_persistence(self):
        task = Task("ورزش", "یک ساعت پیاده‌روی", "متوسط")
        self.assertTrue(self.todo.add_task(task))
        self.assertEqual(len(self.todo.tasks), 1)

        # Reload from CSV to verify persistence
        reloaded_todo = ToDoList(filename=self.test_csv)
        self.assertEqual(len(reloaded_todo.tasks), 1)
        self.assertEqual(reloaded_todo.tasks[0].name, "ورزش")

    def test_add_empty_task_rejected(self):
        task = Task("", "توضیحات", "پایین")
        self.assertFalse(self.todo.add_task(task))
        self.assertEqual(len(self.todo.tasks), 0)

    def test_remove_task(self):
        task1 = Task("کار 1", "توضیح 1", "بالا")
        task2 = Task("کار 2", "توضیح 2", "پایین")
        self.todo.add_task(task1)
        self.todo.add_task(task2)

        # Valid removal
        self.assertTrue(self.todo.remove_task(0))
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0].name, "کار 2")

        # Invalid index out of range
        self.assertFalse(self.todo.remove_task(5))

        # Negative index check (edge case)
        self.assertFalse(self.todo.remove_task(-1))


if __name__ == "__main__":
    unittest.main()
