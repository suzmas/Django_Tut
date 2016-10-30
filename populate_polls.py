from django.utils import timezone
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from polls.models import Question, Choice

cont = True

while cont == True:
    user_input = raw_input('Add or End')
    if user_input == "Add":
        now = timezone.now()
        question = raw_input("Question: ")
        q = Question.objects.get_or_create(question_text=question, pub_date=now)[0]
        q.save()
        choices = raw_input("How many choices?")
        for i in range(int(choices)):
            choice = raw_input("Choice:")
            q.choice_set.create(choice_text=choice)
    if user_input == "End":
        cont = False
