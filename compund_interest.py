def compound_interest_calculator(P, r, n, t):
    n1=float(n); t1=float(t)
    A=P*(1 + r/n)**(n1*t1)
    return A
print(compound_interest_calculator(1000, 0.05, 12, 5))