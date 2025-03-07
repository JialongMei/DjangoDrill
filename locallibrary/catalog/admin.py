from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class BookInline(admin.TabularInline):
    model = Book
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]


admin.site.register(Author,AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','isbn','display_genre','language')

    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'imprint', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None,{
            'fields': ('id', 'book', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }
        )
    )
