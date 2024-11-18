from classes.class_calc_LAB2 import Calculator
from BLL.calculator_LAB2 import Calculator
from BLL.validator_LAB2 import is_valid_operator
from DAL.memory_LAB2 import store_in_memory, recall_memory, show_history
from runner import calculator

# Пам'ять для збереження результатів
memory = None

if __name__ == "__main__":
    calculator()
