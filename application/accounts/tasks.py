from django.core.mail import send_mail
from main.celery import app

@app.task
def send_confirmation_email_mentor(email, code):
    full_link = f"http://127.0.0.1:8000/api/v1/accounts/confirm-mentor/{code}"
    send_mail(
        "User activation",
        f"Пожалуйста подтвердите аккаунт перейдя по ссылке:  {full_link}",
        "sabyrkulov.nurmuhammed@gmail.com",
        [email]
    )
    
@app.task
def send_confirmation_email(email, code):
    full_link = f"http://127.0.0.1:8000/api/v1/accounts/confirm/{code}"
    send_mail(
        "User activation",
        f"Пожалуйста подтвердите аккаунт перейдя по ссылке:  {full_link}",
        "sabyrkulov.nurmuhammed@gmail.com",
        [email]
    )
    

@app.task
def send_password_recovery(email, code, recovery_code):
    full_link = f"http://127.0.0.1:8000/api/v1/accounts/recovery/{code}"
    send_mail(
        "Password recovery",
        f"Перейдите по ссылке чтобы сбросить пароль:  {full_link}\n"
        f"Код для сброса пароля:  {recovery_code}",
        "sabyrkulov.nurmuhammed@gmail.com",
        [email]
    )