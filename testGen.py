#!/usr/bin/python3
#Randomly generates a directory consisting of n files from d dirs with n questions 
# each picked from each directory

import os,random
from art import text2art
import nbformat as nbf
import tkinter as tk
import webbrowser

class testGen:
    """ Class for generating tests based on the practice files\n
    Use txtOps() for txt file format or nbOps() for ipynb format """

    curr_dir = os.path.dirname(os.path.realpath(__file__))
    test_dir = "Test Attempts"

    def getTopicDirs(self):
        """ Get the list of all the different topic directories"""

        return [dir for dir in os.listdir(self.curr_dir) if (os.path.isdir(dir) and dir != self.test_dir and dir[0] != ".")]

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
        file_no = len([file for file in os.listdir(f"{self.curr_dir}/{self.test_dir}") if file.endswith(".txt")]) + 1

        # Setting Test File Path
        self.test_file_path = os.path.abspath(os.path.normpath(f"{self.curr_dir}/{self.test_dir}/Python_Test_{file_no}.txt"))

        # Creating our test file
        test_file = open(self.test_file_path,"w")
        
        # Heading
        test_file.write(text2art("Python Test".center(85), font = "ogre"))

        # Iterating through each list of relative path names of the different topic dirs inside
        # the file_paths_list list 
        for file_paths in self.getFilesPathsList():
            # To track the files that have been read, and to set it to only read from a set number of files
            file_log = []

            # Writing the topic name as the sub-Header, to distinguish between the different topics...
            # Maybe this won't be required, and in the future, should look into jumbling the order up too
            test_file.write(text2art(file_paths[0][:file_paths[0].find(os.path.basename(file_paths[0]))-1], font = "ogre") + "\n")

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
        for file_paths in self.getFilesPathsList():
            # To track the files that have been read, and to set it to only read from a set number of files
            file_log = []

            # Writing the topic name as a sub-header

            nb["cells"].append(nbf.v4.new_markdown_cell("<h2><b>" + 
                                                        file_paths[0][:file_paths[0].find("\\")] 
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

                # Setting our result variable
                # Should contain the entire question
                r_line = ""

                # Iterating through each line in the file
                for line in lines:

                    # Removing any """ found
                    # Replacing \n with <br> and \t with &#160; 4 times for HTML formatting
                    f_line = line.replace("\"\"\"","").replace("\n","<br>").replace("\t","&#160;"*4)
                    # If needed, you can set it to the exact format given in the files
                    # w_line = "<pre>"+w_line+"</pre>"

                    # Adding our formatted line to the result variable
                    r_line += f_line

                    # If """\n exists in the line, it means we reached the end of the multiline comment
                    # It also coincidentally means we reached the end of our question too
                    if "\"\"\"\n" in line:
                        break
                
                # Creating a new markdown cell with the result variable, thus writing a new question
                nb["cells"].append(nbf.v4.new_markdown_cell(str(len(file_log)+1) + ". "+ 
                                                            r_line))
                # Creating a code space for the user to test their code on
                nb["cells"].append(nbf.v4.new_code_cell(code_lines))

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
    def __init__(self):
        """ Presents a GUI for the user to decide whether they want\n
        to make the test file a txt file or an ipynb file"""

        self.gui = tk.Tk()
        self.gui.title("Python Test Generator")
        self.draw()
        self.gui.mainloop()

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

    def onTxt(self):
        """ On clicking this button, user decided to make it a txt file"""

        testObj = testGen()
        testObj.txtOps()
        test_file_name = testObj.test_file_path[testObj.test_file_path.find("Python_Test"):]
        self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                              fg = "blue", font = ("Helvetica",12))
        self.output.bind("<Button-1>", lambda e: webbrowser.open_new(testObj.test_file_path))

    def onIpynb(self):
        """ On clicking this button, user decided to make it a ipynb file"""

        testObj = testGen()
        testObj.nbOps()
        test_file_name = testObj.test_file_path[testObj.test_file_path.find("Python_Test"):]
        self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                              fg = "blue", font = ("Helvetica",12))
        self.output.bind("<Button-1>", lambda e: webbrowser.open_new(testObj.test_file_path))

if __name__ == "__main__":
    GUI()
