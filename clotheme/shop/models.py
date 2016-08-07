from django.db import models


class Product(models.Model):
    KIDS = 'Kids'
    MEN = 'Men'
    WOMEN = 'Women'

    categories = (
        (KIDS, KIDS), (MEN, MEN), (WOMEN, WOMEN)
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=categories)
    cost_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    VIC = 'VIC'
    NSW = 'NSW'
    QLD = 'QLD'
    TAS = 'TAS'
    SA = 'SA'
    WA = 'WA'
    states = (
        (VIC, VIC), (NSW, NSW), (QLD, QLD),
        (TAS, TAS), (SA, SA), (WA, WA)
    )

    product = models.ForeignKey(Product)
    sale_date = models.DateTimeField()
    sale_price = models.DecimalField(max_digits=7, decimal_places=2)
    state = models.CharField(max_length=3, choices=states)

    def __str__(self):
        return "<{0}>: {1}".format(self.pk, self.sale_price)


# -- sales per quarter  (Trunc Datetime)
# -- revenue
# -- revenue per region (SUMIF)
# -- for pricier items, excluding kids items
#
# SELECT
#     trunc(sale_date, 'QQ'),
#     count(id),
#     sum(sale_price),
#     sum(case when state = 'VIC' then sale_price else 0 end),
#     sum(case when state = 'NSW' then sale_price else 0 end),
#     sum(case when state not in ('VIC', 'NSW') then sale_price else 0 end)
# FROM sales   s
# JOIN product p on s.product_id = p.id
# WHERE
#     p.category != 'Kids'
# AND p.cost_price > 30.00
# GROUP BY
#     trunc(sale_date, 'QQ')
# ;
