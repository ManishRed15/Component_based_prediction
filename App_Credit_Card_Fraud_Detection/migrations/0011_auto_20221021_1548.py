# Generated by Django 3.2.16 on 2022-10-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Credit_Card_Fraud_Detection', '0010_auto_20221021_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_transactions',
            name='payment_Date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='payment_Time',
            field=models.TimeField(default=None, null=True),
        ),
    ]
