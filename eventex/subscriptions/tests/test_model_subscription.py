from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubcriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name ='Fabricio Gatto',
            cpf='12345678901',
            email='fa_gatto7@yahoo.com.br',
            phone='21-97979-9797'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)