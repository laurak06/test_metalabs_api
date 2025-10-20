from django.core.mail import send_mail
from decouple import config

HOST = config('HOST_FOR_SEND_MAIL')


def send_activation_email(email, activation_code):
    activation_url = f'{HOST}/users/activate/?code={activation_code}'
    message = ''
    html = f'''
<h1>Для активации нажмите на кнопку</h1>
<a href="{activation_url}">
<button>Activate</button>
</a>
'''
    send_mail(
        subject='Активация аккаунта',
        message=message,
        from_email='a@gmail.com',
        recipient_list=[email],
        html_message=html
    )

def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        subject='Восстановление пароля',
        message=f'Код для восстановления пароля {code}',
        from_email='a@gmail.com',
        recipient_list=[to_email],
        fail_silently=False
    )