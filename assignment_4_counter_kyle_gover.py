def main():


    print("Hello!")

    while True:
        start_value0 = input("Enter a start value (Default: 0): ")
        if start_value0 == "": #check if input was blank and assign value of 0
            print("Using default value")
            start_value = 0
            break
        elif start_value0.isdecimal(): #check if input is number before converting
            start_value = int(start_value0) # to intiger
            break
        print("Please enter only numbers") # error message for if input was not
        pass                                #a number or blank


    while True:
        end_value0 = input("Enter an end value: ")
        if end_value0 == "":
            print("Please enter an end value") #error for if input was blank
        elif end_value0.isdecimal():
            end_value = int(end_value0)
            break
        else:
            print("Please enter only numbers") #error for if input was not a number
        pass

    while True:
        step_value0 = input("Enter a step value (Default: 1): ")
        if step_value0 == "":
            print("Using default value")
            step_value = 1
            break
        elif step_value0.isdecimal():
            step_value = int(step_value0)
            break
        print("Please enter only numbers")
        pass


    print("The numbers are:", end=" ")
    for x in range(start_value,end_value,step_value):
        print(x, end=" ")





if __name__ == '__main__':
    main()
