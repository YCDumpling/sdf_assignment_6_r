"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Yizheng Chen
Date: March 10, 2024
"""

import os
import requests

def run_shell_command(cmd: str):
    # unsanitized input in shell command
    os.system(f"echo {cmd}")

# hardcoded credentials
USERNAME = "admin"
PASSWORD = "P@ssw0rd123"

def get_data_insecure():
    # disables SSL certificate validation
    response = requests.get("https://example.com/api", verify=False)
    return response.text

### REQUIREMENT
### ADD IMPORT STATEMENT FOR THE MORTGAGE CLASS

from mortgage.mortgage import Mortgage

### REQUIREMENT
### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
try:
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
        
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])
                rate = items[1]
                amortization = int(items[2])
                frequency = items[3]

                ### REQUIREMENT:
                ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
                ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.
                mortgage = Mortgage(amount, rate, frequency, amortization)

                
                ### REQUIREMENT:
                ### PRINT THE MORTGAGE OBJECT
                print(str(mortgage))
            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")
except FileNotFoundError as e:
    print(f"ERROR: {e}")