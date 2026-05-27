from ai import (
    generate_startup_idea,
    market_analysis,
    business_plan,
    generate_pitch,
    generate_branding,
    startup_score
)

from history import save_history


def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


def menu():
    print("""
========== AI STARTUP GENERATOR ==========

1 - Generate Startup Idea
2 - Market Analysis
3 - Business Plan
4 - Pitch Generator
5 - Branding Generator
6 - Startup Score

0 - Exit
==========================================
""")


def main():
    print("🚀 AI STARTUP GENERATOR")

    while True:
        menu()

        choice = input("Choice: ")

        if choice == "0":
            break

        topic = input("Введите тему или нишу:\n")

        result = ""

        if choice == "1":
            result = generate_startup_idea(topic)

        elif choice == "2":
            result = market_analysis(topic)

        elif choice == "3":
            result = business_plan(topic)

        elif choice == "4":
            result = generate_pitch(topic)

        elif choice == "5":
            result = generate_branding(topic)

        elif choice == "6":
            result = startup_score(topic)

        else:
            print("Invalid")
            continue

        print("\n========== RESULT ==========\n")
        print(result)

        save_result(result)
        save_history(f"Mode {choice}", result)

        print("\n✅ Saved")


if __name__ == "__main__":
    main()