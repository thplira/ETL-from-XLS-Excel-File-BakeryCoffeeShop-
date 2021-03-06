from python_files.utils import *
from python_files import import_data

path_file = "input_files/exemple file.xls"
data_captured = import_data.import_from_xls(path_file)
file1_output = open('output_files/Sales by Product.csv', 'w') # Create a new CSV File for Sale per Product
file2_output = open('output_files/Payment Info by Sales.csv', 'w') # Create a new CSV File for Payments Info per Sale

all_payments = data_captured[0]
all_sales = data_captured[1]

column_description1 = "item_code;item_description;item_type;emission;hour;document;\
item_quantity;item_price;item_descount;item_addition;item_final_value\n"
column_description2 = "emission;hour;document;payment;payment_value\n"
file1_output.write(column_description1)
file2_output.write(column_description2)

for _ in all_sales:
    
    line = f"{_[0]};{_[1]};{_[2]};{_[3]};{_[4]};{_[5]};{brazil_currency_notation(_[6])};\
        {brazil_currency_notation(_[7])};{brazil_currency_notation(_[8])};\
        {brazil_currency_notation(_[9])};{brazil_currency_notation(_[10])}\n"
    file1_output.write(line)

for _ in all_payments:
    
    line = f"{_[0]};{_[1]};{_[2]};{_[3]};{brazil_currency_notation(_[4])}\n"
    file2_output.write(line)

file1_output.close()
file2_output.close()