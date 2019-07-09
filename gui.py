import sys
import tkinter
import tkinter.ttk as ttk

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global root
    root = tkinter.Tk()
    top = New_Toplevel(root)
    root.mainloop()
    return top

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, rt
    rt = root
    w = tkinter.Toplevel (root)
    top = New_Toplevel(w)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("390x278+784+187")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Entry1 = tkinter.Entry(top)
        self.Entry1.place(relx=0.308, rely=0.216,height=20, relwidth=0.421)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tkinter.Entry(top)
        self.Entry2.place(relx=0.308, rely=0.324,height=20, relwidth=0.421)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=164)

        self.Entry3 = tkinter.Entry(top)
        self.Entry3.place(relx=0.308, rely=0.432,height=20, relwidth=0.421)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label1 = tkinter.Label(top)
        self.Label1.place(relx=0.077, rely=0.216, height=21, width=44)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Name:''')

        self.Label2 = tkinter.Label(top)
        self.Label2.place(relx=0.077, rely=0.324, height=21, width=41)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Email:''')

        self.Label3 = tkinter.Label(top)
        self.Label3.place(relx=0.077, rely=0.432, height=21, width=62)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Password:''')

        self.Button1 = tkinter.Button(top)
        self.Button1.place(relx=0.308, rely=0.576, height=34, width=107)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Email''')
        self.Button1.configure(width=107)

        self.Label4 = tkinter.Label(top)
        self.Label4.place(relx=0.333, rely=0.036, height=41, width=146)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Email Database''')
        self.Label4.configure(width=146)

        self.Label5 = tkinter.Label(top)
        self.Label5.place(relx=0.077, rely=0.755, height=21, width=334)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Name:                                Email:                              Password:''')
        self.Label5.configure(width=334)






if __name__ == '__main__':
    vp_start_gui()

