def get_user_input(prompt, valid_options=None):
    """Отримання введення користувача з валідацією"""
    while True:
        user_input = input(prompt)
        if valid_options and user_input not in valid_options:
            print(f"Невірний вибір. Доступні варіанти: {', '.join(valid_options)}")
        else:
            return user_input



