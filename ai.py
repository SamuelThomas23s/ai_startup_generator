from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


def ask_ai(system, user):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": user
            }
        ]
    )

    return response.choices[0].message.content


# 🚀 STARTUP IDEA
def generate_startup_idea(topic):
    return ask_ai("""
Ты startup founder.

Придумай:
- идею стартапа
- проблему
- решение
- целевую аудиторию
- монетизацию
""", topic)


# 📊 MARKET ANALYSIS
def market_analysis(idea):
    return ask_ai("""
Сделай market analysis:

- аудитория
- конкуренты
- риски
- потенциал
""", idea)


# 💼 BUSINESS PLAN
def business_plan(idea):
    return ask_ai("""
Создай бизнес план:

- MVP
- roadmap
- маркетинг
- доход
- стратегия роста
""", idea)


# 🎤 PITCH DECK
def generate_pitch(idea):
    return ask_ai("""
Создай startup pitch:

- проблема
- решение
- рынок
- монетизация
- why now
""", idea)


# 🏷 BRANDING
def generate_branding(idea):
    return ask_ai("""
Создай:
- название стартапа
- slogan
- brand style
- идеи доменов
""", idea)


# 📈 SUCCESS SCORE
def startup_score(idea):
    return ask_ai("""
Оцени startup idea:

- шанс успеха
- риски
- scalability
- инвестиционный потенциал
""", idea)