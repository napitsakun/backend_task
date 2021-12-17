from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.mail import send_mail

User = get_user_model()


def wish_birthday():
    today = timezone.now().date()
    user_list = User.objects.filter(birthday__day=today.day, birthday__month=today.month)
    
    for item in user_list:
        subject = 'Birthday Wish!'
        body = 'Hi {},\n Happy Birthday!!!'.format(item.username)
        send_mail(subject, body, 'contact@yourdomain.com', [item.email])