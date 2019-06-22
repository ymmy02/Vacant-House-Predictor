from django.test import TestCase
from .predictor import predict

# Create your tests here.
class PredictorFunctionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_is_parcentage(self):
        house_image = object
        occupied_pct, vacant_pct = predict(house_image)
        self.assertTrue(0 <= occupied_pct <= 100)
        self.assertTrue(0 <= vacant_pct <= 100)
