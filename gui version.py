# TO Helper GUI, for people who hate numpad, I guess
# Setting up files to be read. They're .txt because OBS defaults to that in the open selector
# but it doesn't really matter.
import os 
import tkinter as tk

p1name = 'Player 1' # Temporary placeholders for the player names so they aren't submitted
p2name = 'Player 2' # before you press Submit Names, to queue up next matches.
p1w = 0 #same thing for wins
p2w = 0 
# these are the commands used by the buttons in the middle.
def submit():
    p1n = ent_p1name.get()
    p2n = ent_p2name.get()
    with open('p1name.txt','w') as f:
        f.write(p1n)
    with open('p2name.txt','w') as f:
        f.write(p2n)
    with open('p1wins.txt','w') as f:
        f.write('0')
    with open('p2wins.txt','w') as f:
        f.write('0')
    lbl_p2winc["text"]='0'
    lbl_p1winc["text"]='0'
def clear():
    with open('p1name.txt','w') as f:
        f.write('Player 1')
    with open('p2name.txt','w') as f:
        f.write('Player 2')
    with open('p1wins.txt','w') as f:
        f.write('0')
    with open('p2wins.txt','w') as f:
        f.write('0')
    ent_p1name.delete(0,tk.END)
    ent_p2name.delete(0,tk.END)
    ent_p1name.insert(0,"Player 1")
    ent_p2name.insert(0,"Player 2")
def fixnames():
    p1n = ent_p1name.get()
    p2n = ent_p2name.get()
    with open('p1name.txt','w') as f:
        f.write(p1n)
    with open('p2name.txt','w') as f:
        f.write(p2n)
def swap():
    with open("p1name.txt","r+") as f:
        p2n = f.read()
        with open("p2name.txt","r+") as g:
            p1n = g.read()
            g.seek(0)
            g.write(p2n)
            g.truncate()
            ent_p2name.delete(0,tk.END)
            ent_p2name.insert(0,p2n)
        f.seek(0)
        f.write(p1n)
        f.truncate()
        ent_p1name.delete(0,tk.END)
        ent_p1name.insert(0,p1n)
    with open("p1wins.txt","r+") as f:
        p2w = f.read()
        with open("p2wins.txt","r+") as g:
            p1w = g.read()
            g.seek(0)
            g.write(p2w)
            g.truncate()
            lbl_p2winc['text'] = p2w
        f.seek(0)
        f.write(p1w)
        f.truncate()
        lbl_p1winc['text'] = p1w
def p1wininc():
    win = int(lbl_p1winc["text"])+1
    lbl_p1winc["text"] = f"{win}"
    with open("p1wins.txt","w") as f:
        f.write(str(win))
def p1windec():
    win = int(lbl_p1winc["text"])-1
    lbl_p1winc["text"] = f"{win}"
    with open("p1wins.txt","w") as f:
        f.write(str(win))
def p2wininc():
    win = int(lbl_p2winc["text"])+1
    lbl_p2winc["text"] = f"{win}"
    with open("p2wins.txt","w") as f:
        f.write(str(win))
def p2windec():
    win = int(lbl_p2winc["text"])-1
    lbl_p2winc["text"] = f"{win}"  
    with open("p2wins.txt","w") as f:
        f.write(str(win))    

# this is all setting up the GUI. I'm sorry.
window = tk.Tk()
window.title("TO Helper")
window.resizable(False,False)

frm_p1 = tk.Frame(window,padx=5,pady=5,borderwidth=2,relief="ridge")
frm_buttons = tk.Frame(window,padx=5,pady=5)
frm_p2 = tk.Frame(window,padx=5,pady=5,borderwidth=2,relief="ridge")

btn_submit = tk.Button(frm_buttons,text="Submit",width=8,command=submit)
btn_clear = tk.Button(frm_buttons,text="Clear",width=8,command=clear)
btn_fixn = tk.Button(frm_buttons,text="Fix Names",width=8,command=fixnames)
btn_swap = tk.Button(frm_buttons,text="Swap",width=8,command=swap)
btn_submit.grid(row=0,column=0,pady=2)
btn_clear.grid(row=1,column=0,pady=2)
btn_fixn.grid(row=2,column=0,pady=2)
btn_swap.grid(row=3,column=0,pady=2)

lbl_p1name = tk.Label(frm_p1,text="P1 Name")
lbl_p1wins = tk.Label(frm_p1,text="Wins")
lbl_p1winc = tk.Label(frm_p1,text="0")
btn_p1inc = tk.Button(frm_p1,text="+",width=2,command=p1wininc)
btn_p1dec = tk.Button(frm_p1,text="-",width=2,command=p1windec)
ent_p1name = tk.Entry(frm_p1,width=20,text="Player 1")
lbl_p1name.grid(row=0,column=2,sticky="w",padx=5)
lbl_p1winc.grid(row=1,column=1,sticky='ew')
lbl_p1wins.grid(row=1,column=0,sticky='e')
btn_p1inc.grid(row=0,column=1,sticky='nsew')
btn_p1dec.grid(row=2,column=1,sticky='nsew')
ent_p1name.grid(row=1,column=2,sticky="w",padx=5)

lbl_p2name = tk.Label(frm_p2,text="P2 Name")
lbl_p2wins = tk.Label(frm_p2,text="Wins")
lbl_p2winc = tk.Label(frm_p2,text="0")
btn_p2inc = tk.Button(frm_p2,text="+",width=2,command=p2wininc)
btn_p2dec = tk.Button(frm_p2,text="-",width=2,command=p2windec)
ent_p2name = tk.Entry(frm_p2,width=20,text="Player 2")
lbl_p2name.grid(row=0,column=0,sticky="e",padx=5)
lbl_p2winc.grid(row=1,column=1,sticky='ew')
lbl_p2wins.grid(row=1,column=2,sticky='w')
btn_p2dec.grid(row=2,column=1,sticky="nsew")
btn_p2inc.grid(row=0,column=1,sticky="nsew")
ent_p2name.grid(row=1,column=0,sticky="e",padx=5)

frm_p1.grid(row=0,column=0)
frm_buttons.grid(row=0,column=1)
frm_p2.grid(row=0,column=2)

clear()
window.mainloop()