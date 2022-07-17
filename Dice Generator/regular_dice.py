from tkinter import *
from PIL import Image, ImageTk
import tkinter
import random

        
def firstDicePage():
        #global opened, firstWindow
  
        firstWindow = tkinter.Toplevel(window)  # Create new window.

        firstWindow.title("Dice Roller Generator")

        # Change Icon photo
        image = PhotoImage(file = "C:\\Users\\alexi\\Desktop\\Project Photos\\Dice logo.png")
        firstWindow.iconphoto(False, image)

        # Center 
        app_width = 900
        app_height = 600

        screen_width = firstWindow.winfo_screenwidth()
        screen_height = firstWindow.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y= (screen_height / 2) - (app_height / 2)

        firstWindow.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        

        Label(firstWindow, text = "\n\nSelect How Many Dice You Want to Roll!", font='Helvetica 16 bold').pack()

        img = ImageTk.PhotoImage(Image.open("C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\Dice.png"))
        my_label = Label(firstWindow, image=img)
        my_label.img = img  # Save reference to image.
        my_label.pack()

        counter = tkinter.IntVar()

        def increase():
                 counter.set(min(10, counter.get() + 1)) 

        def decrease():
                counter.set(max(0, counter.get() - 1))


        lbl = Label(firstWindow, textvariable = counter, font='Helvetica 16 bold')
        lbl.place(x=450, y=330)

        btn1 = Button(firstWindow, text="+", font='Helvetica 16 bold',  padx = 8, pady = 5, command = increase, fg="dark green", bg = "white")
        btn1.place(x=499, y=320)

        btn2 = Button(firstWindow, text ="-", font='Helvetica 16 bold', padx = 11.1, pady = 5, command = decrease, fg="dark green", bg = "white")
        btn2.place(x=375, y=320)

        btn3 = Button(firstWindow, text = "Back", font='Helvetica 16 bold', command = firstWindow.destroy)
        btn3.place(x = 30 , y = 530)

        btn4 = Button(firstWindow, text = "Next", font='Helvetica 16 bold', command = lambda: secondDicePage(counter.get()))
        btn4.place(x = 800 , y = 530)


