from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class Location(models.Model):

    id = models.AutoField(primary_key=True)
    longitude = models.CharField(
        max_length=50, unique=True, verbose_name='долгота')
    latitude = models.CharField(
        max_length=50, unique=True, verbose_name='ширина')

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

    def __str__(self):
        return f'{self.longitude} | {self.latitude}'


class Subscriber(models.Model):

    id = models.CharField(max_length=20, primary_key=True,
                          verbose_name='телеграм id')
    name = models.CharField(
        max_length=50, verbose_name='телеграм никнейм', unique=True)
    data = models.DateTimeField(
        auto_now_add=True, verbose_name='дата регистрации')
    locations = models.ForeignKey(
        'Location', on_delete=models.CASCADE, verbose_name='id координат', null=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return self.name


class Address(models.Model):

    id = models.AutoField(primary_key=True)
    address = models.CharField(
        max_length=100, unique=True, verbose_name='адрес')
    locations = models.ForeignKey(
        'Location', on_delete=models.CASCADE, verbose_name='id координат', null=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address


class IsSubscribed(models.Model):

    id = models.OneToOneField('Subscriber', on_delete=models.CASCADE,
                              primary_key=True, verbose_name='id пользователя')
    is_subscribed = models.BooleanField(verbose_name='статус подписки')

    class Meta:
        verbose_name = 'Статус подписки'
        verbose_name_plural = 'Статус подписки'

        def __str__(self):
            return f'{self.id} - {self.is_subscribed}'


class Post(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='preview')
    text = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

#  Переопределение класса User
class AccountManager(BaseUserManager):

    def create_user(self, username, password, **kwargs):
        if username is None:
            raise ValueError("Username don't must empty")
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **kwargs):

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        user = self.create_user(username=username, password=password, **kwargs)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField('login', max_length=20, unique=True)
    email = models.EmailField('email' ,max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField('phone', max_length=10, blank=True, null=True, unique=True)
    last_time_visit = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
#
