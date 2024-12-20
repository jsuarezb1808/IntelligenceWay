# Generated by Django 5.1.1 on 2024-10-14 05:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0003_rename_formularioaprendizajeusuario_modeloaprendizajeusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloaprendizajeusuario',
            name='q1',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='modeloaprendizajeusuario',
            name='q2',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='modeloaprendizajeusuario',
            name='q3',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='modeloaprendizajeusuario',
            name='q4',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
