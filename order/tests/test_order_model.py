import pytest

from django.contrib.auth.models import User
from product.models.product import Product
from order.models.order import Order

@pytest.mark.django_db
def test_create_order():
    user = User.objects.create_user(username="testuser", password="password")

    product1 = Product.objects.create(
        title="test1",
        description="test1",
        price="999"
        )
    
    product2 = Product.objects.create(
        title="test2",
        description="test2",
        price="111"
        )
    
    order = Order.objects.create(user=user)

    order.product.add(product1, product2)

    assert order.user == user
    assert order.product.count() == 2
    assert product1 in order.product.all()
    assert product2 in order.product.all()