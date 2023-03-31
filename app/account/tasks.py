from celery import shared_task


@shared_task
def debug():
    print("DEBUG\n" * 10)
