import pizza

pizza.make_pizza(12,'a','b','c')


from pizza import make_pizza

make_pizza(10,'a','c','b')

import pizza as p

p.make_pizza(12,'a','b','c')


from pizza import make_pizza as p2

p2(10,'a','c','b')