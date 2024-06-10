import pandas as pd
import os

def verify_user(ic_number, password):
    if len(ic_number) != 12 or not ic_number.isdigit():
        return False
    return ic_number[-4:] == password

def calculate_tax(income, tax_relief):
    taxable_income = income - tax_relief
    if taxable_income <= 5000:
        tax = 0
    elif taxable_income <= 20000:
        tax = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax = (taxable_income - 20000) * 0.03 + 150
    elif taxable_income <= 50000:
        tax = (taxable_income - 35000) * 0.08 + 600
    elif taxable_income <= 70000:
        tax = (taxable_income - 50000) * 0.14 + 1800
    elif taxable_income <= 100000:
        tax = (taxable_income - 70000) * 0.21 + 4600
    else:
        tax = (taxable_income - 100000) * 0.24 + 10900
    return max(tax, 0)

def save_to_csv(data, filename='tax_data.csv'):
    df = pd.DataFrame([data])
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

def read_from_csv(filename='tax_data.csv'):
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    return None
