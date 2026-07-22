from datetime import datetime

LOG_FILE = "history.txt"


def log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        f.write(f"[{time}] {text}\n")
