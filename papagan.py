import datetime
import subprocess
import time


def speak(text: str) -> None:
    """Reads text aloud using eSpeak."""
    subprocess.run(["espeak", "-v", "tr", text], check=False)


def current_time_text() -> str:
    now = datetime.datetime.now()
    return f"Su an saat {now:%H:%M}"


def main() -> None:
    while True:
        speak(current_time_text())
        time.sleep(120)


if __name__ == "__main__":
    main()
