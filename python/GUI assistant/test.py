#resize the shit and it's ready to use
import tkinter as tk
import wolframalpha
import wikipedia

def show_entry_fields():
    e2.delete(0, tk.END)
    print("Question: %s\n" % e1.get())
    usrinput = e1.get()
    try:
        app_id = "36UY6L-X5VXYHR59R"
        client = wolframalpha.Client(app_id)

        res = client.query(usrinput)
        answer = next(res.results).text
        e2.insert(10, answer)
    except:
        answer = wikipedia.summary(usrinput, sentences=5)
        e2.insert(10, answer)
    
def rst():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
master = tk.Tk()
tk.Label(master, text="Question:").grid(row=0)
tk.Label(master, text="Answer").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.insert(10, "Cat")
e2.insert(10, "Ask Something")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#master.grid_columnconfigure(1, minsize=600)
tk.Button(master, 
          text='Reset', 
          command=rst).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)

tk.Button(master, text='Ask', command=show_entry_fields).grid(row=3, 
                                                               column=2, 
                                                               sticky=tk.W, 
                                                               pady=4)

master.mainloop()
tk.mainloop()