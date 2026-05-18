import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_login_page_accessible(client):
    """
    Test that the login page is accessible via GET request, returns an HTTP 200 status code,
    and displays the expected login form components.
    """
    # Obtain the login URL
    url = reverse("login")
    
    # Make GET request
    response = client.get(url)
    
    # Check status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that crucial page content is present
    content = response.content.decode("utf-8")
    assert "Welcome Back" in content
    assert "Login to your account to continue" in content
    assert "Sign In" in content
    assert "register" in content  # Link to registration page


@pytest.mark.django_db
def test_login_successful_redirect(client):
    """
    Test that submitting the login form with valid credentials redirects the user
    to the quizzes homepage (index) as defined by LOGIN_REDIRECT_URL.
    """
    from django.contrib.auth.models import User
    
    # Create a test user
    username = "testuser"
    password = "password123"
    User.objects.create_user(username=username, password=password, email="test@example.com")
    
    # Submit login POST request
    login_url = reverse("login")
    response = client.post(login_url, {"username": username, "password": password})
    
    # Assert redirect to the quizzes homepage (quizzes:index)
    assert response.status_code == 302
    assert response.url == reverse("quizzes:index")


@pytest.mark.django_db
def test_logout_redirect(client):
    """
    Test that logging out redirects the user to the quizzes homepage (index)
    as defined by LOGOUT_REDIRECT_URL.
    """
    from django.contrib.auth.models import User
    
    # Create and login a user
    username = "testuser"
    password = "password123"
    User.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    
    # Logout (Django 4.2 supports POST logout)
    logout_url = reverse("logout")
    response = client.post(logout_url)
    
    # Assert redirect to the quizzes homepage (quizzes:index)
    assert response.status_code == 302
    assert response.url == reverse("quizzes:index")

