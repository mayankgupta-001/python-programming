import tkinter as tk

class ItemListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("List Item")
        self.createApp()

    def createApp(self):
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        tk.Button(self.root, text='Add', command=self.addItem).pack()
        tk.Button(self.root, text='Remove', command=self.removeItem).pack()
        self.list = tk.Listbox(self.root)
        self.list.pack()
    
    def addItem(self):
        if self.entry1.get() != '':
            self.list.insert(tk.END, self.entry1.get())
            self.entry1.delete(0, tk.END)
    
    def removeItem(self):
        self.list.delete(tk.ANCHOR)

if __name__ == '__main__':
    root = tk.Tk()
    app = ItemListApp(root)
    root.mainloop()

# from tkinter import *
# import tkinter as tk
# from tkinter import messagebox, ttk
# root = tk.Tk()

# def addItem():
#     if entry1.get() != '':
#         # listBox.insert(0, entry1.get())
#         listBox.insert(tk.END, entry1.get())
#         entry1.delete(0, tk.END)

# def removeItem():
#     listBox.delete(tk.ANCHOR)

# entry1 = tk.Entry(root)
# entry1.pack()

# # addBtn = tk.Button(root, text='Add', command=addItem())
# # addBtn.pack()
# # remBtn = tk.Button(root, text='Remove', command=removeItem())
# # remBtn.pack()
# tk.Button(root, text='Add', command=addItem()).pack()
# tk.Button(root, text='Remove', command=removeItem()).pack()


# listBox = tk.Listbox(root)
# listBox.pack()

# root.mainloop()