from django.test import TestCase
from .models import Animal
# Create your tests here.


class AnimalTest(TestCase):

    def setUp(self):
        Animal.objects.create(name="lion", age=10)

    def test_animals_exact_age(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        self.assertEqual(lion.age, 10)

    def test_animals_unmatched_age(self):
        lion = Animal.objects.get(name="lion")
        self.assertEqual(lion.age, 11)
