# Generated by Django 2.1.3 on 2019-01-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0003_auto_20190120_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='fazendeiro',
            name='salario',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6),
            preserve_default=False,
        ),
    ]