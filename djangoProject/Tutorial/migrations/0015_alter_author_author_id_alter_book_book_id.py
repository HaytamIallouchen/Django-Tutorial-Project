# Generated by Django 4.0.2 on 2022-02-17 12:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial', '0014_alter_author_author_id_alter_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]