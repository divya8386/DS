# Program: Evaluate Postfix Expression using Stack

def evaluate_postfix(expression):
    stack = []

    for char in expression.split():
        if char.isdigit():
            # Push operand (number) to stack
            stack.append(int(char))
        else:
            # Pop two operands for the operator
            val2 = stack.pop()
            val1 = stack.pop()

            # Apply the operator
            if char == '+':
                stack.append(val1 + val2)
            elif char == '-':
                stack.append(val1 - val2)
            elif char == '*':
                stack.append(val1 * val2)
            elif char == '/':
                stack.append(val1 // val2)  # Integer division

    # Final result will be the only element left in stack
    return stack.pop()


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    expr = input("Enter a postfix expression (space-separated): ")
    result = evaluate_postfix(expr)
    print("Result:", result)
