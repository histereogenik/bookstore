import pytest

@pytest.mark.django_db
def test_create_order(create_order):
    order = create_order

    assert order.user.username == "testuser"
    assert order.product.count() == 2