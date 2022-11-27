# problem 72
# class A:
#     def f (self):
#         return self.g()
#     def g (self):
#         return 'A'

# class B(A):
#         def g(self):
#             return 'B'
# a = A()
# b = B()

# print(a.f(),b.f())
# print(a.g(),b.g())

#problem 73
# try:
#     print ('a')
# except:
#     print ('b')
# else:
#     print ('c')
# finally:
    # print ('d')

# problem 74
try:
    print ('a')
    raise Exception ('doom')
