from Stacks import queue, stack
s = stack.Stack()
q = queue.Queue()
# Task 1

for i in range(1, 11):
    s.push(i)
# print(s.show_stack())
while s.size() != 0:
    print(s.pop())
# while not s.isEmpty():
#     print(s.pop())
print('-'*25)
# Task 3
s.push('A')
s.push('Z')
s.push('V')
print(s.get_from_stack('Z'))
print(s)
print('-'*25)
q.enqueue('Vasilii')
q.enqueue('Petro')
q.enqueue('Vitalii')
print(q.get_from_stack('Vasilii'))
print(q)








