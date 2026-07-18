class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C(A, B):
    pass
C().show()

class D(B,A):
    pass
D().show()