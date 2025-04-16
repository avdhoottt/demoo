# Python Todo List Project
# Complete the tasks according to the requirements

class Todo:
    def __init__(self, title):
        # TODO: Initialize the Todo object with title and completed properties
        pass

def add_todo(todo_list, title):
    # TODO: Create a new Todo and add it to the todo_list
    pass

def complete_todo(todo_list, index):
    # TODO: Mark the todo at the specified index as completed
    pass

# Example usage
if __name__ == "__main__":
    todos = []
    add_todo(todos, "Learn Python")
    add_todo(todos, "Build a todo app")
    complete_todo(todos, 0)
    
    # Print all todos
    for i, todo in enumerate(todos):
        status = "✓" if todo.completed else " "
        print(f"[{status}] {i+1}. {todo.title}")
