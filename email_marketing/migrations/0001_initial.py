# Generated by Django 4.2.7 on 2023-11-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.TextField()),
                ('receiver', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('EMAIL_BACKEND', models.CharField(max_length=300)),
                ('EMAIL_USE_TLS', models.BooleanField(default=True)),
                ('EMAIL_HOST', models.CharField(max_length=255)),
                ('EMAIL_PORT', models.IntegerField()),
                ('EMAIL_HOST_USER', models.CharField(max_length=255)),
                ('EMAIL_HOST_PASSWORD', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('design', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('category', models.ManyToManyField(to='email_marketing.category')),
            ],
        ),
    ]
