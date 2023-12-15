def stack(number_list, operation, new_element=None):
    if operation == 'add':
        number_list.insert(0,new_element)
    elif operation == 'remove':
        if number_list:
            number_list.pop(0)
 
def queue(number_list, operation, new_element=None):
    if operation == 'add':
        number_list.append(new_element)
    elif operation == 'remove':
        if number_list:
            number_list.pop(0)
    return number_list

new_list = [1,2,3,4]
print("Adding new element to the stack")
stack(new_list,"add",0)
print(new_list)
print("Adding remove an element from stack")
stack(new_list,"remove")
print(new_list)
print("Adding new element to the queue")
queue(new_list,"add",5)
print(new_list)
print("Adding remove and element from the queue")
queue(new_list,"remove")
print(new_list)

