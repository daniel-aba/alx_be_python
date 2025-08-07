#!/usr/bin/env python3

from class_static_methods_demo import Calculator

def main():
    # Using the static method directly on the class.
    # It doesn't need to be called on an instance.
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method directly on the class.
    # It automatically passes the class itself as the first argument.
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()