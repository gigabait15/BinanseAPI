# Generated by Django 5.1.6 on 2025-03-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cryptoprice',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Цена криптовалюты', 'verbose_name_plural': 'Цены криптовалют'},
        ),
        migrations.AlterField(
            model_name='cryptoprice',
            name='price',
            field=models.DecimalField(decimal_places=8, max_digits=20, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='cryptoprice',
            name='symbol',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Тикер'),
        ),
        migrations.AlterField(
            model_name='cryptoprice',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время записи'),
        ),
    ]
