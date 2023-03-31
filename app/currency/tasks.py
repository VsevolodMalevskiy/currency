from celery import shared_task


# @shared_task(autoretry_for=(ConnectionError,),  # при ошибке повтор отправки
#              retry_kwargs={'max_retries': 5})
# def send_mail(subject, message):
#     raise ConnectionError
# '''
#  1 - 2 sec
#  2 - 4 sec
#  3 - 8 sec
#  4 - 16 sec
#  5 - error
#  '''
@shared_task
def send_mail(subject, message):
    recipient = 'support@rambler.ru'
    sender = 'User@gmail.com'
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        sender,
        [recipient, sender],
        fail_silently=False,
    )
