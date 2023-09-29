import tkinter as tk

calculation = ""

def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluateCalculation():
    global calculation
    try:
        
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clearField()
        text_result.insert(1.0, "Error")
        

def clearField():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")



root = tk.Tk()
root.geometry("300x275")


text_result = tk.Text(root, height=2,width=16,font=("Ariel", 24))
text_result.grid(columnspan=5)

#creating buttons
btn1 = tk.Button(root, text="1", command=lambda: addToCalculation(1), width=5, font=("Ariel", 14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: addToCalculation(2), width=5, font=("Ariel", 14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: addToCalculation(3), width=5, font=("Ariel", 14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: addToCalculation(4), width=5, font=("Ariel", 14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: addToCalculation(5), width=5, font=("Ariel", 14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: addToCalculation(6), width=5, font=("Ariel", 14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: addToCalculation(7), width=5, font=("Ariel", 14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: addToCalculation(8), width=5, font=("Ariel", 14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: addToCalculation(9), width=5, font=("Ariel", 14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: addToCalculation(0), width=5, font=("Ariel", 14))
btn0.grid(row=5, column=2)

btnPlus = tk.Button(root, text="+", command=lambda: addToCalculation("+"), width=5, font=("Ariel", 14))
btnPlus.grid(row=2, column=4)
btnMinus = tk.Button(root, text="-", command=lambda: addToCalculation("-"), width=5, font=("Ariel", 14))
btnMinus.grid(row=3, column=4)
btnMult = tk.Button(root, text="*", command=lambda: addToCalculation("*"), width=5, font=("Ariel", 14))
btnMult.grid(row=4, column=4)
btnDiv = tk.Button(root, text="/", command=lambda: addToCalculation("/"), width=5, font=("Ariel", 14))
btnDiv.grid(row=5, column=4)

btnOpen = tk.Button(root, text="(", command=lambda: addToCalculation("("), width=5, font=("Ariel", 14))
btnOpen.grid(row=5, column=1)
btnClose = tk.Button(root, text=")", command=lambda: addToCalculation(")"), width=5, font=("Ariel", 14))
btnClose.grid(row=5, column=3)

btnEquals = tk.Button(root, text="=", command= evaluateCalculation, width=11, font=("Ariel", 14))
btnEquals.grid(row=6, column=1, columnspan=2)
btnClear = tk.Button(root, text="Clear", command=clearField, width=11, font=("Ariel", 14))
btnClear.grid(row=6, column=3, columnspan=2)


root.mainloop()