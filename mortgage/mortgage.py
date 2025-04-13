"""
Description: A class meant to manage Mortgage options.
Author: Yizheng Chen
Date: March 10, 2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:

    def __init__(self, loan_amount: float, rate: str, frequency: str, amortization: int) -> None:
        
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        try:
            self.__rate = MortgageRate[rate]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")
        
        try:
            self.__frequency = PaymentFrequency[frequency]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")

        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization

    @property
    def loan_amount(self):
        """Accessor for the loan_amount attribute."""
        return self.__loan_amount
    
    @loan_amount.setter
    def loan_amount(self, value: float):
        """Set the loan amount for the mortgage.
        Args: 
            value (int): A non-negative integer representing the loan amount.
        Raises:
            ValueError: If the value provided is negative.
        """
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = value

    @property
    def rate(self):
        """Accessor for the rate attribute."""
        return self.__rate
    
    @rate.setter
    def rate(self, value: str):
        """Set the rate for the mortgage.
        Args: 
            value (str): A valid mortgage rate.
        Raises:
            ValueError: If the value not within the valid rates for mortgage.
        """
        try:
            self.__rate = MortgageRate[value]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")

    @property
    def frequency(self):
        """Accessor for the frequency attribute."""
        return self.__frequency
    
    @frequency.setter
    def frequency(self, value: str):
        """Set the frequency for the mortgage.
        Args: 
            value (str): A valid mortgage frequency.
        Raises:
            ValueError: If the value not within the valid frequency range for mortgage.
        """
        try:
            self.__frequency = PaymentFrequency[value]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")

    @property
    def amortization(self):
        """Accessor for the amortization attribute."""
        return self.__amortization
    
    @amortization.setter
    def amortization(self, value: int):
        """Set the amortization for the mortgage.
        Args: 
            value (int): A valid mortgage amortization.
        Raises:
            ValueError: If the value not within the valid amortization range for mortgage.
        """
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = value

    def calculate_payment(self) -> float:
        """Calculates the mortgage payment and returns it back to the user."""
        # 'i' is the interest rate
        i = self.__rate.value / self.__frequency.value
        # 'n' is the total number of payments
        n = self.__amortization * self.__frequency.value
        # 'P' is the principal loan amount
        P = self.__loan_amount
        payment = P * (i * (1 + i)**n) / ((1 + i)**n - 1)
        return round(payment, 2)
    
    def __str__(self) -> str:
        """String representation of Mortgage object."""
        rate_percentage = self.rate.value * 100  # Convert decimal rate to a percentage
        frequency_name = self.frequency.name.capitalize() # Capitalize the first letter
        return (f"Mortgage Amount: ${self.loan_amount:,.2f} Rate: {rate_percentage:.2f}%"
                f" Amortization: {self.amortization} Frequency: {frequency_name}"
                f" -- Calculated Payment: ${self.calculate_payment():,.2f}")
    
    def __repr__(self):
        """Representation of Mortgage object."""
        return (f"[{self.loan_amount}, " + 
                f"{self.rate.value}, " +
                f"{self.amortization}, " + 
                f"{self.frequency.value}]")