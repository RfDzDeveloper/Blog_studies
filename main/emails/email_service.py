from django.core.mail import EmailMessage
import main.settings as settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailService:
    forgot_pass_template: str = 'forgot_password.html/'
    confirmation_account: str = 'confirm_account.html/'
    main_email: str = settings.EMAIL_HOST_USER

    def __init__(self, firstname: str, to: list[str], email: str = None):        
        self.firstname: str = firstname
        self.email: str = email
        self.to: list[str] = to

    def send_reset_pass(self, token: str) -> None:
        template: str = render_to_string(self.forgot_pass_template, 
            {'firstname': self.firstname,
             'token': token})
        EmailMessage(
            subject=f'Hello {self.firstname}', body=strip_tags(template), to=self.to, 
            from_email=self.main_email).send()

    def send_confirmation_email(self, token) -> None:
        template: str = render_to_string(self.confirmation_account, 
            {'token': token, 'first_name': self.firstname})

        EmailMessage(subject=f"Please confirm your account {self.firstname}",
            body=strip_tags(template), to=self.to, from_email=self.main_email).send()