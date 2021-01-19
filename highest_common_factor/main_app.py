""" This program finds the highest common factor among a set of number
- starting with a list of 2
- returns the hcf
- logic: calculate all factors of each number in separate lists. Then find the max of the common between those two lists
- (if time, see to implement logic to omit unnecessary divisibility calculations.)

 """

import logging.config
import app_mod
import logconfig

logging.config.dictConfig(logconfig.dictConfiguration)
logger = logging.getLogger("app_logger")
logger.info("Program has started")

try:
    gcf = app_mod.gcf('12', 144)
    print(f"gcf = {gcf}")
except Exception as err:
    logger.exception("An error occurred when function was called")
else:
    logger.info("Function ran successfully")


logger.info("Program has ended")






# x, y = 12, 144
# smallest = min(x, y)
#
# y_factors = [i for i in range(1, smallest+1) if y % i == 0]
# x_factors = [i for i in range(1, smallest+1) if x % i == 0]
#
# hcf = max(set(x_factors).intersection(set(y_factors)))
#
# print(f"\n x_factors= {x_factors} \n \n y_factors = {y_factors} \n \n HCF = {hcf}")



# The Euclidean Algorithm for Greatest Common Factor
"""
The Euclidean Algorithm for finding GCD(A,B) is as follows:
- If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
- If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
- Write A in quotient(Q)-remainder(R) form  -> A = B⋅Q + R
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


# def greatest_common_factor(a, b):
#     no_1, b= max(no1, no2), min(no1, no2)
#     while b:
#         a, b = b, a%b
#     return a
#
# gcf = gcf(12, 144)
# print(f"gcf = {gcf}")