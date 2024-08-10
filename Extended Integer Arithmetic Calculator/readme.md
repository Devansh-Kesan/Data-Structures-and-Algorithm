# Extended Integer Arithmetic Calculator

The **Extended Integer Arithmetic Calculator** is a custom Python class named `ExtendedInt`, designed to handle integer operations on very large numbers that exceed the typical storage limits of standard integer types. This implementation utilizes a doubly linked list to store each digit of the number individually, allowing operations on numbers with over 100 digits.

## Class Overview

### Node Class
- **Purpose**: Represents a single digit in the linked list.
- **Attributes**:
  - `val`: Stores the digit value.
  - `nref`: Reference to the next node in the list.
  - `pref`: Reference to the previous node in the list.

### ExtendedInt Class
- **Purpose**: Provides methods for performing arithmetic operations (`+`, `-`, `*`, `/`) and comparisons (`<`, `>`, `==`, `<=`, `>=`) on large integers stored as linked lists.
- **Attributes**:
  - `head`: Reference to the first node in the linked list.
  - `length`: The number of digits in the linked list.

## Key Methods

### Initialization and Node Addition

- `__init__()`: Initializes the `ExtendedInt` object and sets the linked list's head and length.
- `add_begin(data)`: Adds a node with the value `data` at the beginning of the linked list.
- `add_end(data)`: Adds a node with the value `data` at the end of the linked list.

### Arithmetic Operations

- `__add__(self, other)`: Implements addition by iterating through both linked lists, adding corresponding digits, and handling carries.
- `__sub__(self, other)`: Implements subtraction by negating digits of the smaller number and adding it to the larger number.
- `__mul__(self, other)`: Implements multiplication by multiplying each digit of one number by all digits of the other and accumulating the results.
- `__truediv__(self, other)`: Implements division using repeated subtraction until the dividend is less than the divisor.

### Comparison Operations

- `__lt__(self, other)`: Less than comparison based on the length and individual digit comparison.
- `__gt__(self, other)`: Greater than comparison based on the length and individual digit comparison.
- `__eq__(self, other)`: Checks if two numbers are equal by comparing lengths and individual digits.
- `__le__(self, other)`: Less than or equal to comparison, utilizing existing methods.
- `__ge__(self, other)`: Greater than or equal to comparison, utilizing existing methods.

### Utility Methods

- `print_LL_in_reverse()`: Prints the number stored in the linked list in the correct order by traversing the list in reverse.

## Input and Output

### Input Format

- `number1 operation number2`
  - `number1` and `number2` can be large integers.
  - `operation` can be any of the supported arithmetic or comparison operators (`+`, `-`, `*`, `/`, `<`, `>`, `==`, `<=`, `>=`).

### Output Format

- The result of the operation performed on `number1` and `number2`.

## Example

Here is how you can create and use `ExtendedInt` objects:

```python
# Example of creating ExtendedInt numbers
number1 = create_number([1, 2, 3, 4, 5])
number2 = create_number([9, 8, 7])

# Performing addition
sum_list = number1 + number2
sum_list.print_LL_in_reverse()  # Output: 1112

# Performing subtraction
diff_list = number1 - number2
diff_list.print_LL_in_reverse()  # Output: 2348

# Performing multiplication
mul_list = number1 * number2
mul_list.print_LL_in_reverse()  # Output: 12193815

# Performing division
div_list = number1 / number2
div_list.print_LL_in_reverse()  # Output: 1
