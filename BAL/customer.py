import DAL.db as d

dta = d.DB()


def get_all_customers():
    return dta.execute_select_query("Customer")


def get_customer(_id: int):
    return dta.execute_select_query("Customer", params={'Id': _id})


def get_customer_by_last_name(_name: str):
    return dta.execute_select_query("Customer", params={'Last_Name': _name})


def get_customer_by_last_first_name(last: str, first: str):
    return dta.execute_select_query("Customer", params={'Last_Name': last, 'First_Name': first})
