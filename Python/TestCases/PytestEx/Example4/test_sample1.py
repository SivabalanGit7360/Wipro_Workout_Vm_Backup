import pytest

@pytest.fixture
def supply_aa_bb_cc():
    aa = 25
    bb = 35
    cc = 45
    return (aa,bb,cc)

def test_comparewithaa(suplly_aa_bb_cc):
    zz = 35
    assert supply_aa_bb_cc[0] == zz
    
def test_comparewithaa(suplly_aa_bb_cc):
    zz = 35
    assert supply_aa_bb_cc[1] == zz
    
def test_comparewithaa(suplly_aa_bb_cc):
    zz = 35
    assert supply_aa_bb_cc[2] == zz