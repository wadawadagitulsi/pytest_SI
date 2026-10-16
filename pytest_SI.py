from SI import simpleint

def test_calculate_SI():
    assert simpleint(1000,4,2) == 80

def test_calculate_zero():
        assert simpleint(1000,5,0) == 0
