from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains the current date and time and prints it in a readable format.
    """
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in "YYYY-MM-DD" format.
    """
    try:
        days_to_add_str = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_to_add_str)

        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)

        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to orchestrate the display of current datetime
    and calculation of a future date.
    """
    display_current_datetime()
    print() # Add a newline for better readability between parts
    calculate_future_date()

# Entry point of the script
if __name__ == "__main__":
    main()