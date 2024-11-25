from operator import iconcat
from tkinter import *                                       # Importing Tkinter
import tkinter.messagebox                                   # Importing Messsagebox function
from PIL import ImageTk, Image                              # Importing Image & Pillow for image manipulation
import sqlite3                                              # Importing Sqlite3

# ------------------------------ Creating Database ------------------------------ #
connection = sqlite3.connect("Spotify.db")                  # Creating a database
cur        = connection.cursor()                            # Creating a cursor
cur.execute(''' CREATE TABLE IF NOT EXISTS users(
                UserID      INTEGER PRIMARY KEY AUTOINCREMENT,
                Email       TEXT UNIQUE,
                Name        TEXT UNIQUE,
                Password    TEXT)
            ''')
# write changes to the database
connection.commit()




def Spotify():                                              # Defining Spotify function
    rootLayout = Tk()                                       # Creating a root layout
    rootLayout.title("Spotify")                             # Giving title to the root layout
    rootLayout.geometry("{0}x{1}+0+0".format(rootLayout.winfo_screenwidth(), rootLayout.winfo_screenheight()))
    rootLayout.overrideredirect(False)                      # Showing windows borders Initially
    rootLayout.attributes("-fullscreen", True)              # Setting fullscreen mode
    rootLayout.config(bg="#2F2F2F")                         # Setting background color
    rootLayout.attributes('-alpha', 0.95)                   # Setting transparency
    rootLayout.iconbitmap('images/spotifyLogo.ico')         # Setting icon

    # Variable to track maximize state
    is_maximized = [True]                 # Using a list to make it mutable in nested function

    # ------------------------ All Windows Functions ------------------------ #
    def closeApplication():                                 # Defining closeApplication function
        MessageBox = tkinter.messagebox.askquestion("EXIT",                               # Title
                                                    "Are you sure you want to exit?", # Message
                                                    icon="warning")                            # Icon
        if MessageBox == "yes":                             # If Yes
            rootLayout.destroy()                            # Destroying the root layout

    def minimizeApplication():                              # Defining minimizeApplication function
        rootLayout.iconify()

    def maximizeApplication():
        if is_maximized[0]:
            rootLayout.attributes("-fullscreen", False)         # Exit fullscreen
            rootLayout.update_idletasks()                       # Update window info to get screen dimensions
            screen_width = rootLayout.winfo_screenwidth()       # Get screen width
            screen_height = rootLayout.winfo_screenheight()     # Get screen height
            new_width = int(screen_width * 0.9)                 # 90% of screen width
            new_height = int(screen_height * 0.9)               # 90% of screen height
            x_position = (screen_width - new_width) // 2        # Calculate x position to center
            y_position = (screen_height - new_height) // 2      # Calculate y position to center
            rootLayout.geometry(f"{new_width}x{new_height}+{x_position}+{y_position}")
            rootLayout.after(10, lambda: rootLayout.geometry(f"{new_width}x{new_height}+{x_position}+{y_position}"))

        else:
            rootLayout.attributes("-fullscreen", True)          # Set fullscreen mode
        is_maximized[0] = not is_maximized[0]                   # Toggle state

    def buttonHover(button, colorOnHover, colorOnLeave):                           # Defining buttonHover function
        button.bind("<Enter>", func=lambda e: button.config(                       # Hovering the button
            background=colorOnHover                                                # Setting background color
        ))
        button.bind("<Leave>", func=lambda e: button.config(                       # Leaving the button
            background=colorOnLeave                                                # Setting background color
        ))


































    controlBox = Frame(rootLayout,                          # Creating a control box
                       height=50,                           # Setting height
                       relief="solid",                      # Setting border style
                       highlightthickness=1,                # Setting border thickness
                       background="#222222",                # Setting background color
                       highlightbackground="#2F2F2F")       # Setting border color
    controlBox.pack(side=TOP, anchor=NE, fill="x")          # Placing the control box

    #------ Inserting Control Box Images ------ #
    closeImage     = Image.open("images/close.png").resize((25, 25))            # Resizing Original Image
    newClose       = ImageTk.PhotoImage(closeImage)        # Assigning Image to object

    maximizeImage  = Image.open("images/maximize.png")      # Opening maximize image
    resizeMaximize = maximizeImage.resize((25, 25))         # Resizing Original Image
    newMaximize    = ImageTk.PhotoImage(resizeMaximize)     # Assigning Image to object

    minimizeImage  = Image.open("images/minimize2.png")      # Opening minimize image
    resizeMinimize = minimizeImage.resize((25, 25))         # Resizing Original Image
    newMinimize    = ImageTk.PhotoImage(resizeMinimize)     # Assigning Image to object

    appLogo        = Image.open("images/spotifyLogo.ico")   # Opening logo image
    resizeLogo     = appLogo.resize((25, 25))               # Resizing Original Image
    newLogo        = ImageTk.PhotoImage(resizeLogo)         # Assigning Image to object


    # ------ Creating Control Box Buttons ------ #
    closeButton    = Button(controlBox,                      # Creating close button
                            bg="#222222",                    # Setting background color
                            width=50,                        # Setting width
                            height=50,                       # Setting height
                            image=newClose,                  # Setting image
                            border=0,                        # Removing border
                            command=closeApplication)                      # Assigning Function to button
    closeButton.image = newClose                             # Assigning Image to object
    closeButton.pack(side=RIGHT)                             # Placing the button
    buttonHover(closeButton, "#ff0000", "#222222")

    maximizeButton = Button(controlBox,                      # Creating maximize button
                            bg="#222222",                    # Setting background color
                            width=50,                        # Setting width
                            height=50,                       # Setting height
                            image=newMaximize,               # Setting image
                            border=0,                        # Removing border
                            command=maximizeApplication)                      # Assigning Function to butto
    maximizeButton.image = newMaximize                       # Assigning Image to object
    maximizeButton.pack(side=RIGHT)                          # Placing the button
    buttonHover(maximizeButton, "#1ED760", "#222222")


    minimizeButton = Button(controlBox,                      # Creating minimize button
                            bg="#222222",                    # Setting background color
                            width=50,                        # Setting width
                            height=50,                       # Setting height
                            image=newMinimize,               # Setting image
                            border=0,                        # Removing border
                            command=minimizeApplication)                      # Assigning Function to button
    minimizeButton.image = newMinimize                       # Assigning Image to object
    minimizeButton.pack(side=RIGHT)                          # Placing the button
    buttonHover(minimizeButton, "#1ED760", "#222222")

    appLogoButton = Button(controlBox,                       # Creating minimize button
                            bg="#222222",                    # Setting background color
                            width=50,                        # Setting width
                            height=50,                       # Setting height
                            image=newLogo,                   # Setting image
                            border=0,                        # Removing border
                            command="")                      # Assigning Function to button
    appLogoButton.image = newLogo                            # Assigning Image to object
    appLogoButton.pack(side=LEFT)                            # Placing the button
    imageGrid(rootLayout)                                    # Calling ImageGrid function


