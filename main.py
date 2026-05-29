from ai import (
    generate_startup_idea,
    market_analysis,
    business_plan,
    generate_pitch,
    generate_branding,
    startup_score,
    investor_analysis,
    revenue_forecast,
    competitor_analysis,
    mvp_generator,
    ai_cofounder,
    global_expansion,
    app_features,
    growth_hacking,
    saas_ideas,
    pricing_strategy,
    unicorn_score,
    founder_analysis
)

from history import save_history


def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


def menu():
    print("""
========== AI STARTUP GENERATOR V3 ==========

1  - Generate Startup Idea
2  - Market Analysis
3  - Business Plan
4  - Pitch Generator
5  - Branding Generator
6  - Startup Score
7  - Investor Analysis
8  - Revenue Forecast
9  - Competitor Analysis
10 - MVP Generator
11 - SaaS Ideas Generator
12 - Pricing Strategy
13 - Unicorn Potential
14 - Founder Analysis
15 - AI Cofounder
16 - Global Expansion Strategy
17 - App Features Generator
18 - Growth Hacking Strategy

0  - Exit

=============================================
""")


def main():
    print("🚀 AI STARTUP GENERATOR V3")

    while True:
        menu()

        choice = input("Choice: ")

        if choice == "0":
            print("Goodbye!")
            break

        topic = input("\nEnter startup idea/topic:\n")

        result = ""

        # 🚀 STARTUP IDEA
        if choice == "1":
            result = generate_startup_idea(topic)

        # 📊 MARKET ANALYSIS
        elif choice == "2":
            result = market_analysis(topic)

        # 💼 BUSINESS PLAN
        elif choice == "3":
            result = business_plan(topic)

        # 🎤 PITCH
        elif choice == "4":
            result = generate_pitch(topic)

        # 🏷 BRANDING
        elif choice == "5":
            result = generate_branding(topic)

        # 📈 SCORE
        elif choice == "6":
            result = startup_score(topic)

        # 💰 INVESTOR ANALYSIS
        elif choice == "7":
            result = investor_analysis(topic)

        # 📈 REVENUE FORECAST
        elif choice == "8":
            result = revenue_forecast(topic)

        # 🧠 COMPETITORS
        elif choice == "9":
            result = competitor_analysis(topic)

        # 🎯 MVP
        elif choice == "10":
            result = mvp_generator(topic)

        # 🤖 SAAS IDEAS
        elif choice == "11":
            result = saas_ideas(topic)

        # 💵 PRICING
        elif choice == "12":
            result = pricing_strategy(topic)

        # 🦄 UNICORN SCORE
        elif choice == "13":
            result = unicorn_score(topic)

        # 🧠 FOUNDER ANALYSIS
        elif choice == "14":
            result = founder_analysis(topic)

        # 🤝 AI COFOUNDER
        elif choice == "15":
            result = ai_cofounder(topic)

        # 🌍 GLOBAL EXPANSION
        elif choice == "16":
            result = global_expansion(topic)

        # 📱 APP FEATURES
        elif choice == "17":
            result = app_features(topic)

        # ⚡ GROWTH HACKING
        elif choice == "18":
            result = growth_hacking(topic)

        else:
            print("Invalid choice")
            continue

        print("\n========== RESULT ==========\n")
        print(result)

        save_result(result)

        save_history(
            f"Mode {choice}",
            result
        )

        print("\n✅ Result saved to result.txt")
        print("✅ History updated")


if __name__ == "__main__":
    main()