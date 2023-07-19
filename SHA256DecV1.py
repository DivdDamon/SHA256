import hashlib
import re
pattern = re.compile(r'[0-9a-f]{64}')
out = 0

data = input("Input SHA256:\n")
datap = data.lower()

if pattern.match(datap) == datap:
        print("SHA256 Check Passed!")
        currnum = 0
        while -1 < currnum < 1000000 and found == 0:
                curr = (str(currnum)).zfill(6)
                if (hashlib.sha256(curr.encode())).hexdigest() != data:
                        currnum += 1
                else:
                        out = (hashlib.sha256(curr.encode())).hexdigest()
                        break
else:
        print('Invalid Input!')

if out == 0:
        print('Not Found!')
else:
        print('SHA256 Found!\n'+out)
