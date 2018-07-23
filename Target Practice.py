import tkinter as tk
import turtle
import random

class Darts:
    def __init__(self):
        self.scores = [500, 700]
        self.main_window = tk.Tk()
      #  self.newgame_window = tk.Tk()

        #create frames for start screen
        self.title_frame = tk.Frame(self.main_window)
        self.buttons_frame = tk.Frame(self.main_window)
        self.version_frame = tk.Frame(self.main_window)

        #create title/label
        self.title_label = tk.Label(self.title_frame, text = "Welcome to Darts 2DX")
        self.title_label.pack()

        #create buttons
        self.newGame_button = tk.Button(self.buttons_frame, text = "New Game",
                                        command = self.chooseOptions, bg = 'green') 
        self.highScores_button = tk.Button(self.buttons_frame, text = "High Scores",
                                           command = self.open_scores, bg = 'orange')
        self.quit_button = tk.Button(self.buttons_frame, text='Exit Game',
                                     command=self.main_window.destroy, bg = 'red')
        self.newGame_button.pack()
        self.highScores_button.pack()
        self.quit_button.pack()

        #version by bottom label
        self.version_label = tk.Label(self.version_frame, text = "version: s.r.0.5")
        self.version_label.pack()

        self.title_frame.pack()
        self.buttons_frame.pack()
        self.version_frame.pack()

        tk.mainloop()
  

    #!!!options (2n !window! for a new game
    def chooseOptions(self):
        self.main_window.destroy() #close main window
        self.options_window = tk.Tk()

        #create frames for Options New Game(2nd) window
        self.optionsTitle_frame = tk.Frame(self.options_window)
        self.color_frame = tk.Frame(self.options_window)
        self.difficulty_frame = tk.Frame(self.options_window)
        self.startButton_frame = tk.Frame(self.options_window)

        #create title: Options
        self.optionsTitle_label = tk.Label(self.optionsTitle_frame,
                                           text = "OPTIONS",
                                           font = ('Arial', 15))
        self.optionsTitle_label.pack()

    #1st option: Color (title and radiobutton choices underneath)
        #1. Choose Color label
        self.color_label = tk.Label(self.color_frame,
                                    text = "\nChoose Color",
                                    font =('Arial', 12))
        self.color_label.pack()

        #2. color radiobuttons
            #StringVar for radiobuttons
        self.color_rb_var = tk.StringVar(value='green')
            #set StringVar to green
        #self.color_rb_var.set('green')

            #create the radiobutton widgets for color in options frame
        self.yellow_rb = tk.Radiobutton(self.color_frame,
                                        text = 'Purple',
                                        bg = 'purple',
                                        variable = self.color_rb_var,
                                        value = 'purple',
                                        tristatevalue=0)
                                        #command = self.'add method )
        self.green_rb = tk.Radiobutton(self.color_frame,
                                        text = 'Green',
                                        bg = 'green',
                                        variable = self.color_rb_var,
                                        value = 'green')
        self.red_rb = tk.Radiobutton(self.color_frame,
                                        text = 'Red',
                                        bg = 'red',
                                        variable = self.color_rb_var,
                                        value = 'red',
                                         tristatevalue=0)
        self.blue_rb = tk.Radiobutton(self.color_frame,
                                        text = 'Blue',
                                        bg = 'blue',
                                        variable = self.color_rb_var,
                                        value = 'blue',
                                        tristatevalue=0 )

        self.yellow_rb.pack(side = 'left')
        self.green_rb.pack(side = 'left')
        self.red_rb.pack(side = 'left')
        self.blue_rb.pack(side = 'left')

        #3. Choose Difficulty label
        self.difficulty_label = tk.Label(self.difficulty_frame,
                                    text = "\nChoose Difficulty",
                                    font = ('Arial', 12))
        self.difficulty_label.pack()

        #4. difficulty radiobuttons
            #StringVar for radiobuttons
        self.difficulty_rb_var = tk.StringVar()
            #set StringVar to easy
        self.difficulty_rb_var.set('easy')

            #create the radiobutton widgets for difficulty in options frame
        self.easy_rb = tk.Radiobutton(self.difficulty_frame,
                                      text = 'Easy',
                                      fg = 'chartreuse',
                                      variable = self.difficulty_rb_var,
                                      value = 'easy')
                                      
        self.hard_rb = tk.Radiobutton(self.difficulty_frame,
                                      text = 'Hard',
                                      fg = 'dark red',
                                      variable = self.difficulty_rb_var,
                                      value = 'hard',
                                      tristatevalue=0)
        self.easy_rb.pack(side = 'left')
        self.hard_rb.pack(side = 'left')

    #start game button
        self.start_button = tk.Button(self.startButton_frame,
                                      text = 'Start Game',
                                      command = self.game)
                                        #command to link to board for game
        self.start_button.pack()

        #pack frames
        self.optionsTitle_frame.pack()
        self.color_frame.pack()
        self.difficulty_frame.pack()
        self.startButton_frame.pack()
        
    def game(self):
        self.options_window.destroy()
        
        # Named constants
        self.SCREEN_WIDTH = 600    # Screen width
        self.SCREEN_HEIGHT = 600   # Screen height
        
        if self.difficulty_rb_var.get() == 'easy':    #easy mode settings = square double size (50)
            self.TARGET_LLEFT_X = random.randint(-289,245)  # Target's lower-left X
            self.TARGET_LLEFT_Y = random.randint (-289, 245) # Target's lower-left Y
            self.TARGET_WIDTH = 50     # Width of the target

        elif self.difficulty_rb_var.get() == 'hard':     #hard mode = square 25 width
            self.TARGET_LLEFT_X = random.randint(-289,265)  # Target's lower-left X
            self.TARGET_LLEFT_Y = random.randint (-289, 265) # Target's lower-left Y
            self.TARGET_WIDTH = 25     # Width of the target


        self.FORCE_FACTOR = 30     # Arbitrary force factor
        self.PROJECTILE_SPEED = 1  # Projectile's animation speed
        self.NORTH = 90            # Angle of north direction
        self.SOUTH = 270           # Angle of south direction
        self.EAST = 0              # Angle of east direction
        self.WEST = 180            # Angle of west direction

        # Setup the window.
        turtle.setup(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        # Draw the target.
        turtle.hideturtle()
        turtle.speed(0)
        turtle.penup()
        turtle.goto(self.TARGET_LLEFT_X, self.TARGET_LLEFT_Y)
        turtle.pendown()
        turtle.setheading(self.EAST)
        turtle.forward(self.TARGET_WIDTH)
        turtle.setheading(self.NORTH)
        turtle.forward(self.TARGET_WIDTH)
        turtle.setheading(self.WEST)
        turtle.forward(self.TARGET_WIDTH)
        turtle.setheading(self.SOUTH)
        turtle.forward(self.TARGET_WIDTH)
        
        #Draw inner target
        turtle.hideturtle()
        turtle.speed(0)
        turtle.penup()

        self.inner_width = self.TARGET_WIDTH * .4
        self.inner_target_x = self.TARGET_LLEFT_X + (.3 * self.TARGET_WIDTH)
        self.inner_target_y = self.TARGET_LLEFT_Y + (.3 * self.TARGET_WIDTH)

        turtle.goto(self.inner_target_x, self.inner_target_y)
        turtle.pendown()
        turtle.setheading(self.EAST)
        turtle.forward(self.inner_width)
        turtle.setheading(self.NORTH)
        turtle.forward(self.inner_width)
        turtle.setheading(self.WEST)
        turtle.forward(self.inner_width)
        turtle.setheading(self.SOUTH)
        turtle.forward(self.inner_width)

        #change turtle color
        turtle.color(self.color_rb_var.get())
        

        self.lives = 3
        self.score = 0
        while (self.lives > 0):
            # Center the turtle.
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.setheading(self.EAST)
            turtle.showturtle()
            turtle.speed(self.PROJECTILE_SPEED)

            
            # Get the angle and force from the user.
            self.angle = float(input("\nEnter the projectile's angle: "))
            self.force = float(input("Enter the launch force (1-12): "))

            # Calculate the distance.
            self.distance = self.force * self.FORCE_FACTOR

            # Set the heading.
            turtle.setheading(self.angle)

            # Launch the projectile.
            turtle.pendown()
            turtle.forward(self.distance)

            # Did it hit the target?
            #main target
            if (turtle.xcor() >= self.TARGET_LLEFT_X and
                turtle.xcor() <= (self.TARGET_LLEFT_X + self.TARGET_WIDTH) and
                turtle.ycor() >= self.TARGET_LLEFT_Y and
                turtle.ycor() <= (self.TARGET_LLEFT_Y + self.TARGET_WIDTH)):
                self.score += 100
                #extra 100 if inner target hit
                if (turtle.xcor() >= self.inner_target_x and
                turtle.xcor() <= (self.inner_target_x + self.inner_width) and
                turtle.ycor() >= self.inner_target_y and
                turtle.ycor() <= (self.inner_target_y + self.inner_width)):
                    self.score += 100

                print('Target hit! Your score is now: ' + str(self.score))
                tk.messagebox.showinfo('You hit the target!', 'Great, you hit the target!')

                #clear board
                turtle.clear()

                if self.difficulty_rb_var.get() == 'easy':    #easy mode settings = square double size (50)
                    self.TARGET_LLEFT_X = random.randint(-289,245)  # Target's lower-left X
                    self.TARGET_LLEFT_Y = random.randint (-289, 245) # Target's lower-left Y
                    self.TARGET_WIDTH = 50     # Width of the target

                elif self.difficulty_rb_var.get() == 'hard':     #hard mode = square 25 width
                    self.TARGET_LLEFT_X = random.randint(-289,265)  # Target's lower-left X
                    self.TARGET_LLEFT_Y = random.randint (-289, 265) # Target's lower-left Y
                    self.TARGET_WIDTH = 25     # Width of the target
                # Draw the target.
                turtle.hideturtle()
                turtle.speed(0)
                turtle.penup()
                turtle.goto(self.TARGET_LLEFT_X, self.TARGET_LLEFT_Y)
                turtle.pendown()
                turtle.setheading(self.EAST)
                turtle.forward(self.TARGET_WIDTH)
                turtle.setheading(self.NORTH)
                turtle.forward(self.TARGET_WIDTH)
                turtle.setheading(self.WEST)
                turtle.forward(self.TARGET_WIDTH)
                turtle.setheading(self.SOUTH)
                turtle.forward(self.TARGET_WIDTH)

                #Draw inner target
                turtle.hideturtle()
                turtle.speed(0)
                turtle.penup()

                self.inner_width = self.TARGET_WIDTH * .4
                self.inner_target_x = self.TARGET_LLEFT_X + (.3 * self.TARGET_WIDTH)
                self.inner_target_y = self.TARGET_LLEFT_Y + (.3 * self.TARGET_WIDTH)

                turtle.goto(self.inner_target_x, self.inner_target_y)
                turtle.pendown()
                turtle.setheading(self.EAST)
                turtle.forward(self.inner_width)
                turtle.setheading(self.NORTH)
                turtle.forward(self.inner_width)
                turtle.setheading(self.WEST)
                turtle.forward(self.inner_width)
                turtle.setheading(self.SOUTH)
                turtle.forward(self.inner_width)
                
            else:
                self.lives -= 1
                print('You missed the target. You now have ' + str(self.lives) + ' lives.' +
                          '\nYour score is: ' + str(self.score) )

        #Game Over (lives = 0)
        tk.messagebox.showinfo('Game Over', 'Game Over! Your score is ' +
                               str(self.score) + '!!!')
        self.enter_score()

    def enter_score(self):
        self.enterScore_window = tk.Tk()

        #frames
        self.score_title_frame = tk.Frame(self.enterScore_window)
        self.score_entername_frame = tk.Frame(self.enterScore_window)
        self.score_enterbutton_frame = tk.Frame(self.enterScore_window)

        #title label including score
        self.score_title_label = tk.Label(self.score_title_frame,
                                          text = 'Congrats! Your score is: ' +
                                          str(self.score))
        self.score_title_label.pack()

        #create Label and Entry to enter name
        self.name_label = tk.Label(self.score_entername_frame,
                                   text = '\nYou made the top 10 list, Enter Your Initials: ')
        self.name_entry = tk.Entry(self.score_entername_frame, width = 10)
        self.name_label.pack(side = 'left')
        self.name_entry.pack(side = 'left')

        #create button to enter name
        self.enter_button = tk.Button(self.score_enterbutton_frame, text = 'Enter',
                                      command = self.writeScoreToFile)
        self.enter_button.pack()

        #pack frames
        self.score_title_frame.pack()
        self.score_entername_frame.pack()
        self.score_enterbutton_frame.pack()


        #label to enter score name
        #if score is high enough, enter name

    def writeScoreToFile(self):

        outfile = open('scores.txt', 'a')

        self.iname = self.name_entry.get()
        outfile.write(str(self.iname) + '\t' + str(self.score) + '\n')
        self.enterScore_window.destroy()

        outfile.close()
        

    def open_scores(self):
        #open file to read to GUI window
        infile = open('scores.txt', 'r')

        self.scores_window = tk.Tk()

        self.scoresTitle_frame = tk.Frame(self.scores_window)
        self.scores_frame = tk.Frame(self.scores_window)

        #create title: High Scores
        self.scoresTitle_label = tk.Label(self.scoresTitle_frame,
                                           text = "HIGH SCORES")
        self.scoresTitle_label.pack()

        #create listbox to display scores
        self.score_listbox = tk.Listbox(self.scores_frame, width = 30, height = 32)
        self.score_listbox.pack()      

        #add scores to list
        for line in infile:
            self.score_listbox.insert(tk.END, line)

        self.scoresTitle_frame.pack()
        self.scores_frame.pack()


darts = Darts()        
 