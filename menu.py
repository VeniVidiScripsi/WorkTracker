from typing import Callable


class Menu:
    def __init__(self, system_name: str):
        self.system_name = system_name
        self.actions: dict[str, Callable[[], None]] = {}

    def add_action(self, description: str, action: Callable[[], None]) -> None:
        self.actions[description] = action

    def display_and_get_choice(self) -> Callable[[], None]:
        print(f"Welcome to the {self.system_name}!")
        descriptions = list(self.actions.keys())
        for idx, desc in enumerate(descriptions, 1):
            print(f"{idx}. {desc}")
        try:
            choice = int(input("Choose an option: "))
            return self.actions.get(descriptions[choice - 1], self.invalid_choice)
        except (ValueError, IndexError):
            return self.invalid_choice

    def invalid_choice(self) -> None:
        print("Invalid choice.")
