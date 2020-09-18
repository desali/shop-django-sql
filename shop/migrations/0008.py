# Generated by Django 3.0.5 on 2020-04-18 20:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0007'),
    ]

    operations = [
        migrations.RunSQL('''
    
    CREATE TABLE "customer_phone" (
        "id" INT NOT NULL,
        "phone" NUMBER(10, 0) UNIQUE NOT NULL,
        "customer_id" INT NOT NULL,
        constraint CUSTOMER_PHONE_PK PRIMARY KEY ("id"));
    
     '''),
    ]
