password_secret = ('python123')
guess = input('Набери пароль:')


if guess == password_secret:
    print('Доступ разрешен')
else:
    print('Ошибка,попробуйте снова')