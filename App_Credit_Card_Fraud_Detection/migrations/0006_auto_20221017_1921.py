# Generated by Django 3.2.16 on 2022-10-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Credit_Card_Fraud_Detection', '0005_user_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_transactions',
            name='Amount',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='CINO',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='Date',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='Name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='Status',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='Time',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='User_ID',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='country',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_transactions',
            name='expiry_date',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
