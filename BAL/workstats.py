import DAL.db_workstats as d

dta = d.DB_workstats()


def get_full_data():
    return dta.execute_select_query("Workstats")


def get_students():
    return dta.execute_select_query("Workstats", params={'IS_STUDENT': 'True'})


def get_data_by_province_name(name: str):
    return dta.execute_select_query("Workstats", params={'PROV_NAME': name})


def get_data_by_labour_force_status(lfs: int):
    return dta.execute_select_query("Workstats", params={'LFSSTAT': lfs})
