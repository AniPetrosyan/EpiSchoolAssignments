import math

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
 
    def area(self):
        s = (self.a + self.b + self.c)/2
        area = math.sqrt(s*((s-self.a)*(s-self.b)*(s-self.c)))
        return area
    

    def perimeter(self):
        return self.a + self.b + self.c


    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)
    

    def is_valid(self):
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a) :
            return False
        else:
            return True     
    

    def right_angled(self):
        if (self.a*self.a+self.b*self.b==self.c*self.c) or (self.c*self.c+self.b*self.b==self.a*self.a) or (self.a*self.a+self.c*self.c==self.b*self.b) :
            return "The triangle is right-angled." 
        else:
            return "The triangle is not right-angled."

test = Triangle(1,3,5)
print(test.is_valid())