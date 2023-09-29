#!/usr/bin/python3
#Randomly generates a directory consisting of n files from d dirs with n questions 
# each picked from each directory

import os,random
from art import text2art
import nbformat as nbf
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
import webbrowser

class testGen:
    """ Class for generating tests based on the practice files\n
    Use txtOps() for txt file format or nbOps() for ipynb format """

    def __init__(self):
        self.curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.test_dir = "Test Attempts"
        self.file_paths_list = self.getFilesPathsList()

    def getTopicDirs(self):
        """ Get the list of all the different topic directories"""

        return [dir for dir in os.listdir(self.curr_dir) 
                if (os.path.isdir(dir) and dir != self.test_dir and dir[0] != ".")]

    def checkTestDir(self):
        """  The test files go into this directory, if it does not exist, we create it"""

        if not os.path.exists(f"{self.curr_dir}/{self.test_dir}"):
            os.mkdir(f"{self.curr_dir}/{self.test_dir}")

    def getFilesPathsList(self):
        """  Get the list of of lists of every single file in each of the topic directories"""

        file_paths_list = []

        # Iterating through the paths of each topic directory found
        for path in self.getTopicDirs():
            # Get the absolute path of the topic directory
            topic_dir = os.path.abspath(path)
            
            # Get the list of files under the topic directory
            files = os.listdir(topic_dir)

            # Setting the filenames to their relative path names as topicDir\\fileName
            files = [os.path.join(file[:file.find("-")],file) for file in files]

            # Appending the list of relative path names to the file_paths_list list
            file_paths_list.append(files)

        return file_paths_list

    def txtOps(self):
        """ Generates a test file in txt format"""

        # First, we check whether the Test Attempts Folder even exists
        self.checkTestDir()

        # Setting Test File Number, as there would be multiple test files 
        file_no = len([file for file in os.listdir(f"{self.curr_dir}/{self.test_dir}") 
                       if file.endswith(".txt")]) + 1

        # Setting Test File Path
        self.test_file_path = os.path.abspath(os.path.normpath(
            f"{self.curr_dir}/{self.test_dir}/Python_Test_{file_no}.txt"))

        # Creating our test file
        test_file = open(self.test_file_path,"w")
        
        # Heading
        test_file.write(text2art("Python Test".center(85), font = "ogre"))

        # Iterating through each list of relative path names of the different topic dirs inside
        # the file_paths_list list
        self.getFilesPathsList()

        for file_paths in self.file_paths_list:
            # To track the files that have been read, and to set it to only read from a set number of files
            file_log = []

            # Writing the topic name as the sub-Header, to distinguish between the different topics...
            # Maybe this won't be required, and in the future, should look into jumbling the order up too
            test_file.write(text2art(file_paths[0][:file_paths[0].find(os.path.basename(file_paths[0]))-1], 
                                     font = "ogre") + "\n")
            # OPTIONAL: IF DECORATED SUB HEADERS ARE NOT REQUIRED, REMOVE COMMENT FROM NEXT LINE
            #test_file.write(file_paths[0][:file_paths[0].find(os.path.basename(file_paths[0]))-1])

            # Writing our 10 questions from the current topic
            while len(file_log) != 10:

                # Getting a unique file randomly
                while True:
                    file_path = random.choice(file_paths)
                    if file_path not in file_log:
                        break

                # Writing the question no
                test_file.write(str(len(file_log) + 1) + ". ")

                # Opening and reading the file line by line
                file = open(file_path,"r")
                lines = file.readlines() 

                # The questions are written in the first multiline comment in each file
                for line in lines:
                    # Ignoring any other comment before first multiline comment, mainly useful in a Unix environment
                    if "#" in line or line == "\n":
                        continue

                    # Removing all instances of the comment quotations
                    w_line = line.replace("\"\"\"","")

                    # Writing our line to the test file
                    test_file.write(w_line)

                    # If the string """"\n" is encountered, it means the end of the comment
                    if "\"\"\"\n" in line:
                        break

                # Adding a new line for the next question
                test_file.write("\n")

                # Closing the file we are reading from
                file.close()

                # Taking note of which file was read from
                file_log.append(file_path)

        # After creating our test file, we close it
        test_file.close()

    def nbOps(self):
        """ Generates a test file in ipynb format"""

        # First, we check whether the Test Attempts Folder even exists
        self.checkTestDir()

        # Creating a new notebook
        nb = nbf.v4.new_notebook()
        nb["cells"] = [nbf.v4.new_markdown_cell("<h1><b><center>PYTHON TEST</center></b></h1>")]

        # Code Boilerplate that goes into each of the code cells
        code_lines = "if __name__ == \"__main__\":\n\t# Code Goes Here\n\tpass"

        # Iterating through each list of relative path names of the different topic dirs inside
        # the file_paths_list list 
        self.getFilesPathsList()

        for file_paths in self.file_paths_list:
            # To track the files that have been read, and to set it to only read from a set number of files
            file_log = []

            # Writing the topic name as a sub-header

            nb["cells"].append(nbf.v4.new_markdown_cell("<h2><b>" + 
                                                        file_paths[0][:file_paths[0].find(os.path.basename(file_paths[0]))-1]
                                                        + "</h2></b>"
                                                        + "\n"))

            # Bonus: Writing the sub-headers in ASCII Art style
            # nb["cells"].append(nbf.v4.new_markdown_cell(
            #     text2art(file_paths[0][:file_paths[0].find("\\")], font = "ogre").
            #             replace("_","&lowbar;").replace(" ","&#160;").replace("\n","<br>").replace("\\","&bsol;")
            #                                             + "\n"))
            
            # Writing our 10 questions from the current topic
            while len(file_log) != 10:

                # Getting a unique file randomly
                while True:
                    file_path = random.choice(file_paths)
                    if file_path not in file_log:
                        break

                # Reading our file
                file = open(file_path, "r")
                lines = file.readlines()

                # Setting our question and solution result variable
                # Should contain the entire question
                q_line = ""
                # Should contain the entire solution
                s_line = ""

                # Extracting the question part from the file
                index = 0
                while "#" in lines[index] or lines[index] == "\n":
                    index += 1
                line = lines[index]
                while True:
                    f_line = line.replace("\"\"\"","").replace("\n","<br>").replace("\t","&#160;"*4)
                    q_line += f_line
                    if "\"\"\"\n" in line:
                        break
                    index += 1
                    line = lines[index]

                # Extracting the solution part from the file
                for i in range(index+1,len(lines)):
                    line = lines[i]
                    f_line = line.replace("\"\"\"","").replace("\n","<br>")
                    firstCharIndex = next(filter(str.isalpha, f_line), None)
                    if firstCharIndex is not None:
                        f_line = f_line.replace(" ", "&#160;", f_line.find(firstCharIndex))
                    s_line += f_line

                # Creating a new markdown cell with the result variable, thus writing a new question
                nb["cells"].append(nbf.v4.new_markdown_cell(str(len(file_log)+1) + ". "+ 
                                                            q_line))
                # Creating a code space for the user to test their code on
                nb["cells"].append(nbf.v4.new_code_cell(code_lines))
                # Creating a markdown cell for the solution
                nb["cells"].append(nbf.v4.new_markdown_cell(
                                        "<details><summary style = \"font-size: 18px;\">Show Solution</summary>"+
                                        "<span style=\"font-size: 15px; color: #03A062;\">" 
                                        + s_line + "</span>"))
                
                # Closing the file we took the question from
                file.close()
                # Logging the file to ensure uniqueness
                file_log.append(file_path)
        
        # Setting Test File Number, as there would be multiple test files 
        file_no = len([file for file in os.listdir(f"{self.curr_dir}/{self.test_dir}") if file.endswith(".ipynb")]) + 1

        # Setting out Test File Path
        self.test_file_path = os.path.abspath(os.path.normpath(f"{self.curr_dir}/{self.test_dir}/Python_Test_{file_no}.ipynb"))

        # Creating our test file
        test_file = open(self.test_file_path,"w")

        # After setting our JSON Format using the nb variable,
        # we write to the new notebook using the write function from the nbformat api
        nbf.write(nb,test_file)
        # Then, we close our test file
        test_file.close()

