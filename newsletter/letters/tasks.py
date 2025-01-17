from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import random
from django.apps import apps


def send_email(param1, param2, param3):
    MailingAttempt = apps.get_model('letters', 'MailingAttempt')

    # Логика отправки email
    print(f"Адресат: {param1}, сообщение: {param2}")

    feedback = random.choice([True, False])

    # Создание записи для MailingAttempt
    mailing_attempt = MailingAttempt(
        mailing_id=param3,
        status='successful' if feedback else 'failed'
    )

    mailing_attempt.save()
    return feedback


def add_mytask(id, periodicity, customer_emails, message):
    scheduler = BackgroundScheduler(timezone='Europe/Moscow')
    # Логика для добавления задачи
    print(f"Задача добавлена для рассылки: {id} с периодичностью: {periodicity}, "
          f"email-адресами клиентов: {customer_emails}, и сообщением: {message}")
    # Добаввим задачу на рассылку в зависимости от периодичности
    if periodicity == 'daily':
        trigger = CronTrigger(day='*', hour='8', minute='0')
    if periodicity == 'weekly':
        trigger = CronTrigger(day_of_week='sat', hour='12', minute='0')
    if periodicity == 'monthly':
        trigger = CronTrigger(day='1', hour='12', minute='0')
    if trigger == None:
        from datetime import datetime
        trigger = datetime.now  # Задайте нужную дату и время
    for e in customer_emails:
        scheduler.add_job(send_email, trigger=trigger, args=[e, message, id])
    scheduler.start()