def imageGrid(rootLayout):                                   # Defining imageGrid function
    imageFrame =Frame(rootLayout,                            # Creating  image frame
                     bg="#2F2F2F")                           # Setting background color
    imageFrame.place(relx=0.06, rely=0.18, relwidth=0.9, relheight=0.75) # Placing image frame to occupy 90

    images = []                                                                 # Loading & arranging 12 images
    for i in range(12):                                                         # Looping 12 times
        img = Image.open(f"images/image{i+1}.png").resize((250, 250))           # Opening images
        images.append(ImageTk.PhotoImage(img))                                  # Assigning Image to object

    for i in range(6):                                                          # Placing images 6 at the top
        (Label(imageFrame, image=images[i],
              bg="#2F2F2F")
         .grid(row=0, column=i, padx=10, pady=10))

    for i in range(6, 12):                                                      # Placing images 6 at the bottom
        (Label(imageFrame, image=images[i],
              bg="#2F2F2F")
         .grid(row=1, column=i-6, padx=10, pady=10))

    rootLayout.images = images                                                 # Assigning Image to object
    musicControls(rootLayout)                                                  # Calling musicControls function

def musicControls(rootLayout):
    #
    controlFrame = Frame(rootLayout, bg="#1C1C1C", height=100)                 # Creating control frame
    controlFrame.pack(side=BOTTOM, fill="x")                                   # Placing the frame


    buttonFrame = Frame(controlFrame, bg="#1C1C1C")                           # Create a frame to hold the buttons
    buttonFrame.pack(side=TOP, pady=10)                                       # Placing the frame


    seekBarWidth = int(rootLayout.winfo_screenwidth() * 0.8)                  # Create a frame to hold the seek bar

    # Adding a seek bar (scale) at the bottom, designed to look like a music seek bar
    seekBar = Scale(controlFrame, from_=0, to=100,                           # Creating seek bar
                    orient=HORIZONTAL,                                       # Orienting it horizontally
                    bg="#1C1C1C",                                            # Setting background color
                    fg="white",                                              # Setting foreground color
                    length=seekBarWidth,                                     # Setting length
                    troughcolor="#444444",                                   # Setting trough color
                    sliderlength=15,                                         # Setting slider length
                    highlightthickness=0,                                    # Setting highlight thickness
                    showvalue=0,                                             # Setting show value
                    bd=0,                                                    # Setting border
                    tickinterval=0, width=8)                                 # Setting tick interval
    seekBar.pack(side=BOTTOM, pady=10)                                       # Placing the seek bar

    # Load images for buttons
    repeatImage = ImageTk.PhotoImage(Image.open("images/repeat.png").resize((25, 25)))      # Create a repeat image
    prevImage   = ImageTk.PhotoImage(Image.open("images/previous.png").resize((25, 25)))    # Create a previous image
    playImage   = ImageTk.PhotoImage(Image.open("images/play.png").resize((35, 35)))        # Create a play image
    stopImage   = ImageTk.PhotoImage(Image.open("images/stop.png").resize((25, 25)))        # Create a stop image
    nextImage   = ImageTk.PhotoImage(Image.open("images/next.png").resize((25, 25)))        # Create a next image

    # Create Repeat, Previous, Play (with larger size and round shape), Next, Stop buttons
    (Button(buttonFrame,                                                     # Creating buttons
           image=repeatImage,                                                # Assigning image
           bg="#1C1C1C",                                                     # Setting background color
           border=0)                                                         # Removing border
     .grid(row=0, column=0, padx=20))                                        # Placing the button

    (Button(buttonFrame,                                                     # Creating buttons
           image=prevImage,                                                  # Assigning image
           bg="#1C1C1C",                                                     # Setting background color
           border=0)                                                         # Removing border
    .grid(row=0, column=1, padx=20))                                         # Placing the button

    # Create a Play button with a larger, round shape, and a border
    playButton = Button(buttonFrame,                                         # Creating buttons
                        image=playImage,                                     # Assigning image
                        bg="#1C1C1C",                                        # Setting background color
                        borderwidth=3,                                       # Setting border
                        relief="solid",                                      # Setting border style
                        width=60,                                            # Setting width
                        height=60,                                           # Setting height
                        highlightbackground="white",                         # Setting border color
                        highlightthickness=2,                                # Setting border thickness
                        highlightcolor="white",                              # Setting border color
                        activebackground="#1C1C1C",                          # Setting active background color
                        activeforeground="white")                            # Setting active foreground color
    playButton.grid(row=0, column=2, padx=20)                                # Placing the button

    (Button(buttonFrame,                                                     # Creating buttons
           image=nextImage,                                                  # Assigning image
           bg="#1C1C1C",                                                     # Setting background color
           border=0)                                                         # Removing border
     .grid(row=0, column=3, padx=20))                                        # Placing the button

    (Button(buttonFrame,                                                     # Creating buttons
           image=stopImage,                                                  # Assigning image
           bg="#1C1C1C",                                                     # Setting background color
           border=0)                                                         # Removing border
     .grid(row=0, column=4, padx=20))                                        # Placing the button

    # Keep references to images
    rootLayout.repeatImage = repeatImage
    rootLayout.playImage = playImage
    rootLayout.stopImage = stopImage
    rootLayout.nextImage = nextImage
    rootLayout.prevImage = prevImage


    welcomeBox()
