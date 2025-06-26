from datetime import datetime

from managers.worker_data_store import WorkerDataStore
from managers.worker_card_manager import WorkerCardManager
from menu.menu import menu_action


store = WorkerDataStore()
manager = WorkerCardManager(store)


@menu_action('Sign In')
def sign_in() -> None:
    manager.sign_in()


@menu_action('Sign Out')
def sign_out() -> None:
    manager.sign_out()


@menu_action('Calculate Work Hours for Today')
def calculate_work_hours_today() -> None:
    return manager.calculate_work_hours(date_input('today'))


@menu_action('Calculate Work Hours for Specific Date')
def calculate_work_hours_specific_date() -> None:
    return manager.calculate_work_hours(date_input())


@menu_action('Exit')
def exit_system() -> None:
    print('Exiting system.')
    raise SystemExit()


def date_input(default_today: str = '') -> str:
    return (
        datetime.now().strftime('%Y-%m-%d')
        if default_today == 'today'
        else input('Enter date (YYYY-MM-DD): ').strip()
    )
