def handle_input(prompt, validator):
    """Handle user input with validation."""
    while True:
        try:
            value = input(prompt)
            if validator(value):
                return value
            print("Invalid input. Try again.")
        except Exception as e:
            print(f"Error: {e}")