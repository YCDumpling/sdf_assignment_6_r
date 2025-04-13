"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: Yizheng Chen
Date: March 10, 2024
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = {5, 10, 15, 20, 25, 30}

class MortgageRate(Enum):
    """
    An enumeration of mortgage rates.

    Values:
    - FIXED_5 = 0.0519
    - FIXED_3 = 0.0589
    - FIXED_1 = 0.0599
    - VARIABLE_5 = 0.0649
    - VARIABLE_3 = 0.0669
    - VARIABLE_1 = 0.0679
    """
    FIXED_5 = 0.0519
    FIXED_3 = 0.0589
    FIXED_1 = 0.0599
    VARIABLE_5 = 0.0649
    VARIABLE_3 = 0.0669
    VARIABLE_1 = 0.0679


class PaymentFrequency(Enum):
    """
    An enumeration of payment frequency.

    Values:
    - MONTHLY = 12
    - BI_WEEKLY = 26
    - WEEKLY = 52
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52