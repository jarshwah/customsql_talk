import datetime
import random
from bisect import bisect
from decimal import Decimal
from django.utils import timezone


def delete_initial_data(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    Product.objects.all().delete()


def create_initial_data(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    Sale = apps.get_model('shop', 'Sale')

    products = [
        Product.objects.create(name='Leather Shoes', category='Men', cost_price=Decimal('120.00')),
        Product.objects.create(name='Winter Coat', category='Men', cost_price=Decimal('190.00')),
        Product.objects.create(name='Beanie', category='Men', cost_price=Decimal('19.00')),

        Product.objects.create(name='Boots', category='Women', cost_price=Decimal('90.00')),
        Product.objects.create(name='Long Overcoat', category='Women', cost_price=Decimal('210.00')),
        Product.objects.create(name='Scarf', category='Women', cost_price=Decimal('18.50')),

        Product.objects.create(name='Gum Boots', category='Kids', cost_price=Decimal('15.00')),
        Product.objects.create(name='Gloves', category='Kids', cost_price=Decimal('10.00')),
        Product.objects.create(name='Rain Jacket', category='Kids', cost_price=Decimal('35.00')),
    ]

    start_period = datetime.datetime(2015, 7, 1, tzinfo=timezone.utc)
    end_period = datetime.datetime(2016, 6, 30, tzinfo=timezone.utc)
    diff = end_period - start_period
    diff_seconds = (diff.days * 24 * 60 * 60) + diff.seconds

    # Skew state choices
    weighted_states = [
        ('VIC', 350), ('NSW', 350), ('QLD', 100), ('TAS', 100), ('SA', 50), ('WA', 50)
    ]
    states, weights = zip(*weighted_states)
    total = 0
    cumulative_weights = []
    for w in weights:
        total += w
        cumulative_weights.append(total)

    for _ in range(1000):
        product = random.choice(products)
        random_second = random.randrange(diff_seconds)
        diff_seconds -= 20000  # skew towards newer sales to highlight growth
        sale_date = end_period - datetime.timedelta(seconds=random_second)
        state_index = bisect(cumulative_weights, random.random() * total)
        Sale.objects.create(
            product=product,
            sale_date=sale_date,
            sale_price=product.cost_price + random.randint(1, 20),
            state=states[state_index]
        )
