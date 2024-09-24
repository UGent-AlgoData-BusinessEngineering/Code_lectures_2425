from Stack import Stack

stack = Stack()
    
for i in range(10):
    stack.push(i) # Push i to stack
    
while not stack.isEmpty():
    print(stack.pop(), end = " ") # Pop from stack
