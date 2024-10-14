'''import re
sample_list=['3123456789123456','9123-4567-8912-3456','5123456789123456','7123 - 4567-8912 -3456','44244x4424442444','0525362587961578']
pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
for eachnumber in sample_list:
    result = re.match(pattern, eachnumber)
    if result:
        print(eachnumber+"->"+"Valid card")
    else:
        print(eachnumber+"->"+"Invalid card")'''

cardNo = '5196081888500645'
nDigits = len(cardNo)
nSum = 0
isSecond = False
     
for i in range(nDigits - 1, -1, -1):
    d = ord(cardNo[i]) - ord('0')
 
    if (isSecond == True):
        d = d * 2
  
    # We add two digits to handle
    # cases that make two digits after
    # doubling
    nSum += d // 10
    nSum += d % 10
  
    isSecond = not isSecond
if (nSum % 10 == 0):
	print('true')
else:
	print('false')

 
