# dic={
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }

# n = int(input()) #87
# arr = []

# ones = 1
# while True:
#     if n == 0:
#         break
#     arr.append((n%10) *ones )
#     ones*=10
#     n = int(n/10)

# def funny(n):
#     if 1 <= n < 5:

#     elif 5<= n <10:

#     elif 10 <= n < 50:

#     elif 50<= n < 100:

#     elif 100<= n < 500:

#     elif 500<= n <1000:

#     elif n==1000:


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print(pwd_context.verify("string", "$2b$12$sTdfwZm3/2rkGh0jVAOhiOc.8yOh2n1cmp0NK2jklma1oK/lGe3PK"))
# print(pwd_context.hash("Sivasathwik"))
        
        
