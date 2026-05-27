from datetime import datetime

def save_history(title, content):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 50 + "\n")
        f.write(str(datetime.now()) + "\n")
        f.write(title + "\n\n")
        f.write(content)
        f.write("\n")