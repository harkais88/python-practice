#!/usr/bin/python3

"""Write a Python program to get a list of locally installed Python modules."""

import pkg_resources
import pandas as pd

if __name__ == "__main__":
    installed_packages = pkg_resources.working_set

    # print("INSTALLED MODULES \n MODULE \t\t VERSION \t\t PATH")
    installed_packages_list = [(i.key,i.version,i.module_path) for i in installed_packages]

    # for key,version,path in installed_packages_list:
    #     print("%s \t %s \t %s" % (key,version,path))

    # This part is to just print it in a clean way
    data = pd.DataFrame(installed_packages_list, columns = ["MODULES","VERSION","PATH"])
    
    print(data.to_string())