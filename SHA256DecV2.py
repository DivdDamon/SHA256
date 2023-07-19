import hashlib
import re
pattern = re.compile(r'[0-9a-f]{64}')
out = 0

data = input("Input SHA256:\n")
datap = data.lower()

if (pattern.match(datap)).group() == datap:
        print("SHA256 Check Passed!")
        currnum = 0
        while -1 < currnum < 1000000:
                curr = (str(currnum)).zfill(6)
                if (hashlib.sha256(curr.encode())).hexdigest() != data:
                        currnum += 1
                else:
                        out = curr
                        break
else:
        print('Invalid Input!')
        print((pattern.search(datap)).group())

if out == 0:
        print('Not Found!')
else:
        print('SHA256 Found!\n'+out)
