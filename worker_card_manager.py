from datetime import datetime, timedelta
from worker_data_store import WorkerDataStore


class WorkerCardManager:
    def __init__(self, store: WorkerDataStore):
        self.store = store
        self.data = self.store.load()

    def sign_in(self) -> None:
        now = datetime.now()
        today = now.strftime('%Y-%m-%d')
        self.data.setdefault(today, {'sign_in': [], 'sign_out': []})
        self.data[today]['sign_in'].append(now.isoformat())
        self.store.save(self.data)
        print(f"Signed in at {now.strftime('%H:%M:%S')}.")

    def sign_out(self) -> None:
        now = datetime.now()
        today = now.strftime('%Y-%m-%d')
        if today not in self.data or not self.data[today]['sign_in']:
            print("You have not signed in today.")
            return
        self.data[today]['sign_out'].append(now.isoformat())
        self.store.save(self.data)
        print(f"Signed out at {now.strftime('%H:%M:%S')}.")

    def calculate_work_hours(self, date: str) -> None:
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
