import time

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_title():
    print(YELLOW + "-------------------------" + RESET)
    print(YELLOW + "|    Hacking: Database    |" + RESET)
    print(YELLOW + "-------------------------" + RESET)

def print_introduction():
    print(GREEN + "\nWelcome to the hacking simulation.\nYou are about to hack into the database to retrieve my social links.\nPress Enter to start hacking..." + RESET)
    input()

def progress_bar():
    for i in range(101):
        print(f"\rHacking progress: [{'#' * (i // 2)}{' ' * (50 - i // 2)}] {i}%", end='')
        time.sleep(0.1)
    print()

def hack_database():
    print(CYAN + "\nInitializing hacking tools and starting the hacking process...\n" + RESET)
    progress_bar()
    print(CYAN + "Database hack successful!" + RESET)

def reveal_links():
    print(GREEN + "\nTop secret developer social links:\n" + RESET)
    time.sleep(1)
    links = [
        ("GitHub", "https://github.com/ThePrimeDeveloper"),
        ("Discord", "@alpha.rex"),
        ("Telegram", "@not3ditz"),
        ("Email", "primedeveloper@icloud.com")
    ]
    for label, url in links:
        print(f" - {label}: {url}")
        time.sleep(0.5)
    print(YELLOW + "\nThank you for visiting my profile! Looking forward to connecting with you." + RESET)

if __name__ == "__main__":
    print_title()
    print_introduction()
    hack_database()
    reveal_links()
