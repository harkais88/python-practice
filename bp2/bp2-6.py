#!/usr/bin/python3

"""Write a Python program that prints long text, converts it to a list, 
and prints all the words and the frequency of each word."""

if __name__ == "__main__":
    string = " ".join(["Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde &" ,
    "Informatica ( CWI ) in the Netherlands as a successor to the ABC programming language, which was inspired by" , 
    "SETL, capable of exception handling and interfacing with the Amoeba operating system. Its implementation" , 
    "began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer," , 
    "until 12 July 2018, when he announced his \"permanent vacation\" from his responsibilities as" ,                  
    "Python\'s \"benevolent dictator for life\", a title the Python community bestowed upon him to reflect" , 
    "his long-term commitment as the project\'s chief decision-maker. In January 2019, active Python core" ,
    "developers elected a five-member Steering Council to lead the project. Python 2.0 was released on 16" ,
    "October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection," ,
    "reference counting, and Unicode support. Python 3.0, released on 3 December 2008, with many of its major" ,
    "features backported to Python 2.6.x and 2.7.x. Releases of Python 3 include the 2to3 utility, which" ,
    "automates the translation of Python 2 code to Python 3. Python 2.7\'s end-of-life was initially set for 2015," ,
    "then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported" ,
    "to Python 3. No further security patches or other improvements will be released for it. Currently only 3.8" ,
    "and later are supported ( 2023 security issues were fixed in e.g. 3.7.17, the final 3.7.x release ) . In 2021," ,
    "Python 3.9.2 and 3.8.8 were expedited as all versions of Python ( including 2.7 ) had security issues leading" ,
    "to possible remote code execution and web cache poisoning. In 2022, Python 3.10.4 and 3.9.12 were expedited" ,
    "and 3.8.13, because of many security issues. When Python 3.9.13 was released in May 2022, it was announced" ,
    "that the 3.9 series ( joining the older series 3.8 and 3. 7) would only receive security fixes in the future." ,
    "On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7," ,
    "3.9.14, 3.8.14, and 3.7.14. As of November 2022, Python 3.11 is the stable release. Notable changes from" ,
    "3.10 include increased program execution speed and improved error reporting. Since 27 June 2023, Python 3.8" ,
    "is the oldest supported version of Python ( albeit in the \'security support\' phase ), due to Python 3.7" ,
    "reaching end-of-life. The first release candidate of Python 3.12 was offered on 6 August 2023."])

    print("The string: ",string,end="\n\n")

    list = string.split()

    print(f"All the letters found in the string: {set(list)} \n\n")
    print(f"Number of letters found in the string: ", end="")

    for char, count in zip(set(list),[list.count(ele) for ele in set(list)]):
        print(f"({char},{count}) ",end = "")
