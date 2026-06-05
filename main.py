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
    saas_ideas,
    pricing_strategy,
    unicorn_score,
    founder_analysis,
    ai_cofounder,
    global_expansion,
    app_features,
    growth_hacking,
    validate_startup,
    customer_persona,
    landing_page_generator,
    investor_questions,
    launch_checklist,
    business_model_canvas,
    financial_model,
    tech_stack_generator,
    generate_prd,
    development_roadmap,
    customer_acquisition_plan,
    startup_advisor,
    swot_analysis,
    market_entry_strategy,
    startup_launch_plan,
    niche_finder,
    startup_name_generator,
    competitive_advantage,
    startup_kpi,
    fundraising_strategy,
    ai_product_manager,
    unit_economics,
    international_expansion,
    exit_strategy,
    ai_ceo
)

from history import save_history


def save_result(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)


def print_menu():
    print("""
==================================================
           AI STARTUP STUDIO V6
==================================================

 1  - Generate Startup Idea
 2  - Market Analysis
 3  - Business Plan
 4  - Pitch Generator
 5  - Branding Generator
 6  - Startup Score

 7  - Investor Analysis
 8  - Revenue Forecast
 9  - Competitor Analysis
10  - MVP Generator

11  - SaaS Ideas
12  - Pricing Strategy
13  - Unicorn Potential
14  - Founder Analysis

15  - AI Cofounder
16  - Global Expansion
17  - App Features
18  - Growth Hacking

19  - Startup Validator
20  - Customer Persona
21  - Landing Page Generator
22  - Investor Questions
23  - Launch Checklist

24  - Business Model Canvas
25  - Financial Model
26  - Tech Stack Generator
27  - Generate PRD
28  - Development Roadmap
29  - Customer Acquisition Plan
30  - Startup Advisor
31  - SWOT Analysis
32  - Market Entry Strategy
33  - Startup Launch Plan

34  - Niche Finder
35  - Startup Name Generator
36  - Competitive Advantage
37  - KPI Generator
38  - Fundraising Strategy
39  - AI Product Manager
40  - Unit Economics
41  - International Expansion
42  - Exit Strategy
43  - AI CEO

 0  - Exit

==================================================
""")


def execute_choice(choice, topic):

    if choice == "1":
        return generate_startup_idea(topic)

    elif choice == "2":
        return market_analysis(topic)

    elif choice == "3":
        return business_plan(topic)

    elif choice == "4":
        return generate_pitch(topic)

    elif choice == "5":
        return generate_branding(topic)

    elif choice == "6":
        return startup_score(topic)

    elif choice == "7":
        return investor_analysis(topic)

    elif choice == "8":
        return revenue_forecast(topic)

    elif choice == "9":
        return competitor_analysis(topic)

    elif choice == "10":
        return mvp_generator(topic)

    elif choice == "11":
        return saas_ideas(topic)

    elif choice == "12":
        return pricing_strategy(topic)

    elif choice == "13":
        return unicorn_score(topic)

    elif choice == "14":
        return founder_analysis(topic)

    elif choice == "15":
        return ai_cofounder(topic)

    elif choice == "16":
        return global_expansion(topic)

    elif choice == "17":
        return app_features(topic)

    elif choice == "18":
        return growth_hacking(topic)

    elif choice == "19":
        return validate_startup(topic)

    elif choice == "20":
        return customer_persona(topic)

    elif choice == "21":
        return landing_page_generator(topic)

    elif choice == "22":
        return investor_questions(topic)

    elif choice == "23":
        return launch_checklist(topic)

    elif choice == "24":
        return business_model_canvas(topic)

    elif choice == "25":
        return financial_model(topic)

    elif choice == "26":
        return tech_stack_generator(topic)

    elif choice == "27":
        return generate_prd(topic)

    elif choice == "28":
        return development_roadmap(topic)

    elif choice == "29":
        return customer_acquisition_plan(topic)

    elif choice == "30":
        return startup_advisor(topic)

    elif choice == "31":
        return swot_analysis(topic)

    elif choice == "32":
        return market_entry_strategy(topic)

    elif choice == "33":
        return startup_launch_plan(topic)

    elif choice == "34":
        return niche_finder(topic)

    elif choice == "35":
        return startup_name_generator(topic)

    elif choice == "36":
        return competitive_advantage(topic)

    elif choice == "37":
        return startup_kpi(topic)

    elif choice == "38":
        return fundraising_strategy(topic)

    elif choice == "39":
        return ai_product_manager(topic)

    elif choice == "40":
        return unit_economics(topic)

    elif choice == "41":
        return international_expansion(topic)

    elif choice == "42":
        return exit_strategy(topic)

    elif choice == "43":
        return ai_ceo(topic)

    return "Unknown option."


def main():

    print("🚀 AI STARTUP STUDIO V6")

    while True:

        print_menu()

        choice = input("Select option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        topic = input("\nEnter startup idea/topic/question:\n\n")

        result = execute_choice(choice, topic)

        print("\n")
        print("=" * 60)
        print("RESULT")
        print("=" * 60)
        print(result)
        print("=" * 60)

        save_result(result)

        save_history(
            f"Mode {choice}",
            result
        )

        print("\n✅ Result saved")
        print("✅ History updated\n")


if __name__ == "__main__":
    main()