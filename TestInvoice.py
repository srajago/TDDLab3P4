import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5, 'tax':0.178125},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10, 'tax': 0.35625 }}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCaluculateTotalSalesTax(invoice, products):
    invoice.totalSalesTax(products)
    assert invoice.totalSalesTax(products) == 0.2

def test_CanCalculateDoubleDiscount(invoice, products):
    invoice.totalDoubleDiscount(products)
    assert invoice.totalDoubleDiscount(products) == 11.24