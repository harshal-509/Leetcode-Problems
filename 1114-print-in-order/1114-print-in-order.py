class Foo:
    def __init__(self):
        self.flag=0
        self.flag1=0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.flag=1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while(self.flag==0):
            pass    
        printSecond()
        self.flag1=1

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while(self.flag1==0):
            pass
        printThird()