def welcomeBox():                                            # Defining welcomeBox function
    welcomeBox   = tkinter.Toplevel()                        # Creating a welcome box
    welcomeBox.title("Welcome")                              # Giving title to the welcome box
    box_width  = 500                                         # Setting width
    box_height = 500                                         # Setting height
    screen_width  = welcomeBox.winfo_screenwidth()           # Getting screen width
    screen_height = welcomeBox.winfo_screenheight()          # Getting screen height
    x = int((screen_width/2)  - (box_width/2))                # Calculating x
    y = int((screen_height/2) - (box_height/2))              # Calculating y
    welcomeBox.geometry("{}x{}+{}+{}".format(box_width, box_height, x, y)) # Setting geometry
    welcomeBox.config(bg="#000000")                          # Setting background color
    welcomeBox.overrideredirect(True)                        # Hiding windows borders
    welcomeBox.resizable(False, False)           # Disabling window resizing
    welcomeBox.attributes('-alpha', 1.0)                     # Setting transparency

    # -------------------------------- All Forms Functions -------------------------------- #
    def loginFunction(*args):
        welcomeBox.destroy()                                 # Closing the welcome box
        loginLayout()                                        # Opening login layout

    def signupFunction(*args):
        welcomeBox.destroy()                                 # Closing the welcome box
        signupLayout()                                       # Opening Signup layout


    spotifyLogo = Image.open("images/spotifyLogo.ico")       # Opening spotify logo
    resizedLogo = spotifyLogo.resize((50, 50))               # Resizing spotify logo
    logo = ImageTk.PhotoImage(resizedLogo)                   # Assigning Image to object
    spotifyLabel = Label(welcomeBox,                         # Creating a label
                         image=logo,                         # Assigning image
                         bg="#000000")                       # Setting background color
    spotifyLabel.image = logo                                # Assigning image
    spotifyLabel.pack(side=LEFT, anchor=N, padx=170, pady=50)   # Placing the label

    spotifyLabel2 = Label(welcomeBox,                        # Creating a label
                          text="Spotify",                    # Setting text
                          font=("Helvetica", 20),            # Setting font
                          bg="#000000",                      # Setting background color
                          fg="white")                        # Setting foreground color
    spotifyLabel2.place(x=222, y=60)    # Placing the label

    MillionsLabel = Label(welcomeBox,                        # Creating a label
                         text="Millions Of Songs.",          # Setting text
                         font=("CircularStd", 30, "bold"),   # Setting font
                         bg="#000000",                       # Setting background color
                         fg="white")                         # Setting foreground color
    MillionsLabel.place(x=80, y=150)                         # Placing the label

    Free = Label(welcomeBox,                                 # Creating a label
                 text="Free on Spotify",                     # Setting text
                 font=("CircularStd", 28, "bold"),           # Setting font
                 bg="#000000",                               # Setting background color
                 fg="white")                                 # Setting foreground color
    Free.place(x=115, y=205)                                 # Placing the label

    # Canvas for creating a rounded rectangle
    loginButton = Canvas(welcomeBox, width=100, height=50, bg="#000000", highlightthickness=0)
    loginButton.place(x=200, y=280)

    # Draw a rounded rectangle
    radius = 20
    x0, y0, x1, y1 = 5, 5, 95, 45
    loginButton.create_arc(x0, y0, x0 + radius, y0 + radius, start=90, extent=90,  fill="#1ED760", outline="#1ED760")
    loginButton.create_arc(x1 - radius, y0, x1, y0 + radius, start=0, extent=90,   fill="#1ED760", outline="#1ED760")
    loginButton.create_arc(x0, y1 - radius, x0 + radius, y1, start=180, extent=90, fill="#1ED760", outline="#1ED760")
    loginButton.create_arc(x1 - radius, y1 - radius, x1, y1, start=270, extent=90, fill="#1ED760", outline="#1ED760")
    loginButton.create_rectangle(x0 + radius / 2, y0, x1 - radius / 2, y1, fill="#1ED760", outline="#1ED760")
    loginButton.create_rectangle(x0, y0 + radius / 2, x1, y1 - radius / 2, fill="#1ED760", outline="#1ED760")

    # Add text or an icon
    loginButton.create_text(35, 25, text="Login", fill="black", font=("Arial", 10, "bold"))
    loginButton.bind("<Button-1>", loginFunction)

    # Load and resize the image
    canvasImage = Image.open("images/share.png")                    # Opening image
    canvasResized = canvasImage.resize((25, 25))                    # Resizing image to fit button
    canvasPhoto = ImageTk.PhotoImage(canvasResized)                 # Assigning Image to object

    # Place image on button canvas
    loginButton.create_image(75, 25, image=canvasPhoto)       # Positioning image in button
    loginButton.image = canvasPhoto                                 # Keep a reference to prevent garbage collection

    New = Label(welcomeBox,                                         # Creating a label)
                text="New to Spotify?",                             # Setting text
                font=("CircularStd", 10, "bold"),                   # Setting font
                bg="#000000",                                       # Setting background color
                fg="#999999")                                       # Setting foreground color
    New.place(x=150, y=350)                                         # Placing the label

    Signup  = Label(welcomeBox,                                     # Creating a label
                    text="Sign up free",                            # Setting text
                    font=("CircularStd", 10, "bold"),               # Setting font
                    bg="#000000",                                   # Setting background color
                    fg="#ffffff")                                   # Setting foreground color
    Signup.place(x=255, y=350)                                      # Placing the label
    Signup.bind("<Button-1>", lambda e: signupFunction())           # Calling the singup functionn

    sharewhite = Image.open("images/share-white.png")               # Opening image
    sharewhiteResized = sharewhite.resize((20, 20))                 # Resizing image to fit button
    sharewhitePhoto = ImageTk.PhotoImage(sharewhiteResized)         # Assigning Image to object

    whiteLabel = Label(welcomeBox,                                  # Creating a label
                        image=sharewhitePhoto,                      # Setting image
                        bg="#000000")                               # Setting background color
    whiteLabel.image = sharewhitePhoto                              # Keep a reference to prevent garbage collection
    whiteLabel.place(x=340, y=350)                                  # Placing the label

    Settings = Label(welcomeBox,                                    # Creating a label
                    text="Settings",                                # Setting text
                    font=("CircularStd", 10, "bold", "underline"),  # Setting font
                    bg="#000000",                                   # Setting background color
                    fg="#999999")                                   # Setting foreground color
    Settings.place(x=220, y=400)                                    # Placing the label


