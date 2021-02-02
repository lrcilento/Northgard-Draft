import tkinter as tk
from draft import draft

root = tk.Tk()

root.title("Northgard Draft v0.1")
root.geometry('600x500')
root.resizable(False, False)

atLeastOneBasic = tk.BooleanVar()
enableDLCs = tk.BooleanVar()
numberOfPlayers = tk.IntVar()
clansPerPerson = tk.IntVar()
views = []

def prepareForDraft():
    for label in root.grid_slaves():
        if int(label.grid_info()["row"] >= 6):
            label.grid_forget()
    results = draft(enableDLCs.get(), atLeastOneBasic.get(), clansPerPerson.get(), numberOfPlayers.get())
    total = len(results)
    for x in range(0, total):
        try:
            tk.Label(root, text = "Player "+str(results[x]['player'])).grid(column = x+4-int(total/2), row = 6)
            for y in range(0, len(results[x - 1]['clans'])):
                tk.Label(root, text = results[x - 1]['clans'][y]).grid(column = x+4-int(total/2), row = y + 7)
        except:
            tk.Label(root, text = results[0]).grid(column = 3, row = 6)

def create():
    topPadding = tk.Label(root, text = "")
    topPadding.grid(row = 0, column = 0, columnspan = 8)

    atLeastOneBasicCheckbox = tk.Checkbutton(root, text = "At least one basic clan", 
                                            variable = atLeastOneBasic, 
                                            onvalue = True, offvalue = False)
    atLeastOneBasicCheckbox.grid(row = 1, column = 0, columnspan = 8, ipady = 10, padx = 200)

    enableDLCsCheckbox = tk.Checkbutton(root, text = "Enable DLCs", 
                                        variable = enableDLCs, anchor = tk.W,
                                        onvalue = True, offvalue = False)
    enableDLCsCheckbox.grid(row = 2, columnspan = 8,column = 0, ipady = 10, ipadx = 33)

    numberOfPlayersSlider = tk.Scale(root, from_=2, to=8, orient=tk.HORIZONTAL, length = 150,
                                    variable = numberOfPlayers, label = "Number of Players")
    numberOfPlayersSlider.grid(row = 3, columnspan = 8, column = 0)

    clansPerPersonSlider = tk.Scale(root, from_=1, to=6, orient=tk.HORIZONTAL, length = 150,
                                    variable = clansPerPerson, label = "Clans per Player")
    clansPerPersonSlider.grid(row = 4, columnspan = 8,column = 0)

    mainButton = tk.Button(root, text = "Draft!", command=prepareForDraft)
    mainButton.grid(row = 5, columnspan = 8,column = 0, pady = 20)


create()
root.mainloop()