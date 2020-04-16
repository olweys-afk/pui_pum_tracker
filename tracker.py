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

if (symp == 'Y' and trav == 'Y' and expo == 'Y') or (symp.lower() == 'Y' and trav.lower() == 'Y') or (symp.lower() == 'Y' and expo.lower() == 'Y'):
    PUI()
    print("PUI")

else:
    PUM()
    print("PUM")
















