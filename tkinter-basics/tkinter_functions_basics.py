import tkinter as tk
from tkinter import messagebox

class MyGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        #root is the main window
        
        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)
        #exit is built in window destroyer
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        
        self.root.config(menu=self.menubar)
        
        self.label = tk.Label(self.root, text = "Enter message here", font=('Arial',18))
        self.label.pack(padx=10,pady=10)
        
        self.textbox = tk.Text(self.root, height=5,font=('Arial',16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        #allows keypress to create event
        self.textbox.pack(padx=10,pady=10)
        
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox?", font=('Arial',16), variable=self.check_state)
        self.check.pack(padx=10,pady=10)
        
        self.button = tk.Button(self.root, text="Show message", font=('Arial',18), command=self.show_message)
        #command lets it execute the function
        self.button.pack(padx=10,pady=10)
        
        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial',18), command=self.clear)
        self.clearbtn.pack(padx=10,pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
            #start and end
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
   
    def shortcut(self, event):
        if event.keysym == "Return":
            #"enter" key
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit the program?"):
            #executes if yes is clicked
            self.root.destroy()
            #destroys the window
            
    def clear(self):
        self.textbox.delete('1.0', tk.END)
            
if __name__ == "__main__":
  MyGUI()
