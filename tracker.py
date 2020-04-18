
def PUI():

    pui = open("pui_info.txt", "a")
    pui.write('\n')
    pui.write('\n')
    pui.write("Name:")
    pui.write(first_name)
    pui.write('\n')
    pui.write("Last Name:")
    pui.write(last_name)
    pui.write('\n')
    pui.write("Age:")
    pui.write(age)
    pui.write('\n')
    pui.write("Address:")
    pui.write(add)
    pui.write('\n')
    pui.write("Contact:")
    pui.write(con)

    pui.close()

def PUM():

    pum = open("pum_info.txt", "a")
    pum.write('\n')
    pum.write('\n')
    pum.write("Name:")
    pum.write(first_name)
    pum.write('\n')
    pum.write("Last Name:")
    pum.write(last_name)
    pum.write('\n')
    pum.write("Age:")
    pum.write(age)
    pum.write('\n')
    pum.write("Address:")
    pum.write(add)
    pum.write('\n')
    pum.write("Contact:")
    pum.write(con)

    pum.close()

def find_pui():
    pui = open("pui_info.txt", "r")

    for text_line in pui:
        print(text_line)

    pui.close()

def find_pum():
    pum = open("pui_info.txt", "r")

    for text_line in pum:
        print(text_line)

    pum.close()


while True:

    print("Select Action: \n ")
    print("A. Add New Entry")
    print("Find Patient", "I. PUI", "M. PUM")
    print("D. Delete Patient")
    print("Q. Exit")
    print("\n")

    sel = input("Enter the Letter:")

    if sel == 'Q':
        print("GoodBye!")
        break

    if sel == 'A':

        print("Personal InFo \n ")
        first_name = input('First Name:')
        middle_name = input('Middle Name:')
        last_name = input('Last Name:')
        age = input("Age:")
        add = input("Address:")
        con = input("Cel/tel no.:")

        print(" \n Just type Y/N in the field \n ")

        trav = input("Have you traveled to china?:")
        expo = input("Do you had exposure to those w/ confirmed nCov?:")
        symp = input("Do you have respiratory symptoms?:")
        fever = input("Do you have fever >=38C?:")

        if (symp == 'Y' and trav == 'Y' and expo == 'Y') or (symp == 'Y' and trav == 'Y') or (symp  == 'Y' and expo == 'Y'):
            PUI()
            print("PUI")

        else:
            PUM()
            print("PUM")

    if sel == 'I':
        find_pui()
        


    if sel == 'M':
        find_pum()



    if sel == "D":

        print("XXXnot ApplicableXXX")














