import os

def log_operation(expression):
    log_file = os.path.join(os.path.dirname(__file__), 'log.txt')
    with open(log_file, 'a') as file:
        file.write(expression + "\n")

def log_history(expression, result):
    history_file = os.path.join(os.path.dirname(__file__), 'history.txt')
    with open(history_file, 'a') as file:
        file.write(f"{expression} = {result}\n")

def show_history():
    history_file = os.path.join(os.path.dirname(__file__), 'history.txt')
    with open(history_file, 'r') as file:
        history = file.read()
    print(history)


