import logging
import logging.config
import json
from functools import wraps


class Logger:
    """Клас для обробки операцій логування"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            try:
                with open('config/logging_config.json', 'r', encoding='utf-8') as config_file:
                    config = json.load(config_file)
                    logging.config.dictConfig(config)
            except FileNotFoundError:
                logging.basicConfig(level=logging.INFO)
            cls._instance.logger = logging.getLogger(__name__)
        return cls._instance

    def log_function_call(self, func):
        """Декоратор для логування викликів функцій"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(f"Starting: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                self.logger.info(f"Completed: {func.__name__}")
                return result
            except Exception as e:
                self.logger.error(f"Error in {func.__name__}: {str(e)}")
                raise

        return wrapper