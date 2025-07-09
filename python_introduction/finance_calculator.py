monthly_income_str = input ("Enter your monthly income: ")
monthly_income = float(monthly_income_str)
monthly_expenses_str = input ("Enter your monthly expenses: ")
monthly_expenses = float(monthly_expenses_str)
monthly_savings = monthly_income - monthly_expenses
annual_interest_rate = 0.05
annual_savings_before_interest = monthly_savings * 12
interest_earned = annual_savings_before_interest * annual_interest_rate
projected_annual_savings = annual_savings_before_interest + interest_earned
print(f"Your projected annual savings, including interest, is: ${projected_annual_savings:.2f}")