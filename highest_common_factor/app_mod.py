# The Euclidean Algorithm for Greatest Common Factor
"""
The Euclidean Algorithm for finding GCD(A,B) is as follows:
- If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.
- If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
- Write A in quotient(Q)-remainder(R) form  -> A = B⋅Q + R
- Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
"""
import logging

module_logger = logging.getLogger("app_mod_logger")

# -------------------------------------------------------------


def gcf(a, b):
    logger = logging.getLogger("app_mod_logger")
    logger.info(f"Finding greatest common factor between {a} and {b}")
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a













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
