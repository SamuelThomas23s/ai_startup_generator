from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


# =========================
# CORE
# =========================

def ask_ai(system, user):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user[:4000]}
        ]
    )

    return response.choices[0].message.content


# =========================
# STARTUP IDEA GENERATOR
# =========================

def generate_startup_idea(topic):
    return ask_ai("""
Создай стартап:
- идея
- проблема
- решение
- аудитория
- монетизация
""", topic)


def market_analysis(idea):
    return ask_ai("""
Сделай анализ рынка:
- рынок
- конкуренты
- тренды
- риски
""", idea)


def business_plan(idea):
    return ask_ai("""
Создай бизнес план:
- MVP
- roadmap
- маркетинг
- монетизация
""", idea)


def generate_pitch(idea):
    return ask_ai("""
Создай pitch deck:
- проблема
- решение
- рынок
- продукт
- стратегия
""", idea)


def generate_branding(idea):
    return ask_ai("""
Создай бренд:
- название
- slogan
- стиль
- домены
""", idea)


def startup_score(idea):
    return ask_ai("""
Оцени стартап:
- шанс успеха
- риски
- масштабируемость
""", idea)


# =========================
# INVESTOR TOOLS
# =========================

def investor_analysis(idea):
    return ask_ai("""
Ты венчурный инвестор.

Оцени:
- стоит ли инвестировать
- риски
- сильные стороны
""", idea)


def revenue_forecast(idea):
    return ask_ai("""
Сделай прогноз:
- 6 месяцев
- 1 год
- 3 года
""", idea)


def competitor_analysis(idea):
    return ask_ai("""
Анализ конкурентов:
- конкуренты
- слабые стороны
- возможности
""", idea)


# =========================
# MVP
# =========================

def mvp_generator(idea):
    return ask_ai("""
Создай MVP:
- функции
- roadmap
- приоритеты
""", idea)


# =========================
# SAAS
# =========================

def saas_ideas(topic):
    return ask_ai("""
Создай SaaS идеи:
- AI SaaS
- Micro SaaS
- B2B SaaS
""", topic)


def pricing_strategy(idea):
    return ask_ai("""
Создай pricing:
- free
- pro
- enterprise
""", idea)


def unicorn_score(idea):
    return ask_ai("""
Оцени unicorn potential:
- TAM
- рост
- итог 0-100
""", idea)


# =========================
# FOUNDER
# =========================

def founder_analysis(founder):
    return ask_ai("""
Проанализируй founder:
- сильные стороны
- слабости
- навыки
""", founder)


def ai_cofounder(idea):
    return ask_ai("""
Ты AI Cofounder.

Помоги:
- улучшить идею
- рост
- стратегия
""", idea)


# =========================
# GROWTH
# =========================

def global_expansion(idea):
    return ask_ai("""
Создай стратегию глобального роста.
""", idea)


def app_features(idea):
    return ask_ai("""
Создай функции продукта.
""", idea)


def growth_hacking(idea):
    return ask_ai("""
Создай growth strategy.
""", idea)


# =========================
# VALIDATION
# =========================

def validate_startup(idea):
    return ask_ai("""
Проверь идею:
- проблема
- рынок
- конкуренция
- score
""", idea)


def customer_persona(idea):
    return ask_ai("""
Создай customer persona.
""", idea)


def landing_page_generator(idea):
    return ask_ai("""
Создай лендинг.
""", idea)


def investor_questions(idea):
    return ask_ai("""
Создай вопросы инвестора.
""", idea)


def launch_checklist(idea):
    return ask_ai("""
Создай launch checklist.
""", idea)


# =========================
# BUSINESS MODEL
# =========================

def business_model_canvas(idea):
    return ask_ai("""
Создай Business Model Canvas.
""", idea)


def financial_model(idea):
    return ask_ai("""
Создай финансовую модель.
""", idea)


def tech_stack_generator(idea):
    return ask_ai("""
Подбери Tech Stack.
""", idea)


def generate_prd(idea):
    return ask_ai("""
Создай Product Requirements Document.
""", idea)


def development_roadmap(idea):
    return ask_ai("""
Создай roadmap на 12 месяцев.
""", idea)


def customer_acquisition_plan(idea):
    return ask_ai("""
Создай план привлечения клиентов.
""", idea)


def startup_advisor(question):
    return ask_ai("""
Ты startup advisor.
""", question)


def swot_analysis(idea):
    return ask_ai("""
Сделай SWOT анализ.
""", idea)


def market_entry_strategy(idea):
    return ask_ai("""
Создай market entry strategy.
""", idea)


def startup_launch_plan(idea):
    return ask_ai("""
Создай startup launch plan.
""", idea)


# =========================
# V6 UPDATE
# =========================

def niche_finder(topic):
    return ask_ai("""
Найди перспективные ниши.
""", topic)


def startup_name_generator(idea):
    return ask_ai("""
Создай 30 названий стартапа.
""", idea)


def competitive_advantage(idea):
    return ask_ai("""
Создай конкурентное преимущество.
""", idea)


def startup_kpi(idea):
    return ask_ai("""
Создай KPI систему.
""", idea)


def fundraising_strategy(idea):
    return ask_ai("""
Создай стратегию привлечения инвестиций.
""", idea)


def ai_product_manager(idea):
    return ask_ai("""
Ты Product Manager.
""", idea)


def unit_economics(idea):
    return ask_ai("""
Создай Unit Economics.
""", idea)


def international_expansion(idea):
    return ask_ai("""
Создай международную стратегию.
""", idea)


def exit_strategy(idea):
    return ask_ai("""
Создай Exit Strategy.
""", idea)


def ai_ceo(idea):
    return ask_ai("""
Ты CEO стартапа.
""", idea)