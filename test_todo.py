import unittest
from main import Todo, add_todo, complete_todo

class TestTodoApp(unittest.TestCase):
    def test_todo_class_exists(self):
        """Test that Todo class exists with required properties"""
        todo = Todo("Test task")
        self.assertEqual(todo.title, "Test task")
        self.assertFalse(todo.completed)
    
    def test_add_todo(self):
        """Test add_todo function adds a new Todo to the list"""
        todos = []
        add_todo(todos, "Learn Python")
        self.assertEqual(len(todos), 1)
        self.assertIsInstance(todos[0], Todo)
        self.assertEqual(todos[0].title, "Learn Python")
        self.assertFalse(todos[0].completed)
    
    def test_complete_todo(self
