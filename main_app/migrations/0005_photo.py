# Generated by Django 3.2.9 on 2021-11-22 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211121_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('sym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sym')),
            ],
        ),
    ]
