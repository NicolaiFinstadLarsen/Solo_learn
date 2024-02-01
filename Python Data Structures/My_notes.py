
class working_with_strings():
    
    print("\n")
    print("CLASS: working with string")
    print("\n")
    
    print("\n")
    print("Last_char")
    print("\n")
    
    def last_char():
        x = "Hello"
        print(x[-1])  
    last_char()
    
    print("\n")
    print("Looping")
    print("\n")
    
    def looping():
        x = "Hello"
        for i in x:
            print(i)
    looping()
    
    print("\n")
    print("Checking_string")
    print("\n")
    
    def checking_string():
        x = "I love Python"
        if "love" in x:
           print('Yes "love" is there')
        if "elefant" not in x:
            print('No "elefant" is not there')
    checking_string()
    
    print("\n")
    print("String_functions")
    print("\n")
    
    def string_functions():
        x = "This is some text"
    
        print(x.count("s"))
        print(x.upper())
        print(x.lower())
        print(x.replace("some text", "awesome"))
        print(len(x)) 
    string_functions()
    
    print("\n")
    print("")
    print("\n")


class lists():
    print("\n")
    print("CLASS: Lists")
    print("\n")

    print("\n")
    print("List_in_list")
    print("\n")
    
    
    def list_in_list():
        m = [
        [1,2,3],
        [4,5,6]
        ]
        
        print(m[1][2])
        print(m[0][2]+m[1][2]) #printer 3 + 6
        
    list_in_list()
    
    print("\n")
    print("Gange_alle_elementer")
    print("\n")
    
    def gange_alle_elementer():
        liste=[1,2,3,4,5]
        res = 1  #husk å ikke begynne på 0 når man ganger noe...
        for n in liste:
            res *= n
        print(res)
    gange_alle_elementer()
    
    print("\n")
    print("Sortering")
    print("\n")
    
    def sortering():
        x = [2, 4, 6, 8]
        x.reverse()
        print(x)
        
        x.sort()
        print(x)
        
        x.sort(reverse=True)
        print(x)
        
        print(min(x))
        print(max(x))
        
    sortering()
    
    print("\n")
    print("List_comprehansion")
    print("\n")
    
    def list_comprehansion():
       # List comprehensions are a useful way of 
       #quickly creating lists whose contents obey a rule.
       cubes = [i**3 for i in range(5)]

       print(cubes)
    list_comprehansion()
    
    print("\n")
    print("if in comprehansion")
    print("\n")
    
    def if_in_comprehansion():
        
        evens=[i**2 for i in range(10) if i**2 % 2 == 0]

        print(evens)
        
    if_in_comprehansion()
    
    
class dictionaries_tuples_sets():
    
    print("\n")
    print("CLASS: Dictionaries")
    print("\n")


    def test():
        print("\n")
        print("Test")
        print("\n")
        
        my_dict = {"nico":42, "anders":25, "thomas":50}
        print(my_dict["thomas"],
              my_dict["anders"])
    test()
    
    def bools():
        nums = {
        1: "one",
        2: "two",
        3: "three",
        }
        print(1 in nums)
        print("three" in nums)
        print(4 not in nums)
    bools()
    
    
    print("\n")
    print("UNDERCLASS: Tuples")
    print("\n")
    
    def feks():
        words = ("spam", "eggs", "sausages",)
        print(words[0])
    feks()
    
    print("\n")
    print("UNDERCLASS: Tuples unpacking")
    print("\n")
    
    def feks2():
        numbers = (1, 2, 3, 4)
        a, b, c, d = numbers #assign variables til tuple variablene
        print(a)
        print(b)
        print(c)
        print(numbers)
        print(d)
    feks2()
    
    print()
    
    def stjerne():
        #tar alle variabler som er "til overs"
        a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
        print(a)
        print(b)
        print(c)
        print(d)
    stjerne()
    
    print("\n")
    print("UNDERCLASS: Sets")
    print("\n")
    
    def feks3():
        #kan ikke inneholde duplikate verdier.
        num_set = {1, 2, 3, 4, 5}

        print(3 in num_set)
        
        num_set.add(-7)
        num_set.remove(2)
        print(num_set)
    feks3()
    
    print()
    
    def operator():
    # =============================================================================
    #         Sets can be combined using mathematical operations.
    #         The union operator | combines two sets to form a new one containing items in either.
    #         The intersection operator & gets items only in both.
    #         The difference operator - gets items in the first set but not in the second.
    #         The symmetric difference operator ^ gets items in either set, but not both.
    # =============================================================================
        first = {1, 2, 3, 4, 5, 6}
        second = {4, 5, 6, 7, 8, 9}
        
        print(first | second)
        print(first & second)
        print(first - second)
        print(second - first)
        print(first ^ second)
    

    
    # =============================================================================
    # Data Structures
    # 
    # 
    # As we have seen in the previous lessons, Python supports the following collection types: Lists, Dictionaries, Tuples, Sets.
    # 
    # Here are some general guidelines for choosing the correct data structure:
    # - Use a dictionary, when you need a logical association between a key:value
    # - Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
    # - Use a set if you need uniqueness for the elements.
    # - Use tuples when your data cannot/should not change.
    # Many times, a tuple is used in combination with a dictionary, for example, a tuple can represent a key, because it's immutable
    # =============================================================================
    operator() # calling fuc here to inclunde comment section in class


