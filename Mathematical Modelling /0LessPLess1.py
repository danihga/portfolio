# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:33:21 2021

@author: Dani
"""

from sympy import *
x, y = symbols('x y')     

eq1 = Eq(abs(x**(9/10)) + abs(y**(9/10)), 1)
eq2 = Eq(abs(x**(8/10)) + abs(y**(8/10)), 1)
eq3 = Eq(abs(x**(7/10)) +abs(y**(7/10)), 1)
eq4 = Eq(abs(x**(6/10)) +abs(y**(6/10)), 1)
eq5 = Eq(abs(x**(5/10)) +abs(y**(5/10)), 1)
eq6 = Eq(abs(x**(4/10)) +abs(y**(4/10)), 1)
eq7 = Eq(abs(x**(3/10)) +abs(y**(3/10)), 1)
eq8 = Eq(abs(x**(2/10)) +abs(y**(2/10)), 1)
eq9 = Eq(abs(x**(1/10)) +abs(y**(1/10)), 1)

p1 = plot_implicit(eq1, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p2 = plot_implicit(eq2, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p3 = plot_implicit(eq3, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p4 = plot_implicit(eq4, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p5 =plot_implicit(eq5, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p6 = plot_implicit(eq6, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p7 = plot_implicit(eq7, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p8 =plot_implicit(eq8, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p9 = plot_implicit(eq9, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))

