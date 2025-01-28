def power(a, b):
    ans =1
    for i in range(b):
        ans = ans * a

    return ans

if __name__=="__main__":
    a = 2
    b = 5

    print(power(a,b))