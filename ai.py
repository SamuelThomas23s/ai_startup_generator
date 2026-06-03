from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


# =========================
# CORE AI FUNCTION
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
# STARTUP CORE FEATURES
# =========================

def generate_startup_idea(topic):
    return ask_ai("""
Ты startup founder.
Создай:
- идею
- проблему
- аудиторию
- монетизацию
- ценность
""", topic)


def market_analysis(idea):
    return ask_ai("""
Сделай market analysis:
- рынок
- конкуренты
- тренды
- риски
- потенциал
""", idea)


def business_plan(idea):
    return ask_ai("""
Создай бизнес план:
- MVP
- roadmap
- маркетинг
- монетизация
- рост
""", idea)


def generate_pitch(idea):
    return ask_ai("""
Создай pitch:
- проблема
- решение
- рынок
- продукт
- почему сейчас
""", idea)


def generate_branding(idea):
    return ask_ai("""
Создай бренд:
- название
- slogan
- стиль
- домен идеи
""", idea)


def startup_score(idea):
    return ask_ai("""
Оцени стартап 0-10:
- успех
- масштаб
- риск
- инвестиции
""", idea)


# =========================
# INVESTMENT & ANALYSIS
# =========================

def investor_analysis(idea):
    return ask_ai("""
Ты инвестор.
Оцени:
- инвестировать или нет
- риски
- потенциал
- слабые стороны
""", idea)


def revenue_forecast(idea):
    return ask_ai("""
Прогноз дохода:
- 6 мес
- 1 год
- 3 года
- ROI
""", idea)


def competitor_analysis(idea):
    return ask_ai("""
Конкуренты:
- кто
- слабости
- как победить
""", idea)


def mvp_generator(idea):
    return ask_ai("""
Создай MVP:
- функции
- roadmap
- приоритеты
""", idea)


# =========================
# SaaS & PRODUCT STRATEGY
# =========================

def saas_ideas(topic):
    return ask_ai("""
Сгенерируй SaaS идеи:
- micro SaaS
- AI SaaS
- прибыльные ниши
""", topic)


def pricing_strategy(idea):
    return ask_ai("""
Pricing стратегия:
- free
- pro
- enterprise
- монетизация
""", idea)


def unicorn_score(idea):
    return ask_ai("""
Оцени unicorn шанс:
- рынок
- рост
- масштаб
- score 0-100
""", idea)


def founder_analysis(founder):
    return ask_ai("""
Проанализируй founder:
- сильные стороны
- слабости
- навыки
- кого нанять
""", founder)


# =========================
# AI COFOUNDER
# =========================

def ai_cofounder(idea):
    return ask_ai("""
Ты AI cofounder:
- улучшение идеи
- стратегия роста
- ошибки
- советы
""", idea)


def global_expansion(idea):
    return ask_ai("""
Глобальная стратегия:
- страны
- локализация
- рынки
- риски
""", idea)


def app_features(idea):
    return ask_ai("""
Функции продукта:
- core
- premium
- AI features
- viral features
""", idea)


def growth_hacking(idea):
    return ask_ai("""
Growth hacking:
- пользователи
- вирусность
- маркетинг
- удержание
""", idea)


# =========================
# STARTUP VALIDATION SYSTEM
# =========================

def validate_startup(idea):
    return ask_ai("""
Проверь стартап:
- проблема есть?
- рынок
- конкуренция
- монетизация
- score 0-100
""", idea)


def customer_persona(idea):
    return ask_ai("""
Создай customer persona:
- кто пользователь
- боли
- цели
- мотивация
""", idea)


def landing_page_generator(idea):
    return ask_ai("""
Создай лендинг:
- headline
- benefits
- features
- CTA
""", idea)


def investor_questions(idea):
    return ask_ai("""
20 вопросов инвестора:
+ слабые места
+ подготовка
""", idea)


def launch_checklist(idea):
    return ask_ai("""
Checklist запуска:
- validation
- MVP
- beta
- launch
- scaling
""", idea)


# =========================
# ADVANCED STARTUP ENGINE
# =========================

def business_model_canvas(idea):
    return ask_ai("""
Business Model Canvas:
- segments
- value
- channels
- revenue
- cost
- partners
""", idea)


def financial_model(idea):
    return ask_ai("""
Финансовая модель:
- расходы
- доходы
- прибыль
- break-even
""", idea)


def tech_stack_generator(idea):
    return ask_ai("""
Tech stack:
- frontend
- backend
- DB
- AI tools
- cloud
""", idea)


def generate_prd(idea):
    return ask_ai("""
PRD:
- vision
- features
- users
- MVP scope
""", idea)


def development_roadmap(idea):
    return ask_ai("""
Roadmap 12 месяцев:
- этапы разработки
- маркетинг
- рост
""", idea)


def customer_acquisition_plan(idea):
    return ask_ai("""
Customer acquisition:
- каналы
- CAC
- KPI
- стратегия
""", idea)


def startup_advisor(question):
    return ask_ai("""
Ты startup advisor.
Дай экспертный ответ.
""", question)


def swot_analysis(idea):
    return ask_ai("""
SWOT:
- strengths
- weaknesses
- opportunities
- threats
""", idea)


def market_entry_strategy(idea):
    return ask_ai("""
Market entry:
- стратегия входа
- позиционирование
- запуск
""", idea)


def startup_launch_plan(idea):
    return ask_ai("""
Launch plan:
- шаги запуска
- MVP
- первые клиенты
- масштабирование
""", idea)