import random

# class to create the node
class Node:
    def __init__(self,data):
        self.val=data
        self.nref=None
        self.pref=None

# doubly linked list class
class ExtendedInt:
    def __init__(self):
        self.head=None
        self.length=0

    # our required output will be always stored in reversed order in the linked list
    # thus we will print the LL in reverse order 
    def print_LL_in_reverse(self):
        n1=self.head
        if n1 is None:
            print("LL is empty")
            return
        if n1.nref is None: 
            print(n1.val)
        else:
            while n1.nref is not None:
                n1=n1.nref
            while n1 is not None:
                print(n1.val,end="")
                n1=n1.pref
            print()

    # method to add node at beginning
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
    
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
        self.length+=1

    # method to add node at end
    def add_end(self,data):
        new_node=Node(data)
        n1=self.head
        if self.head is None:
            self.head=new_node
        else:
            while n1.nref is not None:
                n1=n1.nref
            new_node.pref=n1
            n1.nref=new_node
        self.length+=1

    # method to delete node at end
    def del_end(self):
        n=self.head
        while n.nref is not None:
            n=n.nref
        n.pref.nref=None
        self.length=self.length - 1

    def __add__(self,other):
        l1=self.head
        l2=other.head
        add_LL=ExtendedInt()
        carry=0

        while l1 is not None or l2 is not None or carry!=0:
            digit1=l1.val if l1 is not None else 0
            digit2=l2.val if l2 is not None else 0

            sum=digit1 + digit2 + carry
            digit=sum%10
            carry=sum//10
            add_LL.add_end(digit)

            l1=l1.nref if l1 is not None else None
            l2=l2.nref if l2 is not None else None

        return add_LL

    def __sub__(self,other):
        if self>other:
            l3=other.head
        else:
            l3=self.head
        while l3 is not None:
            l3.val=-l3.val
            l3=l3.nref
        sub_LL=self + other
        l4=sub_LL.head
        while l4.nref is not None:
                l4=l4.nref
        while l4.val==0:
            sub_LL.del_end()
            l4=l4.pref 
        if self<other:
            sub_LL.add_end("-")
        return sub_LL

    def __mul__(self,other):
        l2=other.head
        sum_mul=ExtendedInt()
        carry=0
        sum_index=1
        while l2 is not None:
            sec_LL=ExtendedInt()
            l1=self.head
            
            while l1 is not None or carry!=0:
                l1_val=l1.val if l1 is not None else 0
                product=l1_val*l2.val+carry
                digit=product%10
                carry=product//10
                sec_LL.add_end(digit)
                l1=l1.nref if l1 is not None else None
            if sum_index==1:
                pass
            else:
                for k in range(1,sum_index):
                    sec_LL.add_begin(0)
            sum_index+=1
            sum_mul=sum_mul+sec_LL
            sec_LL.head=None        #or sec_LL.nref=None
            l2=l2.nref
        return sum_mul

    def __truediv__(self,other):
        div_LL=ExtendedInt()
        div_LL.add_begin(0)
        if self < other and other.head is not None:
            return div_LL
        else:   
            count1_LL=ExtendedInt()
            count1_LL.add_begin(1)      
            ll1=ExtendedInt()
            nl1=self.head
            while nl1 is not None:
                ll1.add_end(nl1.val)
                nl1=nl1.nref
            while True:
                if ll1.__ge__(other):
                    div_LL = div_LL + count1_LL
                    ll2=ll1-other         
                    ll1=ll1-other
                    ll1=ll2
                else:
                    break
            return div_LL

    def __lt__(self,other):
        if not self>=other:
            return True
        else:
            return False

    def __gt__(self,other):
        l1=self.head
        l2=other.head
        if self.length>other.length:
            return True
        elif self.length<other.length:
            return False
        else:
            is_gt=False
            while l1.nref is not None and l2.nref is not None:
                l1=l1.nref
                l2=l2.nref
            while l1 is not None and l2 is not None:
                if l1.val>l2.val:
                    is_gt=True
                    break
                elif l1.val<l2.val:
                    is_gt=False
                    break
                else:
                    l1=l1.pref
                    l2=l2.pref
            return is_gt

    def __eq__(self,other):
        l1=self.head
        l2=other.head
        if self.length!=other.length:
            return False
        else:
            is_equal=True
            while l1 is not None and l2 is not None:
                if l1.val!=l2.val:
                    is_equal=False
                    break
                else:
                    l1=l1.nref
                    l2=l2.nref
            return is_equal

    def __le__(self,other):
        if self<other or self==other:
            return True
        else:
            return False

    def __ge__(self,other):
        if self>other or self==other:
            return True
        else:
            return False

# create_number function creates a linked list of digits of a number in reverse order
# it can take input as integer value n which is the number of digits in the number and will give a randomly generated number
# or it can take input as a list of digits of a number 
def create_number(n):
    ExtendedInt3=ExtendedInt()
    if isinstance(n,int):
        for i in range(n):
            data=random.randint(1,9)
            print(data,end="")
            ExtendedInt3.add_begin(data)
    elif isinstance(n,list):
        for i in n:
            print(i,end="")
            ExtendedInt3.add_begin(i)
    print()
    return ExtendedInt3

############# TEST CASES ###################

#add operation
# sum_list=create_number(200) + create_number(50)
# sum_list.print_LL_in_reverse()

#substraction operation
# diff_list=create_number([2,1,9,8]) - create_number([2,3,5,4,8])
# diff_list.print_LL_in_reverse()

#multiplication operation
mul_list=create_number(7) * create_number(8)
mul_list.print_LL_in_reverse()

# division operation
# div_list=create_number(15) / create_number(8)
# div_list.print_LL_in_reverse()

# == operation
# eq_list=create_number(2) == create_number(2)
# print(eq_list)

# >= operation
# ge_list=create_number([1,7]) >= create_number([6,1])
# print(ge_list)

# > operation
# gt_list=create_number([1,0]) > create_number([1,0])
# print(gt_list)

# < operation
# lt_list=create_number([1,2]) < create_number([1,2])
# print(lt_list)

# <= operation
# le_list=create_number([1,2]) <= create_number([1,2])
# print(le_list) 










    

