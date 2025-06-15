import os
import json
from pathlib import Path   
from datetime import datetime, timedelta

class WorkerCardSystem:
    def __init__(self, data_file='worker_data.json'):
        self.data_file = Path(data_file)
        self.load_data()

    def init_data_file(self):
        if not self.data_file.exists():
            self.data_file.write_text('{}')

    def load_data(self):
        try:
            self.data = json.loads(self.data_file.read_text())
        except FileNotFoundError:
            self.init_data_file()
            self.data = {}

    def save_data(self):
        self.data_file.write_text(json.dumps(self.data, indent=4))

    def sign_in(self):
        today = datetime.now().strftime('%Y-%m-%d')
        if today not in self.data:
            self.data[today] = {'sign_in': [], 'sign_out': []}

        self.data[today]['sign_in'].append(datetime.now().isoformat())
        self.save_data()
        print(f"Signed in at {datetime.now().strftime('%H:%M:%S')}.")

    def sign_out(self):
        today = datetime.now().strftime('%Y-%m-%d')
        if today not in self.data or not self.data[today]['sign_in']:
            print("You have not signed in today.")
            return

        self.data[today]['sign_out'].append(datetime.now().isoformat())
        self.save_data()
        print(f"Signed out at {datetime.now().strftime('%H:%M:%S')}.")

    def calculate_work_hours(self) -> None:
        date = input("Enter the date (YYYY-MM-DD) to calculate work hours: ")
        self._calculate_work_hours(date)
        
    def _calculate_work_hours(self, date: str) -> None:
        if date not in self.data:
            print(f"No data for {date}.")
            return

        sign_in_times = self.data[date]['sign_in']
        sign_out_times = self.data[date]['sign_out']

        total_work = timedelta()
        for sign_in, sign_out in zip(sign_in_times, sign_out_times):
            in_time = datetime.fromisoformat(sign_in)
            out_time = datetime.fromisoformat(sign_out)
            total_work += (out_time - in_time)

        print(f"Total work hours on {date}: {total_work}")
    
    def calculate_work_hours_for_today(self) -> None:
        today = datetime.now().strftime('%Y-%m-%d')
        self.calculate_work_hours(today)
    
    def invalid_choice(self) -> None:
        print("Invalid choice. Please try again.")

    def exit(self) -> None:
        print("Exiting the system.")
        exit(0)
 

class Menu:
    def __init__(
        self, 
        system: WorkerCardSystem = WorkerCardSystem(), 
        system_name: str = "Worker Card System",
        description_to_action: dict[str, str] = None, 
    ) -> None:
        self.system = system
        self.system_name = system_name
        self.description_to_action = description_to_action 


    def add_action(self, description: str, action: str) -> None:
        if self.description_to_action is None:
            self.description_to_action = {}
        self.description_to_action[description] = action

    def run_action(self, description: str) -> None:
        if self.description_to_action and description in self.description_to_action:
            getattr(self.system, self.description_to_action[description])()
        else:
            print(f"No action found for '{description}'.")

    def menu(self) -> str:
        print(f"Welcome to the {self.system_name}!")
        choice_to_description = dict(enumerate(self.description_to_action.keys(), start=1))
        for index, description in choice_to_description.items():
            print(f"{index}- {description}")
        choice = input(f"Please choose an option (1-{len(self.description_to_action)}): ")
        return choice_to_description.get(int(choice), "invalid_choice")
        

        
    
def main() -> None:
    decryption_to_action = {
        "Sign In": "sign_in",
        "Sign Out": "sign_out",
        "Calculate Work Hours for Today": "calculate_work_hours_for_today",
        "Calculate Work Hours for a Specific Date": "calculate_work_hours",
        "Exit": "exit"
    }
    system = WorkerCardSystem()
    menu = Menu(description_to_action=decryption_to_action)
    while True:
        os.system('cls || clear')
        choice: str = menu.menu()
        menu.run_action(choice)
        if input("Do you want to continue? (y/n): ").lower().strip() != 'y':
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()