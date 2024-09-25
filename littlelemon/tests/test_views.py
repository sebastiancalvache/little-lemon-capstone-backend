from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializer import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Steak", price=50, inventory=50)
        Menu.objects.create(title="Pancake", price=30, inventory=70)
        
        
    def test_getall(self):
        items = Menu.objects.all()
        menu = MenuSerializer(items,many=True)
        serialized_data = menu.data

        self.assertEqual(serialized_data[0]['title'], "IceCream")
        self.assertEqual(serialized_data[0]['price'], '80.00')
        self.assertEqual(serialized_data[0]['inventory'], 100)
        
        self.assertEqual(serialized_data[1]['title'], "Steak")
        self.assertEqual(serialized_data[1]['price'], '50.00')
        self.assertEqual(serialized_data[1]['inventory'], 50)
        
        self.assertEqual(serialized_data[2]['title'], "Pancake")
        self.assertEqual(serialized_data[2]['price'], '30.00')
        self.assertEqual(serialized_data[2]['inventory'], 70)                
