from time import sleep
from prettytable import PrettyTable
# List to store Cadet Names.
cdt_names = ["thummalapalli pavan teja", "surakanti advaith Reddy", "gummadi charan sai"]

# List to store the Cadet Roll No.
cdt_rolls = ['443', '106', '439']

# List to store Cadet Father Name.
cdtfather_names = ['jkl', 'klj', 'opj']

# List to store Cadet Fee statuses.
fee_Statuses = ['Paid', 'Not Paid', 'Paid']


def find_position_list(matched_list, to_find_inlist):
    position_list = []
    for item in matched_list:
        i = to_find_inlist.index(item)
        position_list.append(i)

    return position_list


def ending():
    instruc = "\n1: Go Back to the previous Menu\n2: Return to Main Menu\n0:Exit\n"
    print(instruc)
    end_choice = int(input('Enter choice from above menu: '))

    return end_choice


def namesd_matched(name, namelist):
    names_matched_list = []
    name_words = name.split()
    for cdt_name in namelist:
        cdt_name = cdt_name.lower()
        count = 0
        cdt_name_words = cdt_name.split()
        for word in name_words:
            if word.lower() in cdt_name_words:
                count += 1
        if count >= 1:
            names_matched_list.append(cdt_name)

    return names_matched_list


def search_cadet():
    instructions3 = "\n1: Search for the cadet with Name\n2: Search for the cadet with Roll No" \
                    "\n3:Search for the Cadet with Father Name\n4: Go Back to the Previous Menu\n5: Return to the" \
                    " Main Menu\n0:Exit\n"
    print(instructions3)
    searchcadet_choice = int(input('Enter your choice from the above Menu: '))
    if searchcadet_choice == 1:
        sleep(0.5)
        cadet_name = input("\nEnter Name of the Cadet: ").lower()
        names_matched = namesd_matched(cadet_name, cdt_names)
        pos_list = find_position_list(names_matched, cdt_names)

        if len(names_matched) >= 1:
            sleep(0.5)
            print('Following are the cadet(s) and cadet(s) Details whose Name Matches with the'
                  ' one you Have Entered')
            x = PrettyTable()
            x.field_names = ["Roll No", "Cadet Name", "Father Name"]
            for pos in pos_list:
                x.add_row([cdt_rolls[pos], cdt_names[pos].title(),
                           cdtfather_names[pos].title()])
            print(x)
            return "ok"

        else:
            print(f'No Cadet Name Matched with the name {cadet_name}')
            return 'Not Matched'


    elif searchcadet_choice == 3:
        sleep(0.5)
        father_name = input("\nEnter Father Name of the Cadet: ").lower()
        names_matched = namesd_matched(father_name, cdtfather_names)
        pos_list = find_position_list(names_matched, cdtfather_names)

        if len(names_matched) >= 1:
            sleep(0.5)
            print('Following are the cadet(s) and cadet(s) Details whose Father Name Matches with the'
                  ' one you Have Entered')
            x = PrettyTable()
            x.field_names = ["Roll No", "Cadet Name", "Father Name"]
            for pos in pos_list:
                x.add_row([cdt_rolls[pos], cdt_names[pos].title(),
                           cdtfather_names[pos].title()])
            print(x)
            return "ok"

        else:
            print(f"No Cadet's Father Name Matched with the name {father_name}")
            return 'Not Matched'

    elif searchcadet_choice == 2:
        roll = input("\nEnter the Roll No of the Cadet: ").upper()
        sleep(0.5)
        if roll in cdt_rolls:
            print('Following are the Details whose Roll No Matched with the one you Have Entered')
            pos = cdt_rolls.index(roll)
            x = PrettyTable()
            x.field_names = ["Roll No", "Cadet Name", "Father Name"]
            x.add_row([cdt_rolls[pos], cdt_names[pos].title(),
                       cdtfather_names[pos].title()])
            print(x)
            return 'ok'
        else:
            print('No Cadet Found with the Roll No You Entered.')
            return 'Not Matched'

    
    else:
        return searchcadet_choice


def changed(roll, name, fat_name, postition):
    global name_val, roll_val, fatname_val
    if roll == cdt_rolls[postition]:
        roll_val = 'Changed'
    elif roll != cdt_rolls[postition]:
        roll_val = 'Not Changed'
    if name == cdt_names[postition]:
        name_val = 'Changed'
    elif name != cdt_names[postition]:
        name_val = 'Not Changed'
    if fat_name == cdtfather_names[postition]:
        fatname_val = 'changed'
    elif fat_name != cdtfather_names[postition]:
        fatname_val = 'Not Changed'
    tbl = PrettyTable()
    tbl.field_names = ["Roll No", "Cdt Name", "Father Name"]
    tbl.add_row((roll_val, name_val, fatname_val))
    print(tbl)