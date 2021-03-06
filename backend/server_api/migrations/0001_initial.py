# Generated by Django 3.2.5 on 2021-09-26 17:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('longitude', models.CharField(max_length=50, unique=True, verbose_name='долгота')),
                ('latitude', models.CharField(max_length=50, unique=True, verbose_name='ширина')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='preview')),
                ('text', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='телеграм id')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='телеграм никнейм')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')),
                ('locations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server_api.location', verbose_name='id координат')),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
        migrations.CreateModel(
            name='IsSubscribed',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='server_api.subscriber', verbose_name='id пользователя')),
                ('is_subscribed', models.BooleanField(verbose_name='статус подписки')),
            ],
            options={
                'verbose_name': 'Статус подписки',
                'verbose_name_plural': 'Статус подписки',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100, unique=True, verbose_name='адрес')),
                ('locations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server_api.location', verbose_name='id координат')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='login')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='phone')),
                ('last_time_visit', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
