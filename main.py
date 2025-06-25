from dotenv import load_dotenv

from chord_editor import run_gui

load_dotenv()

def main() -> None:
    run_gui()

if __name__ == "__main__":
    main()