import csv
from pathlib import Path

# Loan Costs
loan_costs = [500, 600, 200, 1000, 450]

# Calculate and Print the number of loans from the list.
number_of_loans = len(loan_costs)
print (f"There are {number_of_loans} loans in the list")

# Calculate and Print the total value of the loans.
total_of_all_loans = sum(loan_costs)
print (f"The total value of all loans is {total_of_all_loans}")

# Calculate and Print the average loan amount.
average_loan_amount = (total_of_all_loans / number_of_loans)
print (f"The average loan amount is {average_loan_amount}")


# Loan Data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extract and Print the Future Value and Remaining Months on the loan.
future_value = loan.get ("future_value")
print (f"The Future Value is {future_value}")

remaining_months = loan.get ("remaining_months")
print (f"There are {remaining_months} months remaining")

# Calculate a "fair value" of the loan using 20% as the discount rate.
discount_rate = .20
present_value = future_value / (1 + discount_rate/12) ** remaining_months

# Decide if the present value represents the loan's fair value and print a reccomendation.  

loan_price = loan.get ("loan_price")

if present_value >= loan_price:
    print (f"The loan is worth at least the cost to buy it.")
elif present_value < loan_price:
    print (f"The loan is too expensive and not worth the price.")

# Loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Define a new function that will be used to calculate present value.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return (present_value)

# Use the function to calculate the present value of the new loan given below with an `annual_discount_rate` of 0.2.
annual_discount_rate = .2
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")
present_value = calculate_present_value(
    future_value, remaining_months, annual_discount_rate    
)

print(f"The present value of the loan is: {present_value}")

#Loan data set
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#Create an empty list called `inexpensive_loans`
inexpensive_loans = []

#Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for equity in loans:
    if equity["loan_price"] <= 500:
        inexpensive_loans.append(equity)

#Print the `inexpensive_loans` list
print (inexpensive_loans)

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
print("Writing Inexpensive Loans data to a CSV file...")

with open(output_path, "w") as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the header to the CSV file
    csvwriter.writerow(header)

    # Write the values of each dictionary inside of `inexpensive_loans` as a row in the CSV file.
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())
