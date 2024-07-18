from django.contrib import admin
from .models import Flashcard, QuizOption

class QuizOptionInline(admin.TabularInline):
    model = QuizOption

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    inlines = [
        QuizOptionInline,
    ]

admin.site.register(QuizOption)
