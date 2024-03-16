from api.models.spiders import Spider

_spiders = [
    Spider(id=1,
           code='1',
           name='First spider',
           tag='some tag'),
    Spider(id=2,
           code='2',
           name='Second spider',
           tag='some tag'),
]


def get_all_fixtures() -> list[Spider]:
    """Return all spiders"""
    return _spiders


def get_one_fixture(id: int) -> Spider | None:
    """Return one spider"""
    for _spider in _spiders:
        if _spider.id == id:
            return _spider
    return None


def create_fixture(spider: Spider) -> Spider:
    """Add a spider"""
    return spider


def modify_fixture(spider: Spider) -> Spider:
    """Partially modify a spider"""
    return spider


def replace_fixture(spider: Spider) -> Spider:
    """Completely replace a spider"""
    return spider


def delete_fixture(name: str):
    """Delete a spider; return None if it existed"""
    return None
