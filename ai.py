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
                "content": user[:4000]
            }
        ]
    )

    return response.choices[0].message.content


# 🚀 STARTUP IDEA GENERATOR
def generate_startup_idea(topic):
    return ask_ai("""
Ты startup founder и product strategist.

Придумай:
1. Идею стартапа
2. Какую проблему решает
3. Целевую аудиторию
4. Способ монетизации
5. Почему идея перспективна
""", topic)


# 📊 MARKET ANALYSIS
def market_analysis(idea):
    return ask_ai("""
Сделай анализ рынка:

1. Размер рынка
2. Целевая аудитория
3. Конкуренты
4. Тренды
5. Риски
6. Потенциал роста
""", idea)


# 💼 BUSINESS PLAN
def business_plan(idea):
    return ask_ai("""
Создай бизнес-план:

1. MVP
2. Roadmap
3. Маркетинг
4. Growth strategy
5. Монетизация
6. Масштабирование
""", idea)


# 🎤 PITCH GENERATOR
def generate_pitch(idea):
    return ask_ai("""
Создай pitch deck текст:

1. Проблема
2. Решение
3. Рынок
4. Продукт
5. Бизнес модель
6. Почему сейчас
7. Потенциал
""", idea)


# 🏷 BRANDING
def generate_branding(idea):
    return ask_ai("""
Создай branding:

1. Название стартапа
2. Slogan
3. Brand style
4. Идеи доменов
5. Цвета бренда
""", idea)


# 📈 STARTUP SCORE
def startup_score(idea):
    return ask_ai("""
Оцени startup idea:

1. Шанс успеха
2. Инвестиционный потенциал
3. Масштабируемость
4. Риски
5. Итоговый score 0-10
""", idea)


# 💰 INVESTOR MODE
def investor_analysis(idea):
    return ask_ai("""
Ты венчурный инвестор.

Оцени стартап:

1. Стоит ли инвестировать
2. Риски
3. Сильные стороны
4. Слабые стороны
5. Потенциал роста
6. Вероятность успеха
""", idea)


# 📈 REVENUE FORECAST
def revenue_forecast(idea):
    return ask_ai("""
Сделай финансовый прогноз:

1. Доход через 6 месяцев
2. Доход через 1 год
3. Доход через 3 года
4. Потенциальная прибыль
5. Масштабируемость
6. ROI
""", idea)


# 🧠 COMPETITOR ANALYSIS
def competitor_analysis(idea):
    return ask_ai("""
Найди конкурентов стартапа.

Для каждого:
1. Сильные стороны
2. Слабые стороны
3. Как можно обойти
4. Чем выделиться
5. Как победить на рынке
""", idea)


# 🎯 MVP GENERATOR
def mvp_generator(idea):
    return ask_ai("""
Создай MVP стартапа:

1. Основные функции
2. Secondary features
3. Что делать первым
4. План разработки
5. Что можно отложить
6. Tech stack ideas
""", idea)


# 🧠 AI COFOUNDER MODE
def ai_cofounder(idea):
    return ask_ai("""
Ты AI cofounder стартапа.

Помоги:
1. Улучшить идею
2. Найти слабые места
3. Предложить growth hacks
4. Предложить стратегию роста
5. Дать советы founder'у
""", idea)


# 🌍 GLOBAL EXPANSION
def global_expansion(idea):
    return ask_ai("""
Создай стратегию глобального роста:

1. В какие страны выходить
2. Какие рынки лучшие
3. Риски
4. Локализация
5. Growth strategy
""", idea)


# 📱 APP FEATURES GENERATOR
def app_features(idea):
    return ask_ai("""
Создай список функций приложения:

1. Core features
2. Premium features
3. AI features
4. Viral mechanics
5. UX идеи
""", idea)


# ⚡ GROWTH HACKING
def growth_hacking(idea):
    return ask_ai("""
Создай growth hacking стратегию:

1. Как получить первых пользователей
2. Viral marketing
3. Social media strategy
4. Retention strategy
5. Low-budget marketing
""", idea)