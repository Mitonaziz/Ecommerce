# Generated by Django 4.2.4 on 2023-08-28 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LetsShop_App', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Super_SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('SubCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LetsShop_App.subcategory')),
            ],
        ),
    ]
