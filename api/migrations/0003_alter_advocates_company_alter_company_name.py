# Generated by Django 4.1.2 on 2022-10-07 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_advocates_created_at_advocates_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocates',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company', to_field='name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]