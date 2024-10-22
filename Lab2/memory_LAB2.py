memory = None
history = []

def store_in_memory(result):
    global memory
    memory = result
    print(f"Результат {result} збережений у пам'яті.")

def recall_memory():
    if memory is not None:
        print(f"Збережене значення: {memory}")
        return memory
    else:
        print("Пам'ять порожня.")
        return None

def log_operation(operation):
    # Збереження операції в історії
    history.append(operation)

def log_history(expression, result):
    history.append(f"{expression} = {result}")

def show_history():
    if history:
        print("Історія розрахунків:")
        for entry in history:
            print(entry)
    else:
        print("Історія порожня.")

