from django.contrib import admin

from Tutorial.models import Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    inlines = [BookInline]
# class AuthorAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,        {'fields': ['name']}),
#         ('Author age', {'fields': ['age'], 'classes': ['collapse']}),
#     ]
#     inlines = [BookInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'author_id', 'released_at')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
