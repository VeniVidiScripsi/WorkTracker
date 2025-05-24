## 📦 Project Name

**WorkTrackr**
*A lightweight CLI system to track worker sign-ins, sign-outs, and calculate work hours using JSON.*

---

## 📄 `README.md`

```markdown
# WorkTrackr

**WorkTrackr** is a clean, modular, and extensible command-line system that allows employees or freelancers to track their working hours by signing in and out. It uses JSON as a lightweight data store and is designed with full compliance to the **SOLID principles**.

---

## 🚀 Features

- ✅ Sign in/out with timestamp
- 🕒 Calculate work hours for any specific day
- 📅 Default today’s report with a single click
- 💾 Local JSON file persistence
- 🧩 Modular design using SOLID principles
- 📦 Minimal dependencies – just Python standard library

---

## ▶️ Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone https://github.com/VeniVidiScripsi/WorkTracker.git/worktrackr.git
cd worktrackr
````

(Optional: Create and activate a virtual environment.)

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Run the app

```bash
python main.py
```

---

## 💡 Example Use Case

1. Launch the app.
2. Choose **Sign In** when you start work.
3. Choose **Sign Out** when you're done.
4. Use **Calculate Work Hours** to check your time.

---

## 🛠 Architecture Overview

* **`WorkerDataStore`**: Handles reading and writing JSON data.
* **`WorkerCardManager`**: Core business logic (sign in/out, calculating hours).
* **`Menu`**: CLI handler and action dispatcher.
* **`main.py`**: Application entry point and orchestrator.

---

## 📌 Future Ideas

* Export reports to CSV
* Weekly and monthly summaries
* Password-protected login system
* GUI interface using `tkinter` or `PyQt`

---

## 📝 License

MIT License – use freely for personal or professional use.

---

## 🤝 Contributing

Pull requests and improvements are welcome!
For major changes, please open an issue first to discuss what you would like to change.

---

