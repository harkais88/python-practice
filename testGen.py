#!/usr/bin/python3
#Randomly generates a directory consisting of n files from d dirs with n questions 
# each picked from each directory

import os,random
from art import text2art
import nbformat as nbf

class testGen:
    """ Class for generating tests based on the practice files\n
    Use txtOps() for txt file format or nbOps() for ipynb format """

    def __init__(self):
        self.curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.test_dir = "Test Attempts"
        self.file_paths_list = self.getFilesPathsList() 
        self.topic_names_dict = {"bp1": "Basics Part 1", "bp2": "Basics Part 2", "npb": "Numpy Basics"}

    def getTopicDirs(self):
        """ Get the list of all the different topic directories"""

        return [dir for dir in os.listdir(self.curr_dir) 
                if (os.path.isdir(dir) and dir != self.test_dir and dir[0] != "." and dir[0] != "_")]

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

    def txtOps(self, no_of_questions):
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
        test_file.write(text2art("Python Test".center(85), font = "big"))
        # OPTIONAL Heading, comment out the above line, and uncomment out the next line
        # test_file.write("Python Test")

        # Iterating through each list of relative path names of the different topic dirs inside
        # the file_paths_list list
        self.getFilesPathsList()

        for file_paths in self.file_paths_list:
            # To track the files that have been read, and to set it to only read from a set number of files
            file_log = []

            # Writing the topic name as the sub-Header, to distinguish between the different topics...
            # Maybe this won't be required, and in the future, should look into jumbling the order up too
            test_file.write(text2art(
                self.topic_names_dict[file_paths[0][:file_paths[0].find(os.path.basename(file_paths[0]))-1]], 
                font = "standard") + "\n")
            # OPTIONAL: IF DECORATED SUB HEADERS ARE NOT REQUIRED, COMMENT OUT THE ABOVE LINE
            # AND REMOVE COMMENT FROM THE NEXT TWO LINES
            # test_file.write(self.topic_names_dict[file_paths[0][:file_paths[0].find(
            #     os.path.basename(file_paths[0]))-1]])

            # Writing questions from the current topic
            while len(file_log) != no_of_questions:

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
                    # Ignoring any other comment before first multiline comment, 
                    # mainly useful in a Unix environment
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

    def nbOps(self, no_of_questions):
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
                    self.topic_names_dict[file_paths[0][:file_paths[0].find(os.path.basename(file_paths[0]))-1]] + 
                                                        "</h2></b>" +
                                                        "\n"))

            # Bonus: Writing the sub-headers in ASCII Art style
            # nb["cells"].append(nbf.v4.new_markdown_cell(
            #     text2art(file_paths[0][:file_paths[0].find("\\")], font = "ogre").
            #             replace("_","&lowbar;").replace(" ","&#160;").replace("\n","<br>").replace("\\","&bsol;")
            #                                             + "\n"))
            
            # Writing our questions from the current topic
            while len(file_log) != no_of_questions:

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
        self.test_file_path = os.path.abspath(
            os.path.normpath(f"{self.curr_dir}/{self.test_dir}/Python_Test_{file_no}.ipynb"))

        # Creating our test file
        test_file = open(self.test_file_path,"w")

        # After setting our JSON Format using the nb variable,
        # we write to the new notebook using the write function from the nbformat api
        nbf.write(nb,test_file)
        # Then, we close our test file
        test_file.close()

if __name__ == "__main__":
    testObj = testGen()
    testObj.txtOps(3)
    testObj.nbOps(3)