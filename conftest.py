import pytest
from django.contrib.auth.models import User
from order.factories import OrderFactory
from product.factories import ProductFactory


@pytest.fixture
def create_order():
    user = User.objects.create_user(username="testuser", password="password")
    product1 = ProductFactory(title="test1", description="test1", price=889)
    product2 = ProductFactory(title="test2", description="test2", price=111)
    return OrderFactory(user=user, product=[product1, product2])
