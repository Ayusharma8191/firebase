# Generated by Django 3.2.8 on 2023-03-07 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_fields', '0003_alter_extrafield_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedExtraField',
            fields=[
                ('extrafield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user_fields.extrafield')),
                ('fieldName', models.CharField(max_length=150)),
            ],
            bases=('user_fields.extrafield',),
        ),
    ]
