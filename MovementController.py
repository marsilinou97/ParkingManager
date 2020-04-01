import database_test

def display_all_activity():
    for row in database_test.select_all_from_table("parking_movements"):
        print(row)

def display_filtered_info(filter, value):
    for row in database_test.select_all_from_table_filtered("parking_movements", filter, value):
        print(row)

def main():
    filter = "movement_type"
    value = "Exit"
    # checks parking movements table for filter attribute called movement_type for value of "exit"
    display_filtered_info(filter, value)
main()