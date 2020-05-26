def isPrime(n):
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            return False
    
    return True