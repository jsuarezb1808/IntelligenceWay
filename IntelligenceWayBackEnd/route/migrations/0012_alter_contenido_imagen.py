# Generated by Django 5.1.1 on 2024-10-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0011_alter_contenido_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='imagen',
            field=models.ImageField(blank=True, default='IntelligenceWay/static/contenidos/img/default_image.jpg', null=True, upload_to='IntelligenceWay/static/contenidos/img/'),
        ),
    ]
