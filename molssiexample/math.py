"""
A file for executing math functions.
"""

def euler(n=10,maxitr=1000):

    euler_tmp = 0
    euler = 0
    for i in range(maxitr):
        denominator = 1
        for j in range(1,i+1):
            denominator = denominator*j
        euler_tmp += 1/denominator

        print(euler,euler_tmp,denominator)

        if i == 0:
            euler = round(euler_tmp,n)
        else:
            if euler == round(euler_tmp,n):
                break
            else:
                euler = round(euler_tmp,n)
    print("Euler's number up to %g digits is: %f" % (n,euler))


