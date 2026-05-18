import pytest
from django.urls import reverse
from quizzes.models import Quiz, Question, FreeTextAnswer, UserScore
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_ranking_page_accessible(client):
    """
    Test that the ranking leaderboard page is accessible via GET,
    returns 200, and displays the leaderboard headers.
    """
    # Create a mock user score to ensure the leaderboard table is rendered
    user = User.objects.create_user(username="testrunner", password="password")
    UserScore.objects.create(user=user, score=100)

    url = reverse("quizzes:ranking")
    response = client.get(url)
    
    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "Ranking Global" in content
    assert "Pontuação Total" in content
    assert "Ranking" in content




@pytest.mark.django_db
def test_grade_question_adds_score_for_logged_in_user(client):
    """
    Test that answering a question correctly as an authenticated user
    awards the user 10 points and registers the UserScore object.
    """
    # Create user and login
    username = "player1"
    password = "pass123password"
    user = User.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    
    # Create Quiz, Question and FreeTextAnswer
    quiz = Quiz.objects.create(name="Python Test")
    question = Question.objects.create(quiz=quiz, prompt="What is 1 + 1?")
    FreeTextAnswer.objects.create(question=question, correct_answer="2", case_sensitive=False)
    
    # Submit correct answer
    url = reverse("quizzes:grade_question", args=[question.id])
    response = client.post(url, {"answer": "2"})
    
    assert response.status_code == 200
    
    # Check that score was successfully generated and incremented
    user_score = UserScore.objects.get(user=user)
    assert user_score.score == 10


@pytest.mark.django_db
def test_grade_question_does_not_add_score_for_guests(client):
    """
    Test that answering a question as a guest does not award any score.
    """
    # Create Quiz, Question and FreeTextAnswer
    quiz = Quiz.objects.create(name="Python Test")
    question = Question.objects.create(quiz=quiz, prompt="What is 1 + 1?")
    FreeTextAnswer.objects.create(question=question, correct_answer="2", case_sensitive=False)
    
    # Submit correct answer anonymously
    url = reverse("quizzes:grade_question", args=[question.id])
    response = client.post(url, {"answer": "2"})
    
    assert response.status_code == 200
    
    # Verify no UserScore object was created
    assert UserScore.objects.count() == 0


@pytest.mark.django_db
def test_ranking_ordered_correctly(client):
    """
    Test that users are displayed in the leaderboard ordered by their scores in descending order.
    """
    # Create users
    u1 = User.objects.create_user(username="alex", password="password")
    u2 = User.objects.create_user(username="beatriz", password="password")
    u3 = User.objects.create_user(username="carlos", password="password")
    
    # Assign scores: beatriz (30 pts), carlos (20 pts), alex (10 pts)
    UserScore.objects.create(user=u1, score=10)
    UserScore.objects.create(user=u2, score=30)
    UserScore.objects.create(user=u3, score=20)
    
    # Query leaderboard
    url = reverse("quizzes:ranking")
    response = client.get(url)
    
    assert response.status_code == 200
    content = response.content.decode("utf-8")
    
    # Assert that beatriz is listed before carlos, and carlos before alex
    idx_beatriz = content.find("beatriz")
    idx_carlos = content.find("carlos")
    idx_alex = content.find("alex")
    
    assert idx_beatriz != -1
    assert idx_carlos != -1
    assert idx_alex != -1
    assert idx_beatriz < idx_carlos < idx_alex
