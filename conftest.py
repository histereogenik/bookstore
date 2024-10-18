import pytest
from django.contrib.auth.models import User
from product.models import Product
from order.models import Order

@pytest.fixture
def create_user():
    return User.objects.create_user(username="testuser", password="password")

@pytest.fixture
def create_products():
    product1 = Product.objects.create(title="test1", description="test1", price=889)
    product2 = Product.objects.create(title="test2", description="test2", price=111)
    return [product1, product2]

@pytest.fixture
def create_order(create_user, create_products):
    order = Order.objects.create(user=create_user)
    order.product.add(*create_products)
    return order