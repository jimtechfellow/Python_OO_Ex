from sales import cal_tax, cal_shipping
# import sales means import sales module as object.
import sales



from Package_Ex.Shopping.sales2 import cal_shipping2, cal_tax2

# "." means current folder level
# ".." means parent folder level
from ..Customer.contact import contact_customer

# do not use the import below!!!
# from sales import *

def call_module_v1():
    cal_shipping()
    cal_tax()

def call_module_v2():
    sales.cal_tax()
    sales.cal_shipping()

