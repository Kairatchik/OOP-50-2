class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")
        super().method()

class C(A):
    def method(self):
        print("Method from class C")
        super().method()

class D(B, C):
    def method(self):
        print("Method from class D")
        super().method()

d = D()
d.method()

print("\nMRO (Method Resolution Order):")
print(D.mro())
