from django.test import TestCase
from django.conf import settings

from .predictor import predict

from PIL import Image

# Create your tests here.
class PredictorFunctionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_is_parcentage(self):
        vacant_house_image = Image.open(settings.TESTIMAGE_ROOT + '/vacant1.jpg').convert('RGB')
        (occupied_pct, vacant_pct) = predict(vacant_house_image)
        self.assertTrue(0 <= occupied_pct <= 100)
        self.assertTrue(0 <= vacant_pct <= 100)

    def test_total_100_parcent(self):
        vacant_house_image = Image.open(settings.TESTIMAGE_ROOT + '/vacant1.jpg').convert('RGB')
        (occupied_pct, vacant_pct) = predict(vacant_house_image)
        total = occupied_pct + vacant_pct
        self.assertTrue(abs(total - 100) <= 0.01)

    def test_vacant_house(self):
        vacant_house_image = Image.open(settings.TESTIMAGE_ROOT + '/vacant1.jpg').convert('RGB')
        (occupied_pct, vacant_pct) = predict(vacant_house_image)
        print('Occupied Parcentage:', occupied_pct)
        print('Vacant Parcentage:', vacant_pct)
        self.assertTrue(occupied_pct < 50)
        self.assertTrue(vacant_pct > 50)

    def test_occupied_house(self):
        occupied_house_image = Image.open(settings.TESTIMAGE_ROOT + '/occupied1.jpg').convert('RGB')
        (occupied_pct, vacant_pct) = predict(occupied_house_image)
        print('Occupied Parcentage:', occupied_pct)
        print('Vacant Parcentage:', vacant_pct)
        self.assertTrue(occupied_pct > 50)
        self.assertTrue(vacant_pct < 50)
