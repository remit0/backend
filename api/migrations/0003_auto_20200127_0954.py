# Generated by Django 3.0.2 on 2020-01-27 09:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20200126_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.CharField(choices=[('-', '-'), ('CARREFOUR', 'Carrefour'), ('MONOPRIX', 'Monoprix'), ('FRANPRIX', 'Franprix'), ('LECLERC', 'Leclerc'), ('AUCHAN', 'Auchan')], default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('-', '-'), ('BEER', 'Beer'), ('WINE', 'Wine'), ('RUM', 'Rum'), ('TEQUILA', 'Tequila'), ('VODKA', 'Vodka'), ('WHISKY', 'Whisky')], default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='vol',
            field=models.FloatField(default=-1, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.IntegerField(default=-1),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=-1, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(5)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
