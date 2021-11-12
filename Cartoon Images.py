import cv2
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk


screen = Tk()
screen.title("Cartoon Picture ")
screen.iconbitmap("favicon.ico")
screen.resizable(False, False)
screen.config(bg='black')
screen.geometry("300x425")





def file():
    global o
    o = filedialog.askopenfilename(initialdir="c:/Users/Welcome/Pictures", title='Select The File', filetype=(("JPG", "*.jpg"), ("PNG", "*.png")))
    path.insert(0,str(o))


path= Entry(screen, bd=0,width=30, font=('times', 15, 'italic'), bg='black', fg='cyan')
path.grid(row=2, column=0)
pic =Button(screen, text='Import', command=file, bg='black', cursor='plus', fg='gray', activebackground='black', activeforeground="#00FFFF", font=("jokerman", 15, "italic"), bd=0)
screen.update()
pic.grid(row=3, column=0)
screen.update_idletasks()
cnp = ImageTk.PhotoImage(file="logo.png")
out = Label(screen, image=cnp, bg='black')
screen.update()
out.grid(row=1, column=0)
screen.update()
n= Entry(screen,width=25, font=('times', 15, 'italic'), bg='black', fg='gray')
n.grid(row=5, column=0)
Label(screen, text="Specify Export file Name", bg='black', fg='gray', font=("jokerman", 15, "italic")).grid(row=4, column=0)



def generate():
    if len(path.get()) != 0:
        img = cv2.imread(o)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

        color = cv2.bilateralFilter(img, 9, 9, 7)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        name = n.get()
        if len(name) != 0:
            cv2.imwrite(f"{name}.jpg", cartoon)
            path.delete(0, END)
            n.delete(0, END)
            screen.update()
            messagebox.showinfo("Export", "Exported Successfully!")

        else:
            messagebox.showerror("Save Error", "File Name Was Not Specified")

    else:
        messagebox.showerror("Import Error", 'No File Was Imported')



def exit():
    d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
    if d =="yes":
        screen.destroy()
    else:
        return None



gen = Button(screen, text='Export', font=("jokerman", 15, "italic"), bd=0, cursor='plus', command=generate, bg='black', fg='gray', activebackground='black', activeforeground='#00ff00').grid(row=6, column=0)
close = Button(screen, text='Exit', command=exit, bd=0, font=("jokerman", 15, "italic"), cursor='plus', bg='black', fg='gray', activebackground='black', activeforeground='#ff0000').grid(row=7, column=0)




screen.mainloop()