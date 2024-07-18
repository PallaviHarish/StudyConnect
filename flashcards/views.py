# flashcards/views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Flashcard, QuizOption
from .forms import FlashcardForm, QuizOptionForm

def add_question(request):
    if request.method == 'POST':
        flashcard_form = FlashcardForm(request.POST)
        option_forms = [QuizOptionForm(request.POST, prefix=str(i)) for i in range(4)]
        
        if flashcard_form.is_valid() and all(option_form.is_valid() for option_form in option_forms):
            flashcard = flashcard_form.save()
            for option_form in option_forms:
                option = option_form.save(commit=False)
                option.question = flashcard
                option.save()
            return redirect('quiz')
    else:
        flashcard_form = FlashcardForm()
        option_forms = [QuizOptionForm(prefix=str(i)) for i in range(4)]
    
    return render(request, 'flashcards/add_question.html', {'flashcard_form': flashcard_form, 'option_forms': option_forms})

def quiz_view(request):
    topics = Flashcard.objects.values_list('topic', flat=True).distinct()
    return render(request, 'flashcards/quiz_topics.html', {'topics': topics})

def quiz_questions_by_topic(request, topic):
    flashcards = Flashcard.objects.filter(topic=topic)
    return render(request, 'flashcards/quiz_questions_by_topic.html', {'flashcards': flashcards})

def quiz_question(request, pk):
    flashcard = Flashcard.objects.get(pk=pk)
    options = QuizOption.objects.filter(question=flashcard)
    answer_feedback = None
    
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        correct_option = flashcard.answer
        
        if selected_option.lower() == correct_option.lower():
            request.session['points'] = request.session.get('points', 0) + 10
            answer_feedback = 'Correct!'
        else:
            answer_feedback = f'Incorrect. The correct answer is: {correct_option}'

    return render(request, 'flashcards/quiz_question.html', {'flashcard': flashcard, 'options': options, 'answer_feedback': answer_feedback})
