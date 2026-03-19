from simple_math import (
    simple_add, simple_sub, simple_mult, simple_div, 
    poly_first, poly_second
)

def test_simple_add():
    assert simple_add(2, 3) == 5
    assert simple_add(-1, 1) == 0
    assert simple_add(0, 0) == 0

def test_simple_sub():
    assert simple_sub(5, 3) == 2
    assert simple_sub(3, 5) == -2
    assert simple_sub(0, 0) == 0

def test_simple_mult():
    assert simple_mult(2, 3) == 6
    assert simple_mult(-2, 3) == -6
    assert simple_mult(0, 5) == 0

def test_simple_div():
    assert simple_div(6, 2) == 3.0
    assert simple_div(5, 2) == 2.5

def test_poly_first():
    assert poly_first(1, 2, 3) == 5  # 2 + 3*1
    assert poly_first(0, 2, 3) == 2  # 2 + 3*0

def test_poly_second():
    assert poly_second(1, 2, 3, 4) == 9   # 2 + 3*1 + 4*1^2
    assert poly_second(2, 1, 2, 3) == 17  # 1 + 2*2 + 3*2^2
