# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from package_a.entrypoint import entrypoint
from package_a.entrypoint import entrypoint
import package_c.c_entrypoint as pce
from package_c.my_numpy import mult_np

# from p


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    entrypoint(name)
    pce.main(mess=name, fn=20, sn=100)
    print(mult_np(6, 6))
    # package_c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm2')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
