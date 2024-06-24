class item_Employee:
    def __init__(self,name,ID):
        self.name = name
        self.id = ID

    def __eq__(self,other):
        return self.id == other.id

    def __gt__(self,other):
        return self.id > other.id

    def __lt__(self,other):
        return self.id < other.id

class Employee:
    def __init__(self,key = None):   # key is the object of item_Employee class
        self.key = key
        self.left = None
        self.right = None

    def inorder(self):
        employees_list = []

        if self.key is None:
            return None

        if self.left:
            employees_list += self.left.inorder()

        employees_list.append(self.key)

        if self.right:
            employees_list += self.right.inorder()

        return employees_list

    def find_Employee(self,key):   # key is the object of item_Employee class
        if self.key == key:
            return self.key

        if self.key < key:
            return self.left.find_Employee(key)
        else:
            return None

        if self.key > key:
            return self.right.find_Employee(key)
        else:
            return None

    def add_Employee(self,key):     # key is the object of item_Employee class
        # key = item_Employee(name,id)

        if self.key is None:
            self.key = key
            return

        if key < self.key:
            if self.left:
                self.left.add_Employee(key)
            else:
                self.left = Employee(key)

        if key > self.key:
            if self.right:
                self.right.add_Employee(key)
            else:
                self.right = Employee(key)

    def delete_Employee(self, key, curr):
        if self.key.id == curr and self.left is None and self.right is None:
            deleted_employee = self.key
            self.key = None
            return self,deleted_employee

        if key < self.key:
            if self.left:
                self.left, deleted_employee = self.left.delete_Employee(key, curr)
        elif key > self.key:
            if self.right:
                self.right, deleted_employee = self.right.delete_Employee(key, curr)
        else:
            if self.left is None:
                temp = self.right
                deleted_employee = self.key
                if self.key.id == curr:
                    self.key = temp.key
                    self.right = temp.right
                    self.left = temp.left
                    return self, deleted_employee

                return temp, deleted_employee

            if self.right is None:
                temp = self.left
                deleted_employee = self.key
                if self.key.id == curr:
                    self.key = temp.key
                    self.right = temp.right
                    self.left = temp.left
                    return self, deleted_employee

                return temp, deleted_employee

            node = self.right
            while node.left is not None:
                node = node.left
            self.key = node.key
            self.right, deleted_employee = self.right.delete_Employee(node.key, curr)
            return self, deleted_employee

        return self, deleted_employee

def count(node):
    if node is None:
        return 0
    
    return 1 + count(node.left) + count(node.right)

Employee_record = Employee()
operations_stack = []
while True:
    # print("\n")
    print("1. Print all Employees and their information (sorted by ascending id #")
    print("2. Find and display Employee information given the Employee id")
    print("3. Add a new Employee (along with all the information)")
    print("4. Delete an Employee given the id")
    print("5. Rollback")
    print("6. Exit")

    num = int(input("Enter a number : "))

    if num == 6:
        break

    elif num == 3:
        id = int(input("Enter Employee ID : "))
        name = input("Enter Employee name : ")
        item = item_Employee(name,id)
        Employee_record.add_Employee(item)
        operations_stack.append([3,item])

    elif num == 1:
        list_of_employees = Employee_record.inorder()
        if list_of_employees is None:
            print("Record is Empty")
        else:
            for i in list_of_employees:
                print("Employee Name : ",i.name,"   ID : ",i.id)

    elif num == 2:
        id = int(input("Enter Employee ID : "))
        item = item_Employee(None,id)
        emp = Employee_record.find_Employee(item)
        print("Employee Name : ",emp.name)
        print("Employee Id : ",emp.id)

    elif num == 4:
        id = int(input("Enter Employee ID : "))  
        item = item_Employee(None,id)
        s,deleted = Employee_record.delete_Employee(item,Employee_record.key.id)
        operations_stack.append([4,deleted])
    elif num == 5:
        # print(operations_stack)
        if operations_stack:
            i = operations_stack.pop()

            if i[0] == 3:
                Employee_record.delete_Employee(i[1],Employee_record.key.id)

            elif i[0] == 4:
                Employee_record.add_Employee(i[1])