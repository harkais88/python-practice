#!/usr/bin/python3

# Creates a GUI using tkinter

from testGen import testGen
import tkinter as tk
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from fuzzywuzzy import fuzz
import webbrowser

class GUI:
    """ Presents a GUI for the user to decide whether they want\n
        to make the test file a txt file or an ipynb file"""

    def __init__(self):
        #Initializing our testGen Object
        self.testObj = testGen()

        # Get Question list for solution finding and autocomplete feature
        self.dir_state = self.getQuestions()

        # Initializing our tkinter window
        self.gui = tk.Tk()
        self.gui.title("Python Test Generator")
        # Drawing widgets and handling events 
        self.draw()
        self.gui.mainloop()

    def getQuestions(self):
        """ Get all the questions in all the topic dirs in a single list"""

        self.questions_list = []

        # Check if the topic directories are there, and there are any files in there
        if len(self.testObj.file_paths_list) == 0:                   
            self.questions_list.append("NO DIRECTORIES FOUND")
        elif all(len(file) == 0 for file in self.testObj.file_paths_list):
            self.questions_list.append("NO FILES FOUND UNDER DIRECTORIES")
        else:
            r_line = ""

            for file_paths in self.testObj.file_paths_list:
                # Accessing each file in each topic dir
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

                    # Appending question to our list
                    self.questions_list.append(r_line)
                    r_line = "" 

            # This means that questions were found
            return True   
        # This means that either the dirs were empty, or the dirs did not exist at all 
        return False
    
    def draw(self):
        """ Responsible for drawing GUI Elements"""

        # HEADING
        heading = tk.Label(self.gui, text = "Python Test Generator!", font = ("Helvetica",20))
        heading.grid(row = 0, column = 1, pady=10)

        # If directories were detected, with files in them, then we present the Question Toggle
        if self.dir_state:
            # NO OF QUESTIONS TOGGLE

            # Question Toggle Frame
            question_toggle = tk.Frame(self.gui)
            question_toggle.grid(row = 1, column = 1, padx = 10)

            # Getting the max number of questions that would allowed,  
            # assuming there are atleast 3 files in the topic dir(s)
            max_no_of_questions = min([len(file_paths) for file_paths in self.testObj.file_paths_list])
            max_no_of_questions = max_no_of_questions - (max_no_of_questions // 2)

            # Question Toggle Label
            question_toggle_label = tk.Label(question_toggle, 
                                            text = f"No Of Questions (Max: {max_no_of_questions})",
                                            font = ("Helvetica",8,"bold"),
                                            fg = "black")
            question_toggle_label.grid(row = 0, column = 0, padx = 10)

            # Question Toggle Variable
            self.question_var = tk.StringVar()
            self.question_var.set(str(max_no_of_questions))

            # Question Toggle Spinbox
            self.quest_no_set = ttk.Spinbox(question_toggle,
                                            from_ = 1, 
                                            to = max_no_of_questions,
                                            width = 5,
                                            textvariable=self.question_var)
            self.quest_no_set.grid(row = 0, column = 1, padx = 10)

        # DESC
        desc = tk.Label(self.gui, 
                        text = "Select which format you want your test file to be in\n"+
                        "Select ipynb for a more smooth test",
                        font = ("Helvetica",15), fg = "green")
        desc.grid(row = 3, column=1)

        # txt Button
        self.txt = tk.Button(self.gui, text="txt", font = ("Helvetica", 12), command = self.onTxt)
        self.txt.grid(row = 5, column = 0, padx = 10, pady = 10)

        # ipynb Button
        self.note = tk.Button(self.gui, text="ipynb", font = ("Helvetica", 12), command= self.onIpynb)
        self.note.grid(row = 5, column = 2, padx = 10)

        # Output 
        self.output = tk.Label(self.gui, text = "")
        self.output.grid(row = 5, column= 1)

        # Search bar
        search_label_head = tk.Label(self.gui,
                                     anchor="w",
                                     text = "Use this search bar for accessing solution files\n"+
                                     " Not required for ipynb files",
                                     font = ("Helvetica", 10, "bold"))
        search_label_head.grid(row = 6, column=1, pady = 10)

        # Search Frame
        self.search_frame = tk.Frame(self.gui)
        self.search_frame.grid(row = 8, column = 1, pady = 10)

        # Search Frame Label
        search_label = tk.Label(self.search_frame, text = "Enter Question Here", 
                                font = ("Helvetica", 8, "bold"))
        search_label.pack(side = tk.LEFT)

        # Search Frame Bar
        self.search_bar = AutocompleteCombobox(self.search_frame, 
                                                   completevalues = self.questions_list, 
                                                   width = 80)
        self.search_bar.pack(side = tk.LEFT, padx = 10)

        # Search Frame Button
        self.search_get = tk.Button(self.search_frame, text = "GET SOLUTION", command = self.showSol)
        self.search_get.pack(side = tk.LEFT)

        # Search output
        self.search_output = tk.Label(self.gui, text = "")
        self.search_output.grid(row = 10, column = 1, pady = 10)

    def onTxt(self):
        """ On clicking this button, user decided to make it a txt file"""

        # If there are questions detected, then test files will be created
        if self.dir_state:
            no_of_questions = self.question_var.get()
            self.testObj.txtOps(int(no_of_questions))
            test_file_name = self.testObj.test_file_path[self.testObj.test_file_path.find("Python_Test"):]
            self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                                fg = "blue", font = ("Helvetica",12))
            self.output.bind("<Button-1>", lambda e: webbrowser.open_new(self.testObj.test_file_path))
        # Otherwise the error message will be presented
        else:
            self.output.configure(text = "Please make sure there are topic dirs with code files in them\n"+
                                  "in the same dir as the scripts",
                                  fg = "red", font = ("Helvetica",12))

    def onIpynb(self):
        """ On clicking this button, user decided to make it a ipynb file"""

        # If there are questions detected, then test files will be created
        if self.dir_state:
            no_of_questions = self.question_var.get()
            self.testObj.nbOps(int(no_of_questions))
            test_file_name = self.testObj.test_file_path[self.testObj.test_file_path.find("Python_Test"):]
            self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                                fg = "blue", font = ("Helvetica",12))
            self.output.bind("<Button-1>", lambda e: webbrowser.open_new(self.testObj.test_file_path))
        # Otherwise the error message will be presented        
        else:
            self.output.configure(text = "Please make sure there are topic dirs with code files in them\n"+
                                  "in the same dir as the scripts",
                                  fg = "red", font = ("Helvetica",12))

    def showSol(self):
        """ For finding the solution file path and presenting it as a link in the GUI"""

        # If questions were found
        if self.dir_state:
            # Get the value of the search bar
            search_bar_output = self.search_bar.get()
            # Check if search bar output is valid, as it could happen that a question is copied 
            # with the question number with it
            if not search_bar_output[0].isalpha():
                search_bar_output = search_bar_output[search_bar_output.find(
                    next(filter(str.isalpha, search_bar_output))):]
            # Checking if search bar output is a question available in the topic dirs
            # Using Levenshtein Distance to find similarity of strings
            if all(fuzz.ratio(search_bar_output,question) < 80 for question in self.questions_list):
                self.search_output.configure(text = "Enter the correct question", fg="red")
            else:
                r_line = ""
                file_path_log = {}

                # Iterating through each topic dir
                for file_paths in self.testObj.file_paths_list:
                    # Iterating through each file in a topic dir
                    for file_path in file_paths:
                        #Extracting the first multiline comment
                        with open(file_path,"r") as file:
                            lines = file.readlines() 

                            # The questions are written in the first multiline comment in each file
                            for line in lines:
                                if "#" in line or line == "\n":
                                    continue

                                # Removing all instances of the comment quotations
                                w_line = line.replace("\"\"\"","")

                                # Writing our line to the test file
                                r_line += w_line

                                # If the string """"\n" is encountered, it means the end of the comment
                                if "\"\"\"\n" in line:
                                    break
                        
                        # Logging the Levenshtein Distance calculated between the 
                        # search bar output and the extracted multiline comment
                        file_path_log[file_path] = fuzz.ratio(search_bar_output,r_line)
                        r_line = ""

                # Finding the path that had the highest Levenshtein Distance score
                solution_path = next(iter(file_path_log))
                for path in file_path_log:
                    if file_path_log[path] > file_path_log[solution_path]:
                        solution_path = path

                # Showing output to GUI
                self.search_output.configure(text = "Solution found! Click me to open the file", fg="blue")
                self.search_output.bind("<Button-1>", lambda e: webbrowser.open_new(solution_path))

        # If no questions were found
        else:
            self.search_output.configure(text = "NO FILES FOUND", fg = "blue")

if __name__ == "__main__":
    GUI()