def safe_divide(numerator, denominator):
    try:
        # Attempt conversion to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den

        # Return the result if no exceptions were raised
        return f"The result of the division is {result}"

    except ValueError:
        # This block runs if float() conversion fails
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # This block runs if division by zero occurs
        return "Error: Cannot divide by zero."