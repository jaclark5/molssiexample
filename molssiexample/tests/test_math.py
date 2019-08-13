import molssiexample as me
import pytest

def test_euler_1():

    assert me.math.euler(n=1) == 2.7

def test_euler_2():

    assert me.math.euler(n=2) == 2.72

def test_euler_3():

    assert me.math.euler(n=3) == 2.718

# OOOOOR

@pytest.mark.parametrize('n, answer', [(0,2),(1,2.7),(2,2.72),(3,2.718)])
def test_euler(n, answer):
    assert me.math.euler(n) == answer

# OOOOOR

@pytest.mark.parametrize('n, answer', [(0,2),(1,2.7),(2,2.72),(3,2.718)])
def test_euler(n, answer):
    assert me.math.euler(n) == pytest.approx(answer,abs=1e-6)

def test_euler_failures():

    with pytest.raises(ValueError) as exc:
        me.math.euler(n=-1)
    
    assert "positive int" in str(exc.value)

def test_find_pi():
    assert me.math.find_pi(maxitr=1e+4) == pytest.approx(3.14,abs=1e-1)
