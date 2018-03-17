# Generated by Django 2.0 on 2018-03-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_sc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userentreprise',
            name='qualité',
        ),
        migrations.RemoveField(
            model_name='userinstitution',
            name='qualité',
        ),
        migrations.AddField(
            model_name='userentreprise',
            name='adresse',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userinstitution',
            name='adresse',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='useretudiant',
            name='adresse',
            field=models.CharField(default='', max_length=255),
        ),
    ]