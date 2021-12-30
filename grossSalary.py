for _ in range(int(input())):
    a=int(input())
    if (a<1500):
        print(float(a+a*0.10+a*0.90))
    else:
        print(float(a+500+0.98*a))