class user_defined_data_structures():
    print()
    print("CLASS user-defined data structures")
    print()
    
    def stack():
        
        print()
        print("UNDERCLASS stack")
        print()
        
        #FILO, first in, last out
        
        class Stack:
            def __init__(self):
                self.items = []  
          
            def is_empty(self):
                return self.items == []
          
            def push(self, item):
                self.items.insert(0, item)
            
            def pop(self):
                return self.items.pop(0)
            
            def print_stack(self):
                print(self.items)
        
        s = Stack()
        s.push('a')
        s.push('b')
        s.push('d')
        s.print_stack()
        
        s.pop()
        s.print_stack()
    
    stack()
    
    print()
    
    def queue_ex():
        
        print()
        print("UNDERCLASS queue")
        print()
        
        #FIFO, first in, first out
        
        class Queue:
            def __init__(self):
                self.items = []
        
            def is_empty(self):
                return self.items == []
        
            def enqueue(self, item):
                self.items.insert(0, item)
        
            def dequeue(self):
                return self.items.pop()
        
            def print_queue(self):
                print(self.items)
        
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('42')
        q.print_queue()

        q.dequeue()
        q.print_queue()
        
        
    queue_ex()
    
    def linked_list_ex():
        
        print()
        print("UNDERCLASS Linked List")
        print()
        
        #NO IDEA ?!?!?!
        
        class Node:
            def __init__(self, data, next):
                self.data = data
                self.next = next
    
        class LinkedList:
            def __init__(self):
                self.head = None
            
            def add_at_front(self, data):
                self.head = Node(data, self.head)      
        
            def add_at_end(self, data):
                if not self.head:
                    self.head = Node(data, None)
                    return
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.next = Node(data, None)
        
            def get_last_node(self):
                n = self.head
                while(n.next != None):
                    n = n.next
                return n.data
        
            def is_empty(self):
                return self.head == None
        
            def print_list(self):
                n = self.head
                while n != None:
                    print(n.data, end = " => ")
                    n = n.next
                print()
    
    
        s = LinkedList()
        s.add_at_front(5)
        s.add_at_end(8)
        s.add_at_front(9)
        
        s.print_list()
        print(s.get_last_node())

    linked_list_ex()
    
    def graphs_ex():
        
        print()
        print("UNDERCLASS Graphs")
        print()
        
        # Også ingen ide ?!?!
        
        class Graph(): 
            def __init__(self, size): 
                self.adj = [ [0] * size for i in range(size)]
                self.size = size 
            
            def add_edge(self, orig, dest): 
                if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
                    print("Invalid Edge") 
                else: 
                    self.adj[orig-1][dest-1] = 1 
                    self.adj[dest-1][orig-1] = 1 
                
            def remove_edge(self, orig, dest): 
                if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
                    print("Invalid Edge") 
                else: 
                    self.adj[orig-1][dest-1] = 0 
                    self.adj[dest-1][orig-1] = 0 
                    
            def display(self): 
                for row in self.adj: 
                    print() 
                    for val in row: 
                        print('{:4}'.format(val),end="") 
        
        #a sample Graph 
        G = Graph(4) 
        G.add_edge(1, 3) 
        G.add_edge(3, 4)
        G.add_edge(2, 4)
        G.display()
    
    graphs_ex()