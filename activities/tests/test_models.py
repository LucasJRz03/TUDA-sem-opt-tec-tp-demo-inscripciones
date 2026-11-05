from django.db import IntegrityError, transaction
from activities.models import Registration
from .support import NOW, BaseCase

class RegistrationConstraintTests(BaseCase):
    def test_cancelled_and_current_registrations_coexist(self):
        Registration.objects.create(student=self.ana, activity=self.activity, cancelled_at=NOW)
        Registration.objects.create(student=self.ana, activity=self.activity)
        self.assertEqual(Registration.objects.filter(student=self.ana, activity=self.activity).count(), 2)
    def test_history_keeps_multiple_cancelled_rows_and_allows_a_new_current(self):
        current = Registration.objects.create(student=self.ana, activity=self.activity)
        Registration.objects.create(student=self.ana, activity=self.activity, cancelled_at=NOW)
        self.assertEqual(Registration.objects.filter(student=self.ana, activity=self.activity).count(), 2)
        Registration.objects.filter(pk=current.pk).update(cancelled_at=NOW)
        Registration.objects.create(student=self.ana, activity=self.activity)
        self.assertEqual(Registration.objects.filter(student=self.ana, activity=self.activity).count(), 3)
    def test_two_current_registrations_are_rejected(self):
        Registration.objects.create(student=self.ana, activity=self.activity)
        with self.assertRaises(IntegrityError), transaction.atomic():
            Registration.objects.create(student=self.ana, activity=self.activity)
        self.assertEqual(Registration.objects.filter(cancelled_at__isnull=True).count(), 1)
