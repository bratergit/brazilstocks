from typing import Union
import pandas as pd

def calculate_investment_value(
    principal: float,
    monthly_contribution: float,
    annual_interest_rate: float,
    years: int,
    compounding_frequency: int = 12
) -> float:
    """
    Calculate the final value of an investment with compound interest and monthly contributions.
    
    Args:
        principal (float): Initial investment amount
        monthly_contribution (float): Monthly contribution amount
        annual_interest_rate (float): Annual interest rate as decimal (e.g., 0.07 for 7%)
        years (int): Number of years to invest
        compounding_frequency (int): Number of times interest compounds per year (default: 12 for monthly)
    
    Returns:
        float: Final investment value
    """
    if annual_interest_rate == 0:
        # Simple case with no interest
        return principal + (monthly_contribution * 12 * years)
    
    # Convert annual rate to periodic rate
    periodic_rate = annual_interest_rate / compounding_frequency
    total_periods = years * compounding_frequency
    
    # Future value of principal with compound interest
    fv_principal = principal * (1 + periodic_rate) ** total_periods
    
    # Future value of monthly contributions (annuity)
    # Assuming contributions are made at the end of each month
    if periodic_rate != 0:
        fv_contributions = monthly_contribution * (((1 + periodic_rate) ** total_periods - 1) / periodic_rate)
    else:
        fv_contributions = monthly_contribution * total_periods
    
    return fv_principal + fv_contributions

def investment_growth_schedule(
    principal: float,
    monthly_contribution: float,
    annual_interest_rate: float,
    years: int,
    compounding_frequency: int = 12
) -> pd.DataFrame:
    """
    Generate a detailed schedule showing investment growth over time.
    
    Args:
        principal (float): Initial investment amount
        monthly_contribution (float): Monthly contribution amount
        annual_interest_rate (float): Annual interest rate as decimal
        years (int): Number of years to invest
        compounding_frequency (int): Compounding frequency per year
    
    Returns:
        pd.DataFrame: DataFrame with columns ['year', 'balance', 'total_contributions', 'interest_earned']
    """
    periodic_rate = annual_interest_rate / compounding_frequency
    schedule = []
    
    balance = principal
    total_contributions = principal
    
    for year in range(1, years + 1):
        # Calculate growth for this year
        for period in range(compounding_frequency):
            # Add interest
            interest = balance * periodic_rate
            balance += interest
            
            # Add monthly contribution (assuming monthly contributions)
            if period % (compounding_frequency // 12) == 0:  # Monthly contribution
                balance += monthly_contribution
                total_contributions += monthly_contribution
        
        interest_earned = balance - total_contributions
        
        schedule.append({
            'year': year,
            'balance': round(balance, 2),
            'total_contributions': round(total_contributions, 2),
            'interest_earned': round(interest_earned, 2)
        })
    
    return pd.DataFrame(schedule)
