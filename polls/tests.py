import datetime
from django.utils import timezone
from django.test import TestCase

from polls.models import Question

# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        past = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=past)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        barely_recent = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=barely_recent)
        self.assertIs(recent_question.was_published_recently(), True)
