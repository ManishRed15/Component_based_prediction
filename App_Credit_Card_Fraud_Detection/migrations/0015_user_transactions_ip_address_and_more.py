# Generated by Django 4.1.4 on 2022-12-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App_Credit_Card_Fraud_Detection", "0014_user_transactions_exempt_rules"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_transactions",
            name="ip_address",
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user_transactions",
            name="mac_address",
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="user_details",
            name="phonenumber",
            field=models.IntegerField(default=None),
        ),
    ]
