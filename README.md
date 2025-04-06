# 📁 Folder Synchronizer

A modular Python utility that continuously synchronizes a **replica** folder to match a **source** folder.

---

## 🚀 Features

- ✅ One-way sync: `source → replica`
- 🕒 Periodic synchronization at custom intervals
- 🔍 Uses MD5 hashing to detect file changes
- 🧹 Deletes files/folders not present in the source
- 📜 Logs all operations to both console and log file
- ✅ Clean modular structure (`controllers`, `utils`)
- 🧪 Unit tests with `unittest`

---

## 🧱 Project Structure

```
folder_synchronizer/
├── controllers/
│   └── sync_controller.py      # Main sync logic
├── utils/
│   ├── hashing.py              # Hashing helper (MD5)
│   └── logger.py               # Logging setup
├── main.py                     # CLI entry point
├── test_sync.py                # Unit tests
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠 Requirements

- Python 3.6+
- No third-party libraries required

---

## ⚙️ Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/folder-synchronizer.git
cd folder-synchronizer
```

### 2. Run the synchronizer

```bash
python main.py <source_path> <replica_path> <interval_in_seconds> <log_file_path>
```

### Example:

```bash
python main.py "./example/source" "./example/replica" 60 "sync.log"
```

- Synchronizes every 60 seconds
- Keeps `replica` identical to `source`
- Logs to `sync.log` and console

---

## 🧪 Running Unit Tests

The tests cover syncing logic including:
- Copying new files
- Updating modified files
- Deleting missing files

### Run tests with `unittest` or `pytest`:

```bash
# Run with unittest
python -m unittest test_sync.py

# Or use pytest (optional)
pytest test_sync.py
```

Make sure the `controllers` and `utils` folders have `__init__.py` files so they are treated as packages (optional but recommended for imports):

```bash
touch controllers/__init__.py
touch utils/__init__.py
```

---

## 📝 License

This project is open-source under the MIT License.
