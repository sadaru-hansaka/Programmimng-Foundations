#2^4 = 2*2*2*2 = 16
def power (num, pwr):
    if pwr == 0:
        return 1
    else:
        return (num * power(num, pwr-1))
    

answer = power(2,4)
print(answer)


#factorials

def factorials(fac):
    if fac == 0 :
        return 1
    else:
        return fac * factorials(fac-1)

result = factorials(4)
print(result)