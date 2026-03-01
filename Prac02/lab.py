class Par():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def pr(self,a,b):
        print(a+b)
    
class Ch(Par):
    super().__init__(a,b)
    super().pr(a,b)

