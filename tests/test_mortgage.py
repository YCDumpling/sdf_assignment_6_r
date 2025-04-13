"""
Description: A class used to test the Mortgage class.
Author: Yizheng Chen
Date: March 10, 2024
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    # Constructor
    def test_mortgage_class_raise_value_error_when_an_invalid_amount_is_used(self):
        # Arrange
        loan_amount = 0                         # FAIL
        rate = MortgageRate.FIXED_5.name             # PASS
        frequency = PaymentFrequency.MONTHLY.name    # PASS
        amortization = 5                        # PASS

        expected_error_output = "Loan Amount must be positive."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), expected_error_output)

    def test_mortgage_class_raise_value_error_when_an_invalid_rate_is_used(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = "FIXED_7"        # FAIL
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS

        expected_error_output = "Rate provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), expected_error_output)

    def test_mortgage_class_raise_value_error_when_an_invalid_frequency_is_used(self):
        # Arrange
        loan_amount = 5             # PASS
        rate = MortgageRate.FIXED_5.name            # PASS
        frequency = "MONTHLY_TEST"  # FAIL
        amortization = 5            # PASS

        expected_error_output = "Frequency provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), expected_error_output)

    def test_mortgage_class_raise_value_error_when_an_invalid_amortization_is_used(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 0        # FAIL

        expected_error_output = "Amortization provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)

        # Assert
        self.assertEqual(str(context.exception), expected_error_output)

    def test_mortgage_class_mutator_properly_sets_attribute(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        expected_loan_amount = 5
        expected_rate = 0.0519
        expected_frequency = 12
        expected_amortization = 5
        # Act
        mortgage.loan_amount = loan_amount
        mortgage.rate = rate
        mortgage.frequency = frequency
        mortgage.amortization = amortization

        # Assert
        self.assertEqual(mortgage.loan_amount, expected_loan_amount)
        self.assertEqual(mortgage.rate.value, expected_rate)
        self.assertEqual(mortgage.frequency.value, expected_frequency)
        self.assertEqual(mortgage.amortization, expected_amortization)

    # Loan Amount Attribute
    def test_mortgage_class_loan_amount_mutator_raise_value_error_when_entering_a_negative_value(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        # Act & Assert
        with self.assertRaises(ValueError):
            mortgage.loan_amount = -100

    def test_mortgage_class_loan_amount_mutator_raise_value_error_when_entering_a_zero_value(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)

        # Act & Assert
        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0

    def test_mortgage_class_loan_amount_mutator_when_entering_a_valid_positive_value(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected_loan_amount = 100.00

        # Act
        mortgage.loan_amount = expected_loan_amount

        # Assert
        self.assertEqual(mortgage.loan_amount, expected_loan_amount)

    # # Rate Attribute
    def test_mortgage_class_rate_mutator_when_entering_a_valid_mortgage_rate(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        valid_mortgage_rate = PaymentFrequency.FIXED_3.name
        expected_rate = 0.0589
        # Act 
        mortgage.rate = valid_mortgage_rate
            
        # Assert
        self.assertEqual(mortgage.rate.value, expected_rate)

    def test_mortgage_class_rate_mutator_raise_value_error_when_entering_a_invalid_mortgage_rate(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        invalid_mortgage_rate = "FIXED_7"

        # Act & Assert
        with self.assertRaises(ValueError):
            mortgage.rate = invalid_mortgage_rate
        
    # # Frequency Attribute
    def test_mortgage_class_frequency_mutator_when_entering_a_valid_mortgage_frequency(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        valid_mortgage_frequency = PaymentFrequency.BI_WEEKLY.name
        excepted_result = 26
        # Act & 
        mortgage.frequency = valid_mortgage_frequency
            
        # Assert
        self.assertEqual(mortgage.frequency.value, excepted_result)

    def test_mortgage_class_frequency_mutator_raise_value_error_when_entering_a_invalid_mortgage_frequency(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        invalid_mortgage_frequency = "BI_WEEKLYZ"

        # Act & Assert
        with self.assertRaises(ValueError):
            mortgage.rate = invalid_mortgage_frequency
        
    # # Amortization Attribute
    def test_mortgage_class_amortization_mutator_when_entering_a_valid_mortgage_amortization(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        valid_mortgage_amortization = 30

        # Act & 
        mortgage.amortization = valid_mortgage_amortization
            
        # Assert
        self.assertEqual(mortgage.amortization, valid_mortgage_amortization)

    def test_mortgage_class_amortization_mutator_raise_value_error_when_entering_a_invalid_mortgage_amortization(self):
        # Arrange
        loan_amount = 5         # PASS
        rate = MortgageRate.FIXED_5.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name  # PASS
        amortization = 5        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        invalid_mortgage_amortization = 31

        # Act & Assert
        with self.assertRaises(ValueError):
            mortgage.amortization = invalid_mortgage_amortization
        
    # # Mortgage Caclulation
    def test_mortgage_class_mortgage_calculation_method(self):
        # Arrange
        loan_amount = 682912.43 # PASS
        rate = MortgageRate.FIXED_1.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 10        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected_result = 7578.3

        # Act 
        output_result = mortgage.calculate_payment() 
            
        # Assert
        self.assertEqual(expected_result, output_result)
            

    # # __str__ Tests
    def test_mortgage_class__str__monthly_payment(self):
        # Arrange
        loan_amount = 682912.43 # PASS
        rate = MortgageRate.FIXED_3.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 30        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected_str = "Mortgage Amount: $682,912.43 Rate: 5.89% Amortization: 30 Frequency: Monthly -- Calculated Payment: $4,046.23"
        
        # Act 
        output_result = str(mortgage)
            
        # Assert
        self.assertEqual(expected_str, output_result)
        
        # # __str__ Tests
    def test_mortgage_class__str__biweekly_payment(self):
        # Arrange
        loan_amount = 682912.43 # PASS
        rate = MortgageRate.FIXED_3.name        # PASS
        frequency = PaymentFrequency.BI_WEEKLY.name   # PASS
        amortization = 30        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected_str = "Mortgage Amount: $682,912.43 Rate: 5.89% Amortization: 30 Frequency: Bi_weekly -- Calculated Payment: $1,866.60"
        
        # Act 
        output_result = str(mortgage)
            
        # Assert
        self.assertEqual(expected_str, output_result)

    def test_mortgage_class__str__weekly_payment(self):
        # Arrange
        loan_amount = 682912.43 # PASS
        rate = MortgageRate.FIXED_3.name        # PASS
        frequency = PaymentFrequency.WEEKLY.name   # PASS
        amortization = 30        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected_str = "Mortgage Amount: $682,912.43 Rate: 5.89% Amortization: 30 Frequency: Weekly -- Calculated Payment: $933.11"
        
        # Act 
        output_result = str(mortgage)
            
        # Assert
        self.assertEqual(expected_str, output_result)
        
    # __repr__ Tests
    def test_mortgage_class_test_valid__repr__(self):
        # Arrange
        loan_amount = 682912.43 # PASS
        rate = MortgageRate.FIXED_3.name        # PASS
        frequency = PaymentFrequency.MONTHLY.name   # PASS
        amortization = 30        # PASS
        mortgage = Mortgage(loan_amount, rate, frequency, amortization)
        expected_str = "[682912.43, 0.0589, 30, 12]"
        
        # Act 
        output_result = repr(mortgage)
            
        # Assert
        self.assertEqual(output_result, expected_str)
        