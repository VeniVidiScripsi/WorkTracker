import os
from worker_data_store import WorkerDataStore
from worker_card_manager import WorkerCardManager
from menu import Menu


def main():
    store = WorkerDataStore()
    manager = WorkerCardManager(store)
    menu = Menu('Worker Card System')

    menu.add_action('Sign In', manager.sign_in)
    menu.add_action('Sign Out', manager.sign_out)
    menu.add_action(
        'Calculate Work Hours for Today',
        lambda: manager.calculate_work_hours(date_input('today')),
    )
    menu.add_action(
        'Calculate Work Hours for Specific Date',
        lambda: manager.calculate_work_hours(date_input()),
    )
    menu.add_action('Exit', exit_system)

    while True:
        os.system('cls || clear')
        action = menu.display_and_get_choice()
        action()
        if input('Continue? (y/n): ').lower().strip() != 'y':
            break


def date_input(default_today: str = '') -> str:
    return (
        datetime.now().strftime('%Y-%m-%d')
        if default_today == 'today'
        else input('Enter date (YYYY-MM-DD): ').strip()
    )


def exit_system() -> None:
    print('Exiting system.')
    raise SystemExit()


if __name__ == '__main__':
    from datetime import datetime  # Imported here to avoid circular imports

    main()
