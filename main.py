import functions as fn

def main():
    print("Welcome to the Malaysian Tax Input Program")
    
    user_data = {}
    
    while True:
        user_data['id'] = input("Enter your ID: ")
        ic_number = input("Enter your IC number (12 digits): ")
        password = input("Enter the last 4 digits of your IC number as password: ")
        
        if fn.verify_user(ic_number, password):
            print("User verified!")
            user_data['ic_number'] = ic_number
            break
        else:
            print("Invalid IC number or password. Please try again.")
    
    income = float(input("Enter your annual income: "))
    tax_relief = float(input("Enter your total tax relief amount: "))
    
    user_data['income'] = income
    user_data['tax_relief'] = tax_relief
    user_data['tax_payable'] = fn.calculate_tax(income, tax_relief)
    
    print(f"Your calculated tax payable is: {user_data['tax_payable']:.2f}")
    
    fn.save_to_csv(user_data)
    
    print("User data has been saved to CSV file.")
    
    choice = input("Do you want to read the tax records from the CSV file? (yes/no): ")
    if choice.lower() == 'yes':
        records = fn.read_from_csv()
        if records is not None:
            print(records)
        else:
            print("No records found.")

if __name__ == "__main__":
    main()
