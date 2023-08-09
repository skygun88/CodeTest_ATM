# Simple ATM Implementation

## Build
### Environment
* Window 10
* Python 3.8

### Library
* typing

### Package install
```bash
pip install -r requirements.txt
```

## Files
* `ATM.py`: Implementation of ATM controller class
* `Card.py`: Implementation of Card class
* `db_ori.json`: Json style test Banck DB which contains PIN, balance
* `main.py`: Main loop to control ATM
* `evaluate.py`: Code to test our ATM controller implemenation based on 10 testcases
* `remove_output.py`: Code to remove dummy output files in `Test` directory
* `Test`: Directory which contains 10 testcases
    * `Test/{case_num}/input.txt`: Text file contains STDIN of the testcase
    * `Test/{case_num}/answer.txt`: Text file contains desired STOUT of the testcase
    * `Test/{case_num}/db_ans.txt`: Json file contains desired result db file of the testcase
    * `Test/{case_num}/output.txt`: Text file contains STOUT of the testcase (will be generated after executing test code)
    * `Test/{case_num}/db_out.txt`: Json file contains actual result db file of the testcase(will be generated after executing test code)
    
## Testcase
### Case01 - Invalid PIN
Check whether our ATM detects the card which has invalid PIN
### Case02 - Balance (1)
Check whether our ATM shows the balance of current user whose PIN is "bear230809"
### Case03 - Balance (2)
Check whether our ATM shows the balance of current user whose PIN is "codingtest777"
### Case04 - Deposit (1)
Check whether our ATM desposits \$500 on current user whose PIN is "robotics230809"
### Case05 - Deposit (2)
Check whether our ATM desposits successively \$1000 and \$500 on current user whose PIN is "geonkim"
### Case06 - Withdraw (1)
Check whether our ATM withdraws \$700 on current user whose PIN is "bear230809"
### Case07 - Withdraw (2)
Check whether our ATM prevents to withdraw the \$1100 on current user whose PIN is "bear230809"
### Case08 - Withdraw (3)
Check whether our ATM withdraws successively \$300, and \$1000 on current user whose PIN is "codingtest777"
### Case09 - Combined (1)
Check whether our ATM desposits \$500 and withdraws \$1400 on current user whose PIN is "robotics230809"
### Case10 - Combined (2)
Check whether our ATM desposits \$1500 and prevents to withdraw \$4500 on current user whose PIN is "geonkim"

## Run the test code
```bash
python evaluate.py
```