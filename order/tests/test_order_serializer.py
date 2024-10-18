import pytest

from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer(create_order):
    order = create_order
    serializer = OrderSerializer(order)
    serialized_data = serializer.data

    expected_data = {
        'product': [
            {
                'title': 'test1',
                'description': 'test1',
                'price': 889,
                'active': True,
                'category': []
            },
            {
                'title': 'test2',
                'description': 'test2',
                'price': 111,
                'active': True,
                'category': []
            }
        ],
        'total': 1000
    }

    assert serialized_data == expected_data