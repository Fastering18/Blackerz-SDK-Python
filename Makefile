testall: test1 test2

test1:
    python -m coverage run test.py
    
test2:
    python -m blackerz_wrapper bot 777756503028400138
