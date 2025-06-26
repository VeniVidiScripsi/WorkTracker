from typing import Callable


class Menu:
    ACTIONS: dict[str, Callable[[], None]] = {}

    @classmethod
    def display_menu(cls) -> None:
        for idx, desc in enumerate(cls.ACTIONS.keys(), 1):
            print(f'{idx}. {desc}')

    @classmethod
    def get_user_choice(cls) -> Callable[[], None]:
        descriptions = list(cls.ACTIONS.keys())
        try:
            choice = int(input('Choose an option: '))
            return cls.ACTIONS.get(descriptions[choice - 1], cls.invalid_choice)
        except (ValueError, IndexError):
            return cls.invalid_choice

    @staticmethod
    def invalid_choice() -> None:
        print('Invalid choice.')


def menu_action(description: str) -> Callable[[Callable[[], None]], Callable[[], None]]:
    """
    A decorator to register a function as a menu action.
    """

    def decorator(func: Callable[[], None]) -> Callable[[], None]:
        Menu.ACTIONS[description] = func
        return func

    return decorator
