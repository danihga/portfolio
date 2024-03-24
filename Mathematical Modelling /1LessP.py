# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:33:21 2021

@author: Dani
"""

from sympy import *
x, y = symbols('x y')     

eq1 = Eq(abs(x**(1)) + abs(y**(1)), 1)
eq2 = Eq(abs(x**(2)) + abs(y**(2)), 1)
eq3 = Eq(abs(x**(3)) +abs(y**(3)), 1)
eq4 = Eq(abs(x**(10)) +abs(y**(10)), 1)
eq5 = Eq(abs(x**(50)) +abs(y**(50)), 1)
eq6 = Eq(abs(x**(100)) +abs(y**(100)), 1)


p1 = plot_implicit(eq1, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p2 = plot_implicit(eq2, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p3 = plot_implicit(eq3, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p4 = plot_implicit(eq4, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p5 =plot_implicit(eq5, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))
p6 = plot_implicit(eq6, (x, -1, 1), (y, -1, 1), line_color='red', aspect_ratio=(1.,1.))


