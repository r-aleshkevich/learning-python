from random import choice

answers = ["Да, абсолютно!", "Нет, даже не думай!", "Спроси позже"]

#Вызываем choice напрямую (без random.choice)
random_answers = choice(answers)

print("Вопрос: Стоит ли мне сегодня учить Python?")
print(random_answers)