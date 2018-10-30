import tkinter as tk
import tkinter.messagebox as tkmb

top = tk.Tk()
top.geometry("1280x720")

def callback(string):
   print(string)

list = ["hello", "hey", "test", "foo", "bar", "baz", "idk", "python", "c++", "java"]
word_dict = {}

px = 50
py = 50
for word in list: 
    if(py > 1100):
    	py = 50
    	px += 200
    	
    word_dict[word] = tk.Button(text = word, command=lambda j=word: callback(j))
    word_dict[word].place(bordermode=tk.OUTSIDE, height=100, width=100, x=py, y=px)
    py += 200
    
top.mainloop()
