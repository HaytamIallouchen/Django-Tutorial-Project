# Generated by Django 4.0.2 on 2022-02-15 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial', '0005_author_book_remove_books_authors_name_delete_authors_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors_id',
        ),
    ]
