from models.spiders import Spider
import fixtures.spiders as data


def get_all() -> list[Spider]:
    return data.get_all_fixtures()


def get_one(id: int) -> Spider | None:
    return data.get_one_fixture(id)


def create(spider: Spider) -> Spider:
    return data.create_fixture(spider)


def replace(id, spider: Spider) -> Spider:
    return data.replace_fixture(spider)


def modify(id, spider: Spider) -> Spider:
    return data.modify_fixture(spider)


def delete(id, spider: Spider) -> bool:
    return data.delete_fixture(id)
