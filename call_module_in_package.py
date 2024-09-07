import Package_Ex.Shopping.sales
from Package_Ex.Shopping import sales


# think sales as a object
# subpackage call example is in : Shopping/call_sales_and_contact_module.py
def v1():
    Package_Ex.Shopping.sales.cal_tax()

def v2():
    sales.cal_tax()

