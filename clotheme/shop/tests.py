from decimal import Decimal
from django.db.models import Q
from django.test import TestCase

from .functions import SumIf
from .models import Product, Sale


class ShopTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # we don't want data created by data migrations
        Product.objects.all().delete()

    def test_smoketest(self):
        self.assertTrue(True)

    def test_notequal(self):
        Product.objects.create(name='EXCL', category=Product.WOMEN, cost_price=Decimal('10.00'))
        Product.objects.create(name='INCL_A', category=Product.WOMEN, cost_price=Decimal('3.00'))
        Product.objects.create(name='INCL_B', category=Product.WOMEN, cost_price=Decimal('6.00'))

        self.assertQuerysetEqual(
            Product.objects.filter(name__ne='EXCL').order_by('name'), [
                ('INCL_A', Product.WOMEN), ('INCL_B', Product.WOMEN),
            ], lambda p: (p.name, p.category)
        )

    def test_sumif_condition(self):
        Product.objects.create(name='EXCL', category=Product.WOMEN, cost_price=Decimal('10.00'))
        Product.objects.create(name='INCL_A', category=Product.WOMEN, cost_price=Decimal('3.00'))
        Product.objects.create(name='INCL_B', category=Product.WOMEN, cost_price=Decimal('6.00'))

        qs = Product.objects.filter(category=Product.WOMEN).values('category').annotate(
            total=SumIf('cost_price', name__startswith='INCL')
        )
        self.assertQuerysetEqual(qs, [
                {"category": Product.WOMEN, "total": Decimal('9.00')}
            ], lambda o: o
        )

    def test_sumif_qlookup(self):
        Product.objects.create(name='EXCL', category=Product.WOMEN, cost_price=Decimal('10.00'))
        Product.objects.create(name='INCL_A', category=Product.WOMEN, cost_price=Decimal('3.00'))
        Product.objects.create(name='INCL_B', category=Product.WOMEN, cost_price=Decimal('6.00'))

        qs = Product.objects.filter(category=Product.WOMEN).values('category').annotate(
            total=SumIf('cost_price', Q(name__startswith='INCL'))
        )
        self.assertQuerysetEqual(qs, [
                {"category": Product.WOMEN, "total": Decimal('9.00')}
            ], lambda o: o
        )
