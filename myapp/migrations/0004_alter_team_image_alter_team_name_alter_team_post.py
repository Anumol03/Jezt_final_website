# Generated by Django 4.2.3 on 2023-10-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_team_delete_members"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="image",
            field=models.ImageField(upload_to="Team"),
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name="team",
            name="post",
            field=models.TextField(max_length=100),
        ),
    ]
