def strings_formating():
    #strings formating 
    my_list=[4,5,6,7,8,9,0]
    variable = "my_string {0} {1} {2} {3}".format(my_list[0],my_list[1],my_list[2], my_list[3])
    print(variable)

def solo_learn_exploring_formats():
    b=5
    aa = "{x}, {y}".format(x=b**2, y=6)
    print(aa)
    
    a=min(
          [
           sum(
               [
                   11, 22
                   ]
               ), 
           max(
               abs(
                   -30)
               , 2)
           ]
          )
    print(a)

def abs_test():
    print(abs(-30))
    
strings_formating()
solo_learn_exploring_formats()
abs_test()