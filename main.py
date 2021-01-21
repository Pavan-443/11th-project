import dataandtools as datatools
from time import sleep
from prettytable import PrettyTable

while True:
    # First Print the Main menu Options and instructions
    instructions = "\n1: See/Manage Cadets' Info\n2: see/Manage Fee status of Cadets\n0:Exit\n"
    print(instructions, end="\n\n")
    manage_choice = int(input('Enter Your choice from the above Menu: '))

    if manage_choice == 0:
        break

    elif manage_choice == 1:
        print("""\nYou chose to Manage cadets' Info\n""")
        sleep(1)
        instructions2 = "1: See a Cadet's Details\n2: Edit a Cadet Details\n3: Add New Cadet\n4: Remove a Cadet's " \
                        "Details" \
                        "\n5: See All Cadet's Details\n6: Return to the Main Menu\n0:Exit"
        print(instructions2, end="\n\n")
        cadet_choice = int(input("Enter Your choice from the above Menu: "))

        if cadet_choice == 0:
            break
        if cadet_choice == 6:
            continue

        elif cadet_choice == 1:
            print("You Have Chose to see a cadet's Details", end="\n\n")

            searchcadet_choice = datatools.search_cadet()
            if searchcadet_choice == 'ok':
                end_choice = datatools.ending()
                if end_choice == 1:
                    continue
                elif end_choice == 0:
                    break

            if searchcadet_choice == 0:
                break
            if searchcadet_choice == 5:
                continue