def loginLayout():
    loginPage  = Tk()                                               # Creating a root layout
    loginPage.title("Login")                                        # Giving title to the root layout
    login_width = 500                                               # Setting width
    login_height = 800                                              # Setting height
    screen_width = loginPage.winfo_screenwidth()                    # Get screen width
    screen_height = loginPage.winfo_screenheight()                  # Get screen height
    x = (screen_width/2) - (login_width/2)                          # Get x
    y = (screen_height/2) - (login_height/2)                        # Get y
    loginPage.geometry("%dx%d+%d+%d" % (login_width, login_height, x, y))  # Setting geometry
    loginPage.overrideredirect(True)                                # Showing windows borders Initially
    loginPage.config(bg= "#000000")                                 # Setting background color
    loginPage.resizable(False, False)                   # Disable resizing
    loginPage.attributes('-alpha', 1.0)                             # Setting transparency



def signupLayout():
    signupPage  = tkinter.Toplevel()                                 # Creating a root layout
    signupPage.title("Login")                                        # Giving title to the root layout
    signup_width = 500                                               # Setting width
    signup_height = 800                                              # Setting height
    screen_width = signupPage.winfo_screenwidth()                    # Get screen width
    screen_height = signupPage.winfo_screenheight()                  # Get screen height
    x = (screen_width/2) - (signup_width/2)                           # Get x
    y = (screen_height/2) - (signup_height/2)                         # Get y
    signupPage.geometry("%dx%d+%d+%d" % (signup_width, signup_height, x, y))  # Setting geometry
    signupPage.overrideredirect(True)                                # Showing windows borders Initially
    signupPage.config(bg= "#000000")                                 # Setting background color
    signupPage.resizable(False, False)                   # Disable resizing
    signupPage.attributes('-alpha', 1.0)                             # Setting transparency

    # ------------------------ All Forms Function ------------------ #
    def EmailEntry_Focus(*arg):                                      # Defining EmailEntry_Focus function
        if EmailTextField.get() == "name@domain.com":                # Checking if EmailTextField is empty
            EmailTextField.delete(0, "end")                  # Deleting text
            EmailTextField.config(foreground="white")                # Setting foreground color
        else:
            pass

    def EmailEntry_Leave(*arg):                                      # Defining EmailEntry_Leave function
        if len(EmailTextField.get()) == 0:                           # Checking if EmailTextField is empty
            EmailTextField.insert(0, "name@domain.com")   # Inserting text
            EmailTextField.focus()                                   # Focusing on EmailTextField
            EmailTextField.config(foreground="#999999")              # Setting foreground color

    def NameEntry_Focus(*arg):                                       # Defining NameEntry_Focus function
        if NameTextField.get() == "John Doe":                        # Checking if NameTextField is empty
            NameTextField.delete(0, "end")                   # Deleting text
            NameTextField.config(foreground="white")                 # Setting foreground color
        else:
            pass

    def NameEntry_Leave(*arg):                                       # Defining NameEntry_Leave function
        if len(NameTextField.get()) == 0:                            # Checking if NameTextField is empty
            NameTextField.insert(0, "John Doe")           # Inserting text
            NameTextField.focus()                                    # Focusing on NameTextField
            NameTextField.config(foreground="#999999")               # Setting foreground color

    def PasswordEntry_Focus(*arg):                                   # Defining PasswordEntry_Focus function
        if PasswordTextField.get() == "Password":               # Checking if PasswordTextField is empty
            PasswordTextField.config(show="*")                       # Mashing Password
            PasswordTextField.delete(0, "end")               # Erasing all text in PasswordTextField
            PasswordTextField.config(foreground="white")             # Setting foreground color
            EyeImage.place(x=signup_width // 1.35, y=signup_height // 1.67)

        else:
            pass
    def PasswordEntry_Leave(*arg):                                   # Defining PasswordEntry_Leave function
        if len(PasswordTextField.get()) == 0:                        # Checking if PasswordTextField is empty
            PasswordTextField.config(show="")                        # Unmashing Password
            PasswordTextField.insert(0, "Password")       # Inserting text
            PasswordTextField.focus()                                # Focusing on PasswordTextField
            PasswordTextField.config(foreground="#999999")           # Setting foreground color
            EyeImage.place(x=10000, y=10000)


    def show_hide_Password():                                        # Defining show_hide_Password function
        if PasswordTextField["show"] == "*":                         # Checking if PasswordTextField is mashed
            PasswordTextField.config(show="")                        # Unmashing Password
            EyeImage.config(image=NewHideEye)                        # Changing eye image
            EyeImage.image = NewHideEye                              # Prevent garbage collection
        else:
            PasswordTextField.config(show="*")                       # Mashing Password
            EyeImage.config(image=NewShowEye)                        # Changing eye image
            EyeImage.image = NewShowEye                              # Prevent garbage collection


    # ------------------------------------- Signup Function -------------------------------------- #
    def signupFunction():                                            # Creating a signup function
        check_counter = 0                                            # Creating a counter variable
        warnings = ""                                                # Creating a warning variable

        if EmailTextField.get() == "":                               # Checking if Email is empty
            warnings="Email Textfield cannot be empty"               # Creating warning message
        else:
            check_counter += 1                                       # Adding 1 to the check_counter variable

        if NameTextField.get() == "":                                # Checking if Name is empty
            warnings="Name Textfield cannot be empty"                # Creating warning message
        else:
            check_counter += 1                                       # Adding 1 to the check_counter variable

        if PasswordTextField.get() == "":                            # Checking if Password is empty
            warnings="Password Textfield cannot be empty"            # Creating warning message
        else:
            check_counter += 1

        if check_counter == 3:                                       # Creating inserting message
            try:                                                     # Try catch function
                connection = sqlite3.connect('Spotify.db')           # Connection to Database
                cur        = connection.cursor()                     # connecting to database
                cur.execute("INSERT INTO users (Email,Name,Password) "
                            "VALUES (:Email, :Name, :Password)",
      {
                'Email'    : EmailTextField.get(),                    # Assigning entry value to db column
                'Name'     : NameTextField.get(),                     # Assigning entry value to db column
                'Password' : PasswordTextField.get()                  # Assigning entry value to db column
                })
                connection.commit()                                   # Executing Inserting query
                tkinter.messagebox.showinfo("Success",            # Creating message box
                                            "Account Created Successfully",
                                            icon='warning')
                loginLayout()                                          # Calling loginLayout function
            except ValueError:                                         # Catching ValueError
                tkinter.messagebox.showwarning("ERROR", "Contact your Administrator for help",
                                               icon = "warning")       # Error message
        else:
            tkinter.messagebox.showerror("ERROR",
                                         "ERROR !!!, No Data Saved!!! - Try Again",
                                         icon = "warning")

           










    whiteLogo = Image.open("images/spotify_white.png")               # Opening spotify logo
    resizedWhite = whiteLogo.resize((50, 50))                        # Resizing spotify logo
    whiteLogo = ImageTk.PhotoImage(resizedWhite)                     # Assigning Image to object

    spotifyWhite = Label(signupPage,                                 # Correctly using signupPage as parent
                         image=whiteLogo,                            # Assigning image
                         bg="#000000")                               # Setting background color
    spotifyWhite.image = whiteLogo                                   # Prevent garbage collection
    spotifyWhite.pack(side=LEFT, anchor=N, padx=220, pady=50)        # Placing the label

    listenLabel = Label(signupPage,                                  # Correctly using signupPage as parent
                        text="Sign up to",                           # Setting text
                        font=("CircularStd", 35, "bold"),            # Setting font
                        foreground="#ffffff",                        # Setting foreground color
                        bg="#000000")                                # Setting background color
    listenLabel.place(x=signup_width // 4, y=signup_height // 6)     # Placing the label

    listenLabel2 = Label(signupPage,                                 # Correctly using signupPage as parent
                         text="Start Listening",                     # Setting text
                         font=("CircularStd", 35, "bold"),           # Setting font
                         foreground="#ffffff",                       # Setting foreground color
                         bg="#000000")                               # Setting background color
    listenLabel2.place(x=signup_width // 7, y=signup_height // 4)    # Placing the label

    EmailLabel = Label(signupPage,                                   # Correctly using signupPage as parent
                       text="Email address",                         # Setting text
                       font=("CircularStd", 10, "bold"),             # Setting font
                       foreground="#ffffff",                         # Setting foreground color
                       bg="#000000")                                 # Setting background color
    EmailLabel.place(x=signup_width // 7, y=signup_height // 2.8)    # Placing the label

    EmailTextField = Entry(signupPage,                               # Creating a text field
                           relief="solid",                           # Setting relief
                           font=("CircularStd", 10),                 # Setting font
                           background="black",                       # Adding Background color
                           foreground="gray",                        # Setting foreground color
                           highlightthickness=1,                     # Setting highlight thickness
                           highlightbackground="gray")               # Setting highlight background color
    EmailTextField.insert(0, "name@domain.com")           # Inserting text
    EmailTextField.place(x=signup_width // 7, y=signup_height // 2.6 , width=350, height= 50) # Placing the text field
    EmailTextField.bind("<Button-1>", EmailEntry_Focus)              # Binding EmailEntry_Focus function
    EmailTextField.bind("<Leave>",    EmailEntry_Leave)               # Binding EmailEntry_Leave function

    NameLabel = Label(signupPage,                                    # Creating a label,
                      text="Name",                                   # Setting text
                      font=("CircularStd", 10, "bold"),              # Setting font
                      foreground="#ffffff",                          # Setting foreground color
                      bg="#000000")                                  # Setting background color
    NameLabel.place(x=signup_width // 7, y=signup_height // 2.2)     # Placing Label

    NameTextField = Entry(signupPage,                                # Creating a text field
                          relief="solid",                            # Setting relief
                          font=("CircularStd", 10),                  # Setting font
                          background="black",                        # Adding Background color
                          foreground="gray",                         # Adding Foreground Color
                          highlightthickness=1,                      # Setting highlight
                          highlightbackground="gray")                # Setting highlight background color
    NameTextField.insert(0, "John Doe")                   # Inserting text
    NameTextField.place(x=signup_width // 7, y=signup_height // 2.08, width=350, height= 50) # Placing the text field
    NameTextField.bind("<Button-1>", NameEntry_Focus)                # Binding NameEntry_Focus function
    NameTextField.bind("<Leave>",    NameEntry_Leave)                # Binding NameEntry_Leave function

    PasswordLabel = Label(signupPage,                                # Creating a label,
                          text="Password",                           # Setting text
                          font=("CircularStd", 10, "bold"),          # Setting font
                          foreground="#ffffff",                      # Setting foreground color
                          bg="#000000")                              # Setting background color
    PasswordLabel.place(x=signup_width // 7, y=signup_height // 1.8) # Placing Label


    PasswordTextField = Entry(signupPage,                            # Creating a text field
                              relief="solid",                        # Setting relief
                              font=("CircularStd", 10),              # Setting font
                              background="black",                    # Adding Background color
                              foreground="gray",                     # Adding Foreground Color
                              highlightthickness=1,                  # Setting highlight
                              highlightbackground="gray")            # Setting highlight background color
    PasswordTextField.insert(0, "Password")                 # Inserting text
    PasswordTextField.place(x=signup_width // 7, y=signup_height // 1.7, width=350, height= 50) # Placing the text field3
    PasswordTextField.bind("<Button-1>", PasswordEntry_Focus)        # Binding PasswordEntry_Focus function
    PasswordTextField.bind("<Leave>",    PasswordEntry_Leave)        # Binding PasswordEntry_Leave function

    HideEye = Image.open("images/invisible_eye.png")                     # Opening eye image
    ResizedEye = HideEye.resize((25, 25))                            # Resizing the eye images
    NewHideEye = ImageTk.PhotoImage(ResizedEye)                      # Resizing the eye images

    ShowEye = Image.open("images/visible_eye.png")                   # Opening eye image
    ResizedShowEye = ShowEye.resize((25, 25))                        # Resizing the eye images
    NewShowEye = ImageTk.PhotoImage(ResizedShowEye)                  # Resizing the eye images

    EyeImage = Label(signupPage,                                     # Creating a label
                     image=NewShowEye,                               # Setting image
                     bg="#000000",                                   # Setting background color
                     cursor="hand2")                                 # Setting cursor
    EyeImage.image = NewShowEye                                      # Prevent garbage collection
    EyeImage.bind("<Button-1>", lambda e: show_hide_Password())      # Calling show_hide_Password function

    SignupButton = Button(signupPage,                                # Creating a button
                          text="Sign up",                            # Setting text
                          command="",                                # Setting command
                          font=("CircularStd", 10, "bold"),          # Setting font
                          width=43,                                  # Setting width
                          height=3,                                  # Setting height
                          border=0,                                  # Setting border
                          cursor="hand2",                            # Setting cursor
                          background="#1ED760",                      # Setting background color
                          foreground="white")                        # Setting foreground color
    SignupButton.place(x=signup_width // 7, y=signup_height // 1.4) # Placing the button



Spotify()                                                            # Calling Spotify function
mainloop()                                                           # Running mainloop