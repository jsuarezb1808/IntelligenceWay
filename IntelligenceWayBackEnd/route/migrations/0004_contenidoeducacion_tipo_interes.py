# Generated by Django 4.2.5 on 2024-09-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_contenidoeducacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenidoeducacion',
            name='tipo_interes',
            field=models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('django', 'Django')], default='python', max_length=10),
        ),
    ]
