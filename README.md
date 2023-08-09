# Simple ATM Implementation

## Build
### Environment
* Window 10
* Python 3.8

### Library
* shutil
* typing
* json

### Package install
```bash
pip install -r requirement.txt
```

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


## Run
```bash
python evaluate.py
```