a = input("Nhập số a: ")
n1 = int( "%s" % a )
print(n1)
n2 = int( "%s%s" % (a,a) )
print(n2)
n3 = int( "%s%s%s" % (a,a,a) )
print(n3)
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n4)

print ("Tổng cần tính là: ",n1+n2+n3+n4)
