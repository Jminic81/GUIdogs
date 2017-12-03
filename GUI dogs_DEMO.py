import tkinter
import sqlite3

def convert(out_breed, enter_rank):
    """ Find the rank in Sqlite3 dogs89.db table Dog_Licc and return the breed. """
    num = enter_rank.get()
    num_tup=(num,)
    con = sqlite3.connect('dogs89.db')
    cur = con.cursor()
    cur.execute('''SELECT Breed FROM Dog_Licc WHERE Rank = ?''',num_tup)
    output=cur.fetchone()
    output = output[0]
    out_breed.set(output)
         
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

out_breed = tkinter.StringVar()
enter_rank = tkinter.IntVar()

tkinter.Label(frame, text='Enter Breed Rank 1-10').pack()

enter_rank = tkinter.StringVar()
text = tkinter.Entry(frame, textvar=enter_rank, justify='center')
text.pack()

out_breed = tkinter.StringVar()
label = tkinter.Label(frame, textvar=out_breed)
label.pack()

button = tkinter.Button(frame, text='Find Breed', command=lambda: convert(out_breed, enter_rank))
button.pack()

button2 = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
button2.pack()

window.mainloop()
