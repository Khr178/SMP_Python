import logging
import logging.config
import json
from functools import wraps

class InputValidator:
    """Клас для перевірки вхідних даних"""

    @staticmethod
    def validate_number_input(prompt, min_value=None, max_value=None):
        """Перевірте числове введення в необов’язковому діапазоні"""
        while True:
            try:
                value = int(input(prompt))
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}")
                    continue
                if max_value is not None and value > max_value:
                    print(f"Value must be at most {max_value}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number")

    @staticmethod
    def validate_string_input(prompt, min_length=None, max_length=None):
        """Перевірте введений рядок із необов’язковими обмеженнями довжини"""
        while True:
            value = input(prompt).strip()
            if min_length is not None and len(value) < min_length:
                print(f"Input must be at least {min_length} characters long")
                continue
            if max_length is not None and len(value) > max_length:
                print(f"Input must be at most {max_length} characters long")
                continue
            return value