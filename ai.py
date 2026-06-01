from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)


def ask_ai(system, user):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user[:4000]}
        ]
    )
    return response.choices[0].message.content


# 🚀 STARTUP IDEA GENERATOR
def generate_startup_idea(topic):
    return ask_ai("""
Ты startup founder и product strategist.

Придумай:
1. Идею стартапа
2. Проблему
3. ЦА
4. Монетизацию
5. Почему это сработает
""", topic)


# 📊 MARKET ANALYSIS
def market_analysis(idea):
    return ask_ai("""
Сделай market analysis:
- рынок
- конкуренты
- риски
- тренды
- потенциал
""", idea)


# 💼 BUSINESS PLAN
def business_plan(idea):
    return ask_ai("""
Создай бизнес план:
- MVP
- roadmap
- маркетинг
- монетизация
- рост
""", idea)


# 🎤 PITCH
def generate_pitch(idea):
    return ask_ai("""
Создай pitch:
- проблема
- решение
- рынок
- продукт
- почему сейчас
""", idea)


# 🏷 BRANDING
def generate_branding(idea):
    return ask_ai("""
Создай бренд:
- название
- slogan
- стиль
- домены
""", idea)


# 📈 STARTUP SCORE
def startup_score(idea):
    return ask_ai("""
Оцени стартап (0-10):
- успех
- риски
- масштабируемость
- инвестиционный потенциал
""", idea)


# 💰 INVESTOR ANALYSIS
def investor_analysis(idea):
    return ask_ai("""
Ты инвестор.

Оцени:
- инвестировать или нет
- риски
- сильные стороны
- слабые стороны
- шанс успеха
""", idea)


# 📈 REVENUE FORECAST
def revenue_forecast(idea):
    return ask_ai("""
Сделай прогноз дохода:
- 6 месяцев
- 1 год
- 3 года
- ROI
- масштабирование
""", idea)


# 🧠 COMPETITOR ANALYSIS
def competitor_analysis(idea):
    return ask_ai("""
Анализ конкурентов:
- кто они
- слабости
- как победить
- стратегия
""", idea)


# 🎯 MVP GENERATOR
def mvp_generator(idea):
    return ask_ai("""
Создай MVP:
- ключевые функции
- второстепенные
- roadmap
- что делать первым
""", idea)


# 🤖 SAAS IDEAS
def saas_ideas(topic):
    return ask_ai("""
Сгенерируй:
- SaaS идеи
- AI продукты
- micro SaaS
- прибыльные ниши
""", topic)


# 💵 PRICING STRATEGY
def pricing_strategy(idea):
    return ask_ai("""
Создай pricing:
- free plan
- premium
- enterprise
- стратегия монетизации
""", idea)


# 🦄 UNICORN SCORE
def unicorn_score(idea):
    return ask_ai("""
Оцени unicorn potential:
- шанс стать unicorn
- TAM
- рост
- итог 0-100
""", idea)


# 🧠 FOUNDER ANALYSIS
def founder_analysis(founder_info):
    return ask_ai("""
Проанализируй founder:
- сильные стороны
- слабости
- навыки
- кого нанять
""", founder_info)


# 🤝 AI COFOUNDER
def ai_cofounder(idea):
    return ask_ai("""
Ты AI cofounder:
- улучшить идею
- рост
- ошибки
- стратегия
""", idea)


# 🌍 GLOBAL EXPANSION
def global_expansion(idea):
    return ask_ai("""
Глобальная стратегия:
- страны
- рынки
- локализация
- риски
""", idea)


# 📱 APP FEATURES
def app_features(idea):
    return ask_ai("""
Список функций:
- core features
- premium
- AI features
- viral mechanics
""", idea)


# ⚡ GROWTH HACKING
def growth_hacking(idea):
    return ask_ai("""
Growth hacking:
- первые пользователи
- вирусность
- маркетинг
- удержание
""", idea)


# 🧪 STARTUP VALIDATOR
def validate_startup(idea):
    return ask_ai("""
Проверь идею:
- есть ли проблема
- рынок
- конкуренция
- монетизация
- score 0-100
""", idea)


# 👤 CUSTOMER PERSONA
def customer_persona(idea):
    return ask_ai("""
Создай клиента:
- возраст
- работа
- боли
- цели
- мотивация
""", idea)


# 🌐 LANDING PAGE
def landing_page_generator(idea):
    return ask_ai("""
Создай лендинг:
- headline
- subtitle
- benefits
- features
- CTA
""", idea)


# ❓ INVESTOR QUESTIONS
def investor_questions(idea):
    return ask_ai("""
20 вопросов инвестора:
+ слабые места проекта
+ что улучшить
""", idea)


# 🚀 LAUNCH CHECKLIST
def launch_checklist(idea):
    return ask_ai("""
Checklist запуска:
- idea validation
- MVP
- beta
- marketing
- scale
""", idea)