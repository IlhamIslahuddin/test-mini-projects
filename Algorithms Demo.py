import time
def demo_algorithms():
    print ("Welcome User. This is a function designed to demonstrate the 4 basic principles of algorithms.")
    time.sleep(2)
    print ("If you encounter any errors, clear the terminal and run the code again.")
    time.sleep(2)
    print ("Make the terminal fullscreen/wide for the best experience.")
    time.sleep(1.5)
    print ("--------------------------------------------------------------------------------------------")
    time.sleep(2)
    print ("~ The first is: 'Sequence'. The order in which the steps of the algorithm are carried out.")
    time.sleep(2)
    print ("This line gets printed first. (1)")
    time.sleep(1.5)
    print ("Then this line. (2)")
    time.sleep(1.5)
    print ("And lastly this line. (3)")
    time.sleep(1.5)
    print ("This is because the lines were written in that order before execution.")
    time.sleep(1.5)
    print ("It would not make sense if the sentences were in a different order.")
    time.sleep(1)
    print ("--------------------------------------------------------------------------------------------")
    time.sleep(1.5)
    print ("~ Next is: 'Selection'. The ability to choose the next action between multiple choices.")
    time.sleep(3)
    valid = False
    while valid == False:
        choice = str(input("Would you like the phrase 'Hello World!' to be printed? (1 = yes, 2 = no).\n"))
        if choice == "1":
            print ("Hello World!")
            valid = True
            time.sleep(1)
            print ("1 was inputted, the phrase was printed.")
        elif choice == "2":
            print ("2 was inputted, the phrase was not printed.")
            valid = True
        else:
            print ("Input was not recognised. Try again.")
    time.sleep(2)
    print ("Selection can also be condition-based.")
    time.sleep(1)
    print ("--------------------------------------------------------------------------------------------")
    time.sleep(1.5)
    print ("~ Next is: 'Repetition'/'Iteration'. The action of repeating a step more than once.")
    time.sleep(2)
    worked = False
    while worked == False:
        try:
            count = int(input(("How many times would you like the phrase 'Hello World!' to be printed? (Numbers only)\n")))
            for i in range(count):
                print("Hello World!")
                time.sleep(1)
                worked = True
        except:
            print ("Input was not a whole number. Try again.")
    time.sleep(0.5)
    if count == 1:
        print ("Hello world! was printed 1 time.")
    else:
        print (f"'Hello World!' was printed {count} time(s).")
    time.sleep(1.5)
    print ("Iteration can also be used conditionally, in which the code will repeat until a condition is met.")
    time.sleep(1)
    print ("--------------------------------------------------------------------------------------------")
    time.sleep(2)
    print ("~ Lastly: 'Variable'. The action of storing a value in a named variable.")
    time.sleep(2)
    variable = input("Whatever you type next will be stored in a variable and printed again.\n")
    time.sleep(1.5)
    print (f"{variable} was stored in the variable.")
    time.sleep(1)
    print ("--------------------------------------------------------------------------------------------")
    time.sleep(2)
    print ("End of demonstration.")

if __name__ == "__main__":
    demo_algorithms()
