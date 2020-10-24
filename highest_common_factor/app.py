""" This program finds the highest common factor among a set of number
- starting with a list of 2 items then 4 then 10 until the logic is developed
- takes in only positive numbers in infinite range
- returns the hcf
- logic: calculate all factors of each number in separate lists. Then find the max of the common between those two lists
- (if time see to implement logic to omit unnecessary divisibility calculations.)

 """


x, y = 12, 144
smallest = min(x, y)

y_factors = [i for i in range(1, smallest+1) if y % i == 0]
x_factors = [i for i in range(1, smallest+1) if x % i == 0]

hcf = max(set(x_factors).intersection(set(y_factors)))

print(f"\n x_factors= {x_factors} \n \n y_factors = {y_factors} \n \n HCF = {hcf}")



# The Euclidean Algorithm for Greatest Common Factor
"""
The Euclidean Algorithm for finding GCD(A,B) is as follows:
- If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
- If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
- Write A in quotient remainder form (A = B⋅Q + R)
- Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
"""
# def gcf(x, y):
#     x, y = max(x, y), min(x, y)
#     while 1:
#         if x == 0:
#             return y
#             break
#         elif y == 0:
#             return x
#             break
#         else:
#             x, y = y, x%y


def gcf(a, b):
    a, b = max(a, b), min(a,b)
    while b:
        a, b = b, a%b
    return a

gcf = gcf(12, 100)
print(f"gcf = {gcf}")