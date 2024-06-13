from privilegios import *

privilegios = ["ver usuarios"]
admin = Admin('yo','yo mismo',privilegios)

admin.ver_privilegios()