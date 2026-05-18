from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import Question, Quiz


class IndexView(generic.ListView):
    model = Quiz
    template_name = "quizzes/index.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("quizzes:index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    return redirect("quizzes:index")


def display_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = quiz.question_set.first()
    return redirect(reverse("quizzes:display_question", kwargs={"quiz_id": quiz_id, "question_id": question.pk}))


def display_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    # fetch ALL of the questions to find current and next question
    questions = quiz.question_set.all()
    current_question, next_question = None, None
    for ind, question in enumerate(questions):
        if question.pk == question_id:
            current_question = question
            if ind != len(questions) - 1:
                next_question = questions[ind + 1]

    return render(
        request,
        "quizzes/display.html",
        {"quiz": quiz, "question": current_question, "next_question": next_question},
    )


def grade_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = question.get_answer()
    if answer is None:
        return render(request, "quizzes/partial.html", {"error": "Question must have an answer"}, status=422)
    is_correct = answer.is_correct(request.POST.get("answer"))
    if is_correct and request.user.is_authenticated:
        from .models import UserScore
        user_score, created = UserScore.objects.get_or_create(user=request.user)
        user_score.score += 10
        user_score.save()
    return render(
        request,
        "quizzes/partial.html",
        {"is_correct": is_correct, "correct_answer": answer.correct_answer},
    )


def ranking(request):
    from .models import UserScore
    scores = UserScore.objects.select_related("user").order_by("-score")[:20]
    return render(request, "quizzes/ranking.html", {"scores": scores})

