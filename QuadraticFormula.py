import math 
  
  
# function for finding roots
def solve_quadratic( a, b, c): 
  
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # checking condition for discriminant
    if dis > 0: 
        root1 = (-b + sqrt_val)/(2 * a)
        root2 = (-b - sqrt_val)/(2 * a)
        return (root1, root2)
      
    elif dis == 0: 
        root = -b / (2 * a)
        return root
      
    # when discriminant is less than 0
    else:
        #Complex Roots
        root1 = (- b / (2 * a), " + i", sqrt_val) 
        root2 = (- b / (2 * a), " - i", sqrt_val) 
        return(root1, root2)
  

a = 1
b = 0
c = 1

# If a is 0, then incorrect equation
if a == 0: 
        print("Input correct quadratic equation") 
  
else:
    print(solve_quadratic(a, b, c))