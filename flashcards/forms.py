# flashcards/forms.py
from django import forms
from .models import Flashcard, QuizOption

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question', 'answer', 'topic']

class QuizOptionForm(forms.ModelForm):
    class Meta:
        model = QuizOption
        fields = ['option_text']
