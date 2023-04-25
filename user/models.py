from django.contrib.auth.models import User


class CustomUser(User):
    pass

CustomUser._meta.get_field('email')._unique = True

CustomUser._meta.get_field('username').verbose_name = 'Имя пользователя'
CustomUser._meta.get_field('email').verbose_name = 'Email'
CustomUser._meta.get_field('password').verbose_name = 'Пароль'

CustomUser._meta.get_field('username').help_text = 'Обязательно. Максимум 150 символов. Только буквы, цифры и символы @/./+/-/_ .'
CustomUser._meta.get_field('email').help_text = 'Обязательно. Уникальный адрес электронной почты'
CustomUser._meta.get_field('password').help_text = 'Обязательно. Минимум 8 символов.'

CustomUser._meta.get_field('username').error_messages = {
    'unique': "Пользователь с таким именем уже существует.",
}

CustomUser._meta.get_field('email').error_messages = {
    'unique': "Пользователь с таким email уже существует.",
}


