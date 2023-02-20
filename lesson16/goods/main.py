from UnitGood import UnitGood
from WebGood import WebGood
from WeigthGood import WeigntGood

web_item = WebGood(5)
print("Итоговая стоимость цифровых товаров с учетом количества:", web_item.get_final_price())
unit_item = UnitGood(5)
print("Итоговая стоимость единичных товаров с учетом количества:", unit_item.get_final_price())
weight_item = WeigntGood(120, 2)
print("Итоговая стоимость весовых товаров с учетом количества:", weight_item.get_final_price())
