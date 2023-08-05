import pytest
from modules.common.database import Database
from sqlite3 import OperationalError
from sqlite3 import IntegrityError
import datetime


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(5, "цукерки", "мятні", 15.25)
    sweets_qnt = db.select_product_qnt_by_id(5)
    db.delete_product_by_id(5)

    assert sweets_qnt[0][0] == 15.25


@pytest.mark.database
def test_product_insert1():
    db = Database()
    try:
        db.insert_product(32.76, "цукерки", "золотий ключик", 7)
    except IntegrityError as dberror:
        assert dberror.args[0] == "datatype mismatch"


@pytest.mark.database
def test_product_insert_error():
    db = Database()
    try:
        db.insert_product(6, "цукерки", "не існуючі", "три")
    except OperationalError as dberror:
        sweets = db.select_product_qnt_by_id(6)
        assert len(sweets) == 0
        assert dberror.args[0] == "no such column: три"


@pytest.mark.database
def test_product_insert_error_raises():
    db = Database()
    with pytest.raises(OperationalError) as dberror:
        db.insert_product(6, "цукерки", "не існуючі", "три")
    assert dberror.value.args[0] == "no such column: три"


@pytest.mark.database
def test_order_insert():
    db = Database()
    db.insert_orders(2, 1, 1, "2023-08-03")
    show = db.get_detailed_orders()
    db.delete_order_by_id(2)

    assert show[1][4] == "2023-08-03 00:00:00"


@pytest.mark.database
def test_order_insert_date_wrong_format():
    db = Database()
    db.insert_orders(2, 1, 1, "2023-25-15")
    show = db.get_detailed_orders()
    db.delete_order_by_id(2)

    print(show)
    assert show[1][4] == None
