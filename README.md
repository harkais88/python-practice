# python-practice

<figure>
    <blockquote>
        Take up an idea, devote yourself, struggle in patience, and the sun will rise.<br>
        <b><i>Swami Vivekananda</i></b>
    </blockquote>
</figure>

This code generates a python test file consisting of questions taken from the files under the different topic directories. 10 questions are randomly chosen from each topic directory and are written to the test file.
The test file can be either in the format of a text file (.txt) or a notebook file (.ipynb). 
The option of which format is to be used is to be selected by the user using the GUI presented by the code.

The text file format should be considered as practicing without a crutch. If you are not able to solve the 
question at first, try to research more about relevant modules that can come to use. You can also google to see if there are any solutions provided in the online forums, although I would recommend to first try it by yourself until you are absolutely certain you cannot do it. Alternatively, you may use the search bar provided in the GUI to find a solution to the questions, although it is simply limited to the files that are provided in the topic directories.

If you would like a more simpler or efficient practice approach, use the ipynb format. You would need a notebook viewer for this, like Jupyter Notebook or Google Collab Notebooks (at least this way, you don't have to install anything). A code space and kernel is provided this way, and while solutions are also provided along with the questions, they are hidden at first, and should only be opened after you try it yourself. 

To use, download the testGen.py script and atleast one of the different topic directories and put them in the same directory. Then, simply run the script and the GUI will be presented. Aternatively, you may want to convert the script into an .exe file using pyinstaller, for which I would suggest using a spec file for building exe.

If you simply want to execute the testGen.py script, the following modules are needed to be installed using pip:
nbformat, tkinter, ttkwidgets, art(This one is actually optional, if you don't like this, open up the script, go to the txtOps function, and find the OPTIONAL comment)

All of these questions are taken from the W3Resource Website
https://www.w3resource.com/python-exercises/
