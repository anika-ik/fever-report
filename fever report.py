from tkinter import*
root= Tk()
root.title("fever report")
root.geometry("600x600")

question1_radiobutton= StringVar(value="0")

question1= Label(root, text= "do you have headache and soar throat")
question1.pack()
question1_r1= Radiobutton(root, text= "yes", variable= question1_radiobutton, value="yes")
question1_r1.pack()
question1_r2= Radiobutton(root, text= "no", variable= question1_radiobutton, value= "no")
question1_r2.pack()


question2_radiobutton= StringVar(value="0")

question2= Label(root, text= "is your body temperature high?")
question2.pack()
question2_r1= Radiobutton(root, text= "yes", variable= question2_radiobutton, value="yes")
question2_r1.pack()
question2_r2= Radiobutton(root, text= "no", variable= question2_radiobutton, value= "no")
question2_r2.pack()

question3_radiobutton= StringVar(value="0")

question3= Label(root, text= "do you have any symptoms of eye redness?")
question3.pack()
question3_r1= Radiobutton(root, text= "yes", variable= question3_radiobutton, value="yes")
question3_r1.pack()
question3_r2= Radiobutton(root, text= "no", variable= question3_radiobutton, value= "no")
question3_r2.pack()

def fever_score():
    score= 0
    if question1_radiobutton.get()=="yes":
        score= score+20
        print(score)
    if question2_radiobutton.get()=="yes":
        score= score+20
        print(score)
    if question3_radiobutton.get()=="yes":
        score= score+20
        print(score)
        
    if score<=20:
        messagebox.showinfo("Report", "you dont need to visit a doctor")
    elif score > 20 and score<=40:
        messagebox.showinfo("Report", "you might perhaps have to visit a doctor")
    else:
        messagebox.showinfo("Report", "I strongly advice you to go visit a doctor")
        

btn= Button(root, text="click me", command= fever_score)
btn.pack()
root.mainloop()