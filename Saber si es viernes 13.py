
from datetime import datetime
def es_viernes_13():
    hoy = datetime.date.today()
    return hoy.weekday() == 4 and hoy.day == 13

print(es_viernes_13)
