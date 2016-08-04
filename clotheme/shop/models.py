#from django.db import models


# -- sales per quarter  (Trunc Datetime)
# -- revenue
# -- revenue per region (SUMIF)
# -- for cheaper items, excluding kids items
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
# AND p.cost_price < 20.00
# GROUP BY
#     trunc(sale_date, 'QQ')
# ;
