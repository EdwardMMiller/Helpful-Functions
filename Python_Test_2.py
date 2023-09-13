def string_num_checker(string):

    '''
    Checks to ensure a string is not empty and
    does contain at least one number

    Args:
         string - a string inputted by the user
    Returns:
         string_check = a boolean of either False or True
    '''
    
    string_check = False
    if len(string) == 0:
        # checks if string is empty
        return string_check
    else:
        for char in string:
            if char.isnumeric() == True:
                string_check =  True
            # checks if string contains
            # any digits and if so c
    return string_check

def string_to_integer_list(string):

    '''
    Gets the integers out of a string inputted by
    the user and returns a list of integers

    Args:
         string - a string inputted by the user
    Returns:
         new_list = a list of integers obtained from the
                    user inputted string 
    '''
    num_string = 0
    for char in string:
        if char.isnumeric() == True:
            num_string =  1
    # checks if string contains any digits

    if len(string) == 0 or num_string != 1:
        return "Please input a string containing numbers!"
    else:      
        new_list = []
        # initialize a list
        num = str()
        # initialize an empty string to store the numbers
        cnt = 1
        # assume the string has length of 1
        for char in string:
            # loops through each character in the string
            if cnt == len(string) and string[-1].isnumeric() == True:
                # to deal with last character in the string
                # and ignoring it if it's not numeric
                new_list.append(int(num+string[-1]))
                # adds number plus the last char in string 
            elif char.isnumeric() == False and len(num) != 0:
                # deals with next break after a new integer has been started
                # so the length of num is not 0 here
                new_list.append(int(num))
                # add integer to list
                num = str()
                # reset num list for next number in the list
            elif char.isnumeric() == False:
                # deals with empty spaces and other characters
                # that aren't numbers, keeps num from adding chars
                # until an actual number is reached
                num = num
            else:
                # adds numeric characters until
                # something that is not a numeric char
                # is reached
                num = num+char
            cnt = cnt +1
            
        return new_list

def list_updater(num_list):

    '''
    if a digit in the list reappears,
    the function multiplies the next digit by 2
    and returns the updated list
    
    Args:
         num_list - a list of integers
    Returns:
         updated_list = a list of integers with multiples of the integers
          multipled by 2
    '''
    
    updated_list = [] 
    double = False
    # initialize list and variable
    
    for i in range(len(num_list)):

        if double == True:
            updated_list.append(num_list[i]*2)
        else:
            updated_list.append(num_list[i])
        # adds the next item in the list
        # if the double is set to True, it doubles it
        if i == len(num_list) -1:
            break
        # leaves if this is the last item on the list
        # to prevent out of range errors with 
        # comparing i and i + 1
        
        if num_list[i] == num_list[i + 1]:
            double = True
            # double variable set to True
            # if the numbers are the same
        else:
            double = False
        
    return updated_list

def run_program():
    '''
    Main program to run functions above

    Args: none

    Returns:
            str('STOP') if input_list == 'Q'
    '''
    input_list= input("Enter a list of numbers: Separate each number with a comma: ")
    # gets a string from the user

    while string_num_checker(input_list) == False:
        # loops while invalid string type entered
        print("Empty or Non-Numerical String! Press 'Q' to quit")
        input_list= input("Enter a list of numbers: Separate each number with a comma: ")
        if input_list == 'Q':
            break
        # allows user to exit

    if input_list == 'Q':
        print("Quitting program")
        return 'STOP'
    else:
        number_list = string_to_integer_list(input_list)
        print("List of numbers obtained from string: ", number_list)
        print("Upated list: ", list_updater(number_list))

    return 

answer = 'y'
# intialize answer variable

while answer == 'y' or answer == 'Y' and Run != 'STOP':
    # keep loop going until user decides to quit
    
    Run = run_program()
    if Run == 'STOP':
        break
    answer = input("Would you like to go again? If so, input y or Y : ")



