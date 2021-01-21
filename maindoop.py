import dataandtools as datatools
from time import sleep
from prettytable import PrettyTable

i = 1
while i != 0:
    k = 1
    # First Print the Main menu Options and instructions
    instructions = "\n1: See/Manage Cadets' Info\n2: see/Manage Fee status of Cadets\n0:Exit\n"
    print(instructions, end="\n\n")
    manage_choice = int(input('Enter Your choice from the above Menu: '))

    if manage_choice == 0:
        break

    elif manage_choice == 1:
        print("""\nYou chose to Manage cadets' Info\n""")
        while k != 0:
            n = 1
            s = 1
            sleep(0.5)
            instructions2 = "\n1: See a Cadet's Details\n2: Edit a Cadet Details\n3: Add New Cadet\n4: Remove a Cadet's " \
                            "Details" \
                            "\n5: See All Cadet's Details\n6: Return to the Main Menu\n0:Exit\n"
            print(instructions2, end="\n\n")
            cadet_choice = int(input("Enter Your choice from the above Menu: "))

            if cadet_choice == 0:
                i = 0
                break
            if cadet_choice == 6:
                break

            elif cadet_choice == 1:
                print("You Have Chose to see a cadet's Details", end="\n\n")
                while s != 0:
                    searchcadet_choice = datatools.search_cadet()
                    if searchcadet_choice == 'ok' or searchcadet_choice == "Not Matched":
                        end_choice = datatools.ending()
                        if end_choice == 1:
                            continue
                        elif end_choice == 0:
                            i = 0
                        elif end_choice == 2:
                            k = 0
                            break
                        else:
                            print('\nEnter a Valid Input From the Menu')
                            print('Going Back to the Previous Menu\n')
                            sleep(0.5)

                    elif searchcadet_choice == 0:
                        i = 0
                        k = 0
                        break
                    elif searchcadet_choice == 5:
                        k = 0
                        break
                    elif searchcadet_choice == 4:
                        break
                    else:
                        print('\nEnter a Valid Input from the Menu.\n')

            elif cadet_choice == 2:
                print("You Have Chose to Edit a Cadet Details", end="\n\n")
                while n != 0:
                    searchcadetedit_choice = datatools.search_cadet()
                    if searchcadetedit_choice == 'ok':
                        number = input('Enter the Roll No of the cadet You want to Edit from the above table: ')
                        if number in datatools.cdt_rolls:
                            position = datatools.cdt_rolls.index(number)
                            tb = PrettyTable()
                            tb.field_names = ["Roll No", "Cdt Name", "Father Name"]
                            tb.add_row([datatools.cdt_rolls[position], datatools.cdt_names[position], datatools.cdtfather_names[position]])
                            print(f'\nAbove Table Contains Data About the Cadet with Roll no. {number}')
                            confirm = int(input('Press 1 to proceed(Press Any other key to cancel): '))
                            if confirm == 1:
                                print('Enter the same Detail Again to Retain the Data and Not Edit it')
                                name = input(f'Enter a New Name to Replace {datatools.cdt_names[position]}: ')
                                roll_no = input(f'Enter a New Roll No to Replace {datatools.cdt_rolls[position]}: ')
                                fath_name = input(f'Enter Father Name to Replace {datatools.cdtfather_names[position]}: ')
                                print(f"Result of what you did Now is: ")
                                datatools.changed(roll_no, name, fath_name, position)
                                endchoice = datatools.ending()
                                if endchoice == 0:
                                    i = 0
                                    k = 0
                                    break
                                if endchoice == 1:
                                    break
                                if endchoice == 2:
                                    k = 0
                                    break
                            else:
                                print('You Have chose to cancel the Process')
                                print('cancelling...')
                                sleep(0.5)
                                endchoice2 = datatools.ending()
                                if endchoice2 == 0:
                                    i = 0
                                    k = 0
                                    break
                                if endchoice2 == 1:
                                    break
                                if endchoice2 == 2:
                                    k = 0
                                    break
                        elif number not in datatools.cdt_rolls:
                            print('Enter A valid Roll No from the Table Above')
                    if searchcadetedit_choice == 4:
                        break
                    if searchcadetedit_choice == 5:
                        k = 0
                        break
                    if searchcadetedit_choice == 0:
                        k = 0
                        i = 0
                        break

