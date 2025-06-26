import os

from menu.menu import Menu


def main() -> None:
    while True:
        os.system('cls || clear')
        print('Wellcome to the Worker Card System!')
        Menu.display_menu()
        action = Menu.get_user_choice()
        action()
        if input('Continue? (y/n): ').lower().strip() != 'y':
            break


if __name__ == '__main__':
    main()
