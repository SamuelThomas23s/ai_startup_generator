# 🤖 SAAS IDEA GENERATOR
def saas_ideas(topic):
    return ask_ai("""
Ты AI startup strategist.

Придумай:
1. 5 SaaS идей
2. AI product идеи
3. Micro SaaS идеи
4. Какие идеи проще запустить
5. Какие идеи самые прибыльные
""", topic)


# 💵 PRICING STRATEGY
def pricing_strategy(idea):
    return ask_ai("""
Создай pricing strategy:

1. Free plan
2. Premium plan
3. Enterprise plan
4. Freemium strategy
5. Как увеличить LTV
""", idea)


# 🦄 UNICORN POTENTIAL
def unicorn_score(idea):
    return ask_ai("""
Оцени стартап:

1. Unicorn potential
2. TAM
3. Growth potential
4. Venture scalability
5. Итоговый score 0-100
""", idea)


# 🧠 FOUNDER ANALYSIS
def founder_analysis(founder_info):
    return ask_ai("""
Проанализируй founder profile:

1. Сильные стороны
2. Слабые стороны
3. Какие навыки развивать
4. Какие cofounders нужны
5. Founder success probability
""", founder_info)