def secondDicePage(num_dices):

        secondWindow = tkinter.Toplevel(window)  # Create new window.

        secondWindow.title("Dice Roller Generator")

        # Change Icon photo
        image = PhotoImage(file = "C:\\Users\\alexi\\Desktop\\Project Photos\\Dice logo.png")
        secondWindow.iconphoto(False, image)

        # Center 
        app_width = 900
        app_height = 600

        screen_width = secondWindow.winfo_screenwidth()
        screen_height = secondWindow.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y= (screen_height / 2) - (app_height / 2)

        secondWindow.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        
        # all six die
        dice = ['C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\dice_1.png', 'C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\dice_2.png', 'C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\dice_3.png', 
                'C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\dice_4.png', 'C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\dice_5.png', 'C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\dice_6.png']

        # questionmark image
        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\questionmark.png"))

        # error message image
        img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\message.png"))

        # Images will show depending on the increments on firstDicePage
        if num_dices == 0:
                lbl = Label(secondWindow, image=img2)
                lbl.img = img2  # Save reference to image.
                lbl.pack()
                lbl.place(x = 380 , y = 95)
        elif num_dices == 1:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)
        elif num_dices == 2:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 500 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 260 , y = 95)
        elif num_dices == 3:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 195 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 565 , y = 95)
        elif num_dices == 4:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 500 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 260 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 500 , y = 300)

                lbl4 = Label(secondWindow, image=img1)
                lbl4.img = img1  # Save reference to image.
                lbl4.pack()
                lbl4.place(x = 260 , y = 300)
        elif num_dices == 5:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 195 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 565 , y = 95)

                lbl4 = Label(secondWindow, image=img1)
                lbl4.img = img1  # Save reference to image.
                lbl4.pack()
                lbl4.place(x = 746 , y = 95)

                lbl5 = Label(secondWindow, image=img1)
                lbl5.img = img1  # Save reference to image.
                lbl5.pack()
                lbl5.place(x = 1 , y = 95)
        elif num_dices == 6:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 195 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 565 , y = 95)

                lbl4 = Label(secondWindow, image=img1)
                lbl4.img = img1  # Save reference to image.
                lbl4.pack()
                lbl4.place(x = 565 , y = 300)

                lbl5 = Label(secondWindow, image=img1)
                lbl5.img = img1  # Save reference to image.
                lbl5.pack()
                lbl5.place(x = 195 , y = 300)
 
                lbl6 = Label(secondWindow, image=img1)
                lbl6.img = img1  # Save reference to image.
                lbl6.pack()
                lbl6.place(x = 380 , y = 300)
        elif num_dices == 7:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 195 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 565 , y = 95)

                lbl4 = Label(secondWindow, image=img1)
                lbl4.img = img1  # Save reference to image.
                lbl4.pack()
                lbl4.place(x = 746 , y = 95)

                lbl5 = Label(secondWindow, image=img1)
                lbl5.img = img1  # Save reference to image.
                lbl5.pack()
                lbl5.place(x = 1 , y = 95)
 
                lbl6 = Label(secondWindow, image=img1)
                lbl6.img = img1  # Save reference to image.
                lbl6.pack()
                lbl6.place(x = 500 , y = 300)
 
                lbl7 = Label(secondWindow, image=img1)
                lbl7.img = img1  # Save reference to image.
                lbl7.pack()
                lbl7.place(x = 250 , y =300)
        elif num_dices == 8:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 195 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 565 , y = 95)

                lbl4 = Label(secondWindow, image=img1)
                lbl4.img = img1  # Save reference to image.
                lbl4.pack()
                lbl4.place(x = 746 , y = 95)

                lbl5 = Label(secondWindow, image=img1)
                lbl5.img = img1  # Save reference to image.
                lbl5.pack()
                lbl5.place(x = 1 , y = 95)
 
                lbl6 = Label(secondWindow, image=img1)
                lbl6.img = img1  # Save reference to image.
                lbl6.pack()
                lbl6.place(x = 380 , y = 300)
 
                lbl7 = Label(secondWindow, image=img1)
                lbl7.img = img1  # Save reference to image.
                lbl7.pack()
                lbl7.place(x = 195 , y =300)

                lbl8 = Label(secondWindow, image=img1)
                lbl8.img = img1  # Save reference to image.
                lbl8.pack()
                lbl8.place(x = 565 , y = 300)
        elif num_dices == 9:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 195 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 565 , y = 95)

                lbl4 = Label(secondWindow, image=img1)
                lbl4.img = img1  # Save reference to image.
                lbl4.pack()
                lbl4.place(x = 746 , y = 95)

                lbl5 = Label(secondWindow, image=img1)
                lbl5.img = img1  # Save reference to image.
                lbl5.pack()
                lbl5.place(x = 1 , y = 95)
 
                lbl6 = Label(secondWindow, image=img1)
                lbl6.img = img1  # Save reference to image.
                lbl6.pack()
                lbl6.place(x = 250 , y = 300)
 
                lbl7 = Label(secondWindow, image=img1)
                lbl7.img = img1  # Save reference to image.
                lbl7.pack()
                lbl7.place(x = 1 , y =300)

                lbl8 = Label(secondWindow, image=img1)
                lbl8.img = img1  # Save reference to image.
                lbl8.pack()
                lbl8.place(x = 500 , y = 300)

                lbl9 = Label(secondWindow, image=img1)
                lbl9.img = img1  # Save reference to image.
                lbl9.pack()
                lbl9.place(x = 746 , y = 300)
        elif num_dices == 10:
                lbl1 = Label(secondWindow, image=img1)
                lbl1.img = img1  # Save reference to image.
                lbl1.pack()
                lbl1.place(x = 380 , y = 95)

                lbl2 = Label(secondWindow, image=img1)
                lbl2.img = img1  # Save reference to image.
                lbl2.pack()
                lbl2.place(x = 195 , y = 95)

                lbl3 = Label(secondWindow, image=img1)
                lbl3.img = img1  # Save reference to image.
                lbl3.pack()
                lbl3.place(x = 565 , y = 95)

                lbl4 = Label(secondWindow, image=img1)
                lbl4.img = img1  # Save reference to image.
                lbl4.pack()
                lbl4.place(x = 746 , y = 95)

                lbl5 = Label(secondWindow, image=img1)
                lbl5.img = img1  # Save reference to image.
                lbl5.pack()
                lbl5.place(x = 1 , y = 95)
 
                lbl6 = Label(secondWindow, image=img1)
                lbl6.img = img1  # Save reference to image.
                lbl6.pack()
                lbl6.place(x = 380 , y = 300)
 
                lbl7 = Label(secondWindow, image=img1)
                lbl7.img = img1  # Save reference to image.
                lbl7.pack()
                lbl7.place(x = 195 , y =300)

                lbl8 = Label(secondWindow, image=img1)
                lbl8.img = img1  # Save reference to image.
                lbl8.pack()
                lbl8.place(x = 565 , y = 300)

                lbl9 = Label(secondWindow, image=img1)
                lbl9.img = img1  # Save reference to image.
                lbl9.pack()
                lbl9.place(x = 746 , y = 300)
   
                lbl10 = Label(secondWindow, image=img1)
                lbl10.img = img1  # Save reference to image.
                lbl10.pack()
                lbl10.place(x = 1 , y = 300)
        else:
                return None


       # functions connect to all lbl above in the elif statment
        def rolling_dice0():

                lbl.configure( bg = '#B9C6C9')

        def rolling_dice1():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl1.configure(image = image1, bg = '#B9C6C9')
                lbl1.image = image1

        def rolling_dice2():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl2.configure(image = image1, bg = '#B9C6C9')
                lbl2.image = image1

        
        def rolling_dice3():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl3.configure(image = image1, bg = '#B9C6C9')
                lbl3.image = image1


        def rolling_dice4():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl4.configure(image = image1, bg = '#B9C6C9')
                lbl4.image = image1


        def rolling_dice5():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl5.configure(image = image1, bg = '#B9C6C9')
                lbl5.image = image1

        
        def rolling_dice6():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl6.configure(image = image1, bg = '#B9C6C9')
                lbl6.image = image1


        def rolling_dice7():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl7.configure(image = image1, bg = '#B9C6C9')
                lbl7.image = image1

        def rolling_dice8():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl8.configure(image = image1, bg = '#B9C6C9')
                lbl8.image = image1

        
        def rolling_dice9():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl9.configure(image = image1, bg = '#B9C6C9')
                lbl9.image = image1

        
        def rolling_dice10():
                
                image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

                lbl10.configure(image = image1, bg = '#B9C6C9')
                lbl10.image = image1  
        
        # able to roll depending on the number chosen in firstDicePage
        if num_dices == 0:
                btn0 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice0()])
                btn0.place(x = 400 , y = 30)        
        elif num_dices == 1:
                btn1 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1()])
                btn1.place(x = 400 , y = 30)
        elif num_dices == 2:
                btn2 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2()])
                btn2.place(x = 400 , y = 30)
        elif num_dices == 3:
                btn3 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3()])
                btn3.place(x = 400 , y = 30)
        elif num_dices == 4:
                btn4 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3(), rolling_dice4()])
                btn4.place(x = 400 , y = 30)
        elif num_dices == 5:
                btn5 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3(), rolling_dice4(), rolling_dice5()])
                btn5.place(x = 400 , y = 30)
        elif num_dices == 6:
                btn6 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3(), rolling_dice4(), rolling_dice5(), rolling_dice6()])
                btn6.place(x = 400 , y = 30)
        elif num_dices == 7:
                btn7 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3(), rolling_dice4(), rolling_dice5(), rolling_dice6(), rolling_dice7()])
                btn7.place(x = 400 , y = 30)
        elif num_dices == 8:
                btn8 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3(), rolling_dice4(), rolling_dice5(), rolling_dice6(), rolling_dice7(), rolling_dice8()])
                btn8.place(x = 400 , y = 30)
        elif num_dices == 9:
                btn9 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3(), rolling_dice4(), rolling_dice5(), rolling_dice6(), rolling_dice7(), rolling_dice8(), rolling_dice9()])
                btn9.place(x = 400 , y = 30)
        elif num_dices == 10:
                btn10 = Button(secondWindow, text = "Roll Dice", font='Helvetica 16 bold', command = lambda: [rolling_dice1(), rolling_dice2(), rolling_dice3(), rolling_dice4(), rolling_dice5(), rolling_dice6(), rolling_dice7(), rolling_dice8(), rolling_dice9(), rolling_dice10()])
                btn10.place(x = 400 , y = 30)
        else:
                return None

        btn = Button(secondWindow, text = "Back", font='Helvetica 16 bold', command = secondWindow.destroy)
        btn.place(x = 30 , y = 530)


# Create the window(root inteface)
window = Tk()

# Create a title
window.title("Dice Roller Generator")

# Change Icon photo
img = PhotoImage(file = "C:\\Users\\alexi\\Desktop\\Project Photos\\Dice logo.png")
window.iconphoto(False, img)

# Center 
app_width = 600
app_height = 400

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y= (screen_height / 2) - (app_height / 2)

window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# background image
bg = PhotoImage( file = "C:\\Users\\alexi\\Desktop\\Project Photos\\Dice Rolling\\background.png")

label1 = Label( window, image = bg)
label1.place(x = 0,y = 0)

# Create a label widget 
lbl = Label(window, text = "\n\n\nClick the Button Below to Start!", font='Helvetica 16 bold', image = bg)
lbl.pack()

btn1 = Button(window, text = "Click Here to Roll Dice", padx = 15, pady = 15, command = firstDicePage,)
btn1.place(x=230, y=130)


btn3 = Button(window, text="Exit", padx = 15, pady = 5, command = window.quit)
btn3.place(x=275, y=335)

window.mainloop()