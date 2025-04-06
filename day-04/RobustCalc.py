def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        a=int(a)
        b=int(b)
        if operator == '+':
            a+b
        elif operator == '-':
            a-b
        elif operator == '*':
            a*b
        elif operator == '/':
            a/b
        elif operator == '%' :
            a%b
        else:
            raise TypeError("Unsupported operator")
    except ZeroDivisionError as e:
        return "Error: "+str(e)
    except ValueError as e :
        return "Error:"+" Invalid input"
    except TypeError as e:
        return "Error: "+str(e)
    
# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"

