#!/usr/bin/python3

# Creates a GUI using custom tkinter

from testGen import testGen
import customtkinter as ctk
from ttkwidgets.autocomplete import AutocompleteCombobox
from fuzzywuzzy import fuzz
import webbrowser

class cGUI:
    """ Presents a modern-style GUI for the user to decide whether they want\n
        to make the test file a txt file or an ipynb file"""

    def __init__(self):
        #Initializing our testGen Object 
        self.testObj = testGen()    

        # Get Question list for solution finding and autocomplete feature
        self.dir_state = self.getQuestions()
        
        # Setting Appearance and Theme of CTk Window
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Initializing our customtkinter window
        self.cGUI = ctk.CTk()
        self.cGUI.geometry(f"{1053}x{210}+{380}+{350}")
        self.cGUI.title("Python Test Generator")

        # Drawing widgets and handling events 
        self.draw()
        self.cGUI.mainloop()

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
        # MainFrame
        mainframe = ctk.CTkFrame(self.cGUI, 
                                border_width=2, 
                                corner_radius=8)
        mainframe.grid(row = 0, column = 1, rowspan = 7, columnspan = 3, 
                       padx = 10, pady = 10,sticky = "nsew")
        mainframe.grid_rowconfigure(7,weight=20)

        # Heading
        heading = ctk.CTkLabel(mainframe,
                               text = "PYTHON TEST GENERATOR", 
                               text_color="#E1D9D1",
                               font = ("Helvetica",20,"bold"))
        heading.grid(row = 0, column = 1,pady = 5)

        # DESC
        desc = ctk.CTkLabel(mainframe,
                            text = "Select which format you want your test file to be in\n".upper()+
                            "Select ipynb for a more smooth test".upper(),
                            text_color="#19EB87",
                            font = ("Helvetica",12,"bold"))
        desc.grid(row = 1, column = 1, padx = 10, pady = 5)

        # Txt Button
        self.txt = ctk.CTkButton(mainframe,
                                 text = "txt",
                                 font = ("Helvetica",12),
                                 width = 100,
                                 corner_radius=4,
                                 command = self.onTxt)
        self.txt.grid(row = 2, column = 0, padx = 10, pady = 10)

        # Ipynb Button
        self.ipynb = ctk.CTkButton(mainframe,
                                 text = "ipynb",
                                 font = ("Helvetica",12),
                                 width = 100,
                                 corner_radius=4,
                                 command = self.onIpynb)
        self.ipynb.grid(row = 2, column = 2, padx = 10, pady = 10)

        # Output
        self.output = ctk.CTkLabel(mainframe,
                                   text = "")
        self.output.grid(row = 2, column = 1)

        # If directories were detected, with files in them, then we present the Question Toggle
        if self.dir_state: 
            # NO OF QUESTIONS TOGGLE

            # Question Toggle Frame
            question_toggle_frame = ctk.CTkFrame(mainframe, width=230)
            question_toggle_frame.grid(row = 3, column = 1, pady = 10)

            # Getting the max number of questions that would allowed,  
            # assuming there are atleast 3 files in the topic dir(s)
            max_no_of_questions = min([len(file_paths) for file_paths in self.testObj.file_paths_list])
            max_no_of_questions = max_no_of_questions - (max_no_of_questions // 2)

            # Question Toggle Variable
            self.question_var = ctk.IntVar()
            self.question_var.set(max_no_of_questions)
            
            def showQuestionVal(val):
                """ For displaying the current number of questions"""
                question_toggle_value.configure(text = val)
            
            # Question Toggle Label
            question_toggle_head = ctk.CTkLabel(question_toggle_frame,
                                                text = "MAX NO OF QUESTIONS: ",
                                                font = ("Helvetica", 10, "bold"),
                                                text_color="#F5CB64",
                                                anchor = "w",
                                                corner_radius=0)
            question_toggle_head.grid(row = 0, column = 0)

            # Question Toggle Value Display
            question_toggle_value = ctk.CTkLabel(question_toggle_frame,
                                                text = float(self.question_var.get()),
                                                font = ("Helvetica",9,"bold"),
                                                fg_color="#7f7f7f",
                                                height=21,
                                                corner_radius=4)
            question_toggle_value.grid(row = 0, column = 1)

            # Question Toggle Slider
            self.question_toggle = ctk.CTkSlider(question_toggle_frame,
                                                from_= 1,
                                                to = max_no_of_questions,
                                                variable = self.question_var,
                                                number_of_steps= max_no_of_questions-1,
                                                command = showQuestionVal)
            self.question_toggle.grid(row = 1, column = 0, columnspan = 2)

        # Search Frame
        search_frame = ctk.CTkFrame(self.cGUI,
                                    width = 80,
                                    corner_radius=0)
        search_frame.grid(row = 0, column = 0, rowspan = 7, sticky = "nsew")
        search_frame.grid_rowconfigure(7,weight=1)

        # Search Header
        search_header = ctk.CTkLabel(search_frame,
                                    text = "Use this search bar for accessing solution files\n"+
                                     " Not required for ipynb files",
                                    font = ("Helvetica",12,"bold"))
        search_header.grid(row = 0,column = 0, columnspan = 3, padx = 10, pady = 10)

        # Seach Label
        search_label = ctk.CTkLabel(search_frame,
                                    text = "Enter question here",
                                    font = ("Helvetica", 12))
        search_label.grid(row = 2, column = 0, padx = 10, pady = 10)

        # AutoComplete Search Bar
        # In event of no topic dir or empty dir, the questions_list will only have one value
        self.search_bar = AutocompleteCombobox(search_frame,
                                          completevalues=self.questions_list,
                                          width = 50)
        self.search_bar.grid(row = 2, column = 1, columnspan=2, padx = 10)

        # Get Solution Button
        search_get = ctk.CTkButton(search_frame,
                                   text = "GET SOLUTION",
                                   width = 30,
                                   corner_radius=4,
                                   command= self.showSol)
        search_get.grid(row = 3, column = 0, columnspan = 3,pady = 10)

        # Search Output
        self.search_output = ctk.CTkLabel(search_frame,
                                           text = "")
        self.search_output.grid(row = 5, column = 0, columnspan = 3)

        # Theme Toggle
        
        self.switch_var = ctk.StringVar()
        self.switch_var.set("dark")

        def switch_event():
            ctk.set_appearance_mode(self.switch_var.get())
            if self.switch_var.get() == "dark":
                # FOR DARK THEME

                heading.configure(text_color = "#E1D9D1", font = ("Helvetica",20,"bold"))
                question_toggle_head.configure(text_color = "#F5CB64")
                question_toggle_value.configure(fg_color="#7f7f7f")
                desc.configure(text_color = "#19EB87")
            else:
                # FOR WHITE THEME

                heading.configure(text_color = "black", font = ("Helvetica",20,"bold"))
                question_toggle_head.configure(text_color = "#D4A019")
                question_toggle_value.configure(fg_color="#FFFEF2")
                desc.configure(text_color = "#008F11")

        theme_toggle = ctk.CTkSwitch(search_frame,
                                     text = "THEME",
                                     command=switch_event,
                                     variable = self.switch_var,
                                     offvalue= "dark",
                                     onvalue="light")
        theme_toggle.grid(row = 7, column = 1)

    def onTxt(self):
        """ On clicking this button, user decided to make it a txt file"""

        # If there are topic dirs with files in them, then this gets executed
        if self.dir_state:
            no_of_questions = self.question_var.get()
            self.testObj.txtOps(no_of_questions)
            test_file_name = self.testObj.test_file_path[self.testObj.test_file_path.find("Python_Test"):]
            self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                                 text_color = "#DC143C", font = ("Helvetica",12))
            self.output.bind("<Button-1>", lambda e: webbrowser.open_new(self.testObj.test_file_path))
        # Otherwise the error message will be presented
        else:
            self.output.configure(text = "Please make sure there are topic dirs with code files in them\n"+
                                  "in the same dir as the scripts",
                                  text_color = "#0047AB", font = ("Helvetica",12))

    def onIpynb(self):
        """ On clicking this button, user decided to make it a ipynb file"""

        # If there are questions detected, then test files will be created
        if self.dir_state:
            no_of_questions = self.question_var.get()
            self.testObj.nbOps(no_of_questions)
            test_file_name = self.testObj.test_file_path[self.testObj.test_file_path.find("Python_Test"):]
            self.output.configure(text = f"{test_file_name} created! Click on me to check me out",
                                     text_color = "#DC143C", font = ("Helvetica",12))
            self.output.bind("<Button-1>", lambda e: webbrowser.open_new(self.testObj.test_file_path))
        # Otherwise the error message will be presented                 
        else:
            self.output.configure(text = "Please make sure there are topic dirs with code files in them\n" +
                                  "in the same dir as the scripts",
                                  text_color = "#0047AB", font = ("Helvetica",12))

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
                self.search_output.configure(text = "Enter the correct question", text_color="red")
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
                self.search_output.configure(text = "Solution found! Click me to open the file", text_color="blue")
                self.search_output.bind("<Button-1>", lambda e: webbrowser.open_new(solution_path))

        # If no questions were found        
        else:
            self.search_output.configure(text = "NO FILES FOUND!", text_color = "blue")

if __name__ == "__main__":
    cGUI()