class GUI:
    """ Presents a GUI for the user to decide whether they want\n
        to make the test file a txt file or an ipynb file"""
    
    testObj = testGen()

    def __init__(self):
        # Get Question list for solution finding and autocomplete feature
        self.getQuestions()

        self.gui = tk.Tk()
        self.gui.title("Python Test Generator")
        self.draw()
        self.gui.mainloop()

    def getQuestions(self):
        """ Get all the questions in all the topic dirs in a single list"""

        self.questions_list = []
        r_line = ""

        for file_paths in self.testObj.file_paths_list:
            for file_path in file_paths:
                with open(file_path,"r") as file:
                    lines = file.readlines() 

                    # The questions are written in the first multiline comment in each file
                    for line in lines:
                        if "#" in line or line == "\n":
                            continue

                        # Removing all instances of the comment quotations
                        w_line = line.replace("\"\"\"","").replace("\n"," ")

                        # Writing our line to the test file
                        r_line += w_line

                        # If the string """"\n" is encountered, it means the end of the comment
                        if "\"\"\"\n" in line:
                            break

                self.questions_list.append(r_line)
                r_line = ""    

    def draw(self):
        """ Responsible for drawing GUI Elements"""

        # HEADING
        heading = tk.Label(self.gui, text = "Python Test Generator!", font = ("Helvetica",20))
        heading.grid(row = 0, column = 1)

        # DESC
        desc = tk.Label(self.gui, 
                        text = "Select which format you want your test file to be in\n"+
                        "Select ipynb for a more smooth test",
                        font = ("Helvetica",15), fg = "green")
        desc.grid(row = 1, column=1)

        # txt Button
        self.txt = tk.Button(self.gui, text="txt", font = ("Helvetica", 12), command = self.onTxt)
        self.txt.grid(row = 3, column = 0, padx = 10, pady = 10)

        # ipynb Button
        self.note = tk.Button(self.gui, text="ipynb", font = ("Helvetica", 12), command= self.onIpynb)
        self.note.grid(row = 3, column = 2, padx = 10)

        # Output 
        self.output = tk.Label(self.gui, text = "")
        self.output.grid(row = 3, column= 1)

        # Search bar
        search_label_head = tk.Label(self.gui,
                                     anchor="w",
                                     text = "Use this search bar for accessing solution files\n"+
                                     " Not required for ipynb files",
                                     font = ("Helvetica", 10, "bold"))
        search_label_head.grid(row = 4, column=1, pady = 10)

        self.search_frame = tk.Frame(self.gui)
        self.search_frame.grid(row = 6, column = 1, pady = 10)

        search_label = tk.Label(self.search_frame, text = "Enter Question Here", 
                                font = ("Helvetica", 8, "bold"))
        search_label.pack(side = tk.LEFT)

        self.search_bar = AutocompleteCombobox(self.search_frame, 
                                                   completevalues = self.questions_list, 
                                                   width = 80)
        self.search_bar.pack(side = tk.LEFT, padx = 10)

        self.search_get = tk.Button(self.search_frame, text = "GET SOLUTION", command = self.showSol)
        self.search_get.pack(side = tk.LEFT)

        self.search_output = tk.Label(self.gui, text = "")
        self.search_output.grid(row = 8, column = 1, pady = 10)

    def onTxt(self):
        """ On clicking this button, user decided to make it a txt file"""

        self.testObj.txtOps()
        test_file_name = self.testObj.test_file_path[self.testObj.test_file_path.find("Python_Test"):]
        self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                              fg = "blue", font = ("Helvetica",12))
        self.output.bind("<Button-1>", lambda e: webbrowser.open_new(self.testObj.test_file_path))

    def onIpynb(self):
        """ On clicking this button, user decided to make it a ipynb file"""

        self.testObj.nbOps()
        test_file_name = self.testObj.test_file_path[self.testObj.test_file_path.find("Python_Test"):]
        self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                              fg = "blue", font = ("Helvetica",12))
        self.output.bind("<Button-1>", lambda e: webbrowser.open_new(self.testObj.test_file_path))

    def showSol(self):
        """ For finding the solution file path and presenting it as a link in the GUI"""

        search_bar_output = self.search_bar.get()
        if search_bar_output[0].isdigit():
            search_bar_output = search_bar_output[search_bar_output.find(
                next(filter(str.isalpha, search_bar_output))):]
        if all(search_bar_output not in question for question in self.questions_list):
            self.search_output.configure(text = "Enter the correct question", fg="red")
        else:
            r_line = ""
            r_file_path = ""

            for file_paths in self.testObj.file_paths_list:
                flag = False
                for file_path in file_paths:
                    with open(file_path,"r") as file:
                        lines = file.readlines() 

                        # The questions are written in the first multiline comment in each file
                        for line in lines:
                            # Removing all instances of the comment quotations
                            w_line = line.replace("\"\"\"","")

                            # Writing our line to the test file
                            r_line += w_line

                            # If the string """"\n" is encountered, it means the end of the comment
                            if "\"\"\"\n" in line:
                                break
                    
                    if search_bar_output in r_line:
                        r_file_path = file_path
                        flag = True
                        break
                    else:
                        r_line = ""
                if flag:
                    break

            if r_line != "":
                self.search_output.configure(text = "Solution found! Click me to open the file", fg="blue")
                self.search_output.bind("<Button-1>", lambda e: webbrowser.open_new(r_file_path))

if __name__ == "__main__":
    GUI()
