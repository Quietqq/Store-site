# Generated by Django 4.2 on 2023-07-27 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_category_basket"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Product", "verbose_name_plural": "Products"},
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={"verbose_name": "Category", "verbose_name_plural": "Caregories"},
        ),
    ]
