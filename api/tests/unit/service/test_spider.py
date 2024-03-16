from api.models.spiders import Spider
from api.service.spiders import create, get_one

sample = Spider(id=1,
           code='1',
           name='First spider',
           tag='some tag')

def test_create():
    resp = create(sample)
    assert resp == sample


def test_get_exists():
    resp = get_one("1")
    assert resp == sample


def test_get_missing():
    resp = get_one("1000")
    assert resp is None
