def pow(base, exp):
    if exp == 0:
        return 1
    return base * pow(base,exp-1)

print(pow(2,3))