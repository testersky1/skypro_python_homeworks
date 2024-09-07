from employee import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "skyPro"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "Danil"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "DanilTarkhanov", "A")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "DanilTarkhanov"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "A"


def test_get_employee_by_id():
    name = "Danil"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "DanilTarkhanov", "Al")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "DanilTarkhanov"
    assert get_info["lastName"] == "Al"


def test_change_employee_info():
    name = "Danil"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "DanilTarkhanov", "Ale")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Ale2", "test2@mail.ru")
    assert update["id"] == id_employee
    assert update["email"] == "test2@mail.ru"
    assert update["isActive"] == True