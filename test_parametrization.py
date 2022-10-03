import pytest

@pytest.mark.parametrize("num,output",[(1,11),(2,22),(3,34),(4,45),(5,55)])
def test_multiplication(num,output):
    assert num*11 == output
