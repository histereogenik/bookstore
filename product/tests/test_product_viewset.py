import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory
from product.models.product import Product

class TestProductViewSet(APITestCase):
    
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()

        self.product = ProductFactory(
            title='pro controller',
            price=200.00,
        )

    def test_get_all_products(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)
        self.assertEqual(product_data[0]['title'], self.product.title)
        self.assertEqual(product_data[0]['price'], self.product.price)
        self.assertEqual(product_data[0]['active'], self.product.active)

    def test_get_single_product(self):
        product_id = self.product.id

        response = self.client.get(
            reverse('product-detail', kwargs={'version': 'v1', 'pk': product_id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)

        self.assertEqual(product_data['title'], self.product.title)
        self.assertEqual(product_data['price'], self.product.price)

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps({
            'title': 'notebook',
            'price': 800.00,
            'categories_id': [ category.id ]
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title='notebook')

        self.assertEqual(created_product.title, 'notebook')
        self.assertEqual(created_product.price, 800.00)

    def test_delete_product(self):
        product_id = self.product.id

        response = self.client.delete(
            reverse('product-detail', kwargs={'version': 'v1', 'pk': product_id})
        )

        # import pdb; pdb.set_trace()
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)