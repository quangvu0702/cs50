# Generated by Django 2.2.5 on 2019-09-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190925_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in U$S', max_digits=4)),
            ],
        ),
    ]
