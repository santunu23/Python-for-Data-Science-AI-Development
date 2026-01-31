list1=["disco",10,1.2]
list1[0]="hard rock"
print(list1)

A=["hard rock",10,1.2]
B=A
print("A:",A)
print("B:",B)
print('B[0]',B[0])
A[0]="banana"
print("A[0]:",B[0])


A=(1,2,3,4,5)
print(A[1:4])

A=[1,2,3] + [1,1,1]
print(A)

A = [1]
A.append([2, 3, 4, 5])
print(len(A))

A=["Joy","Sen","Joy",2,1]
print(A)
B=set(A)
print(B)