from tkinter import *
root = Tk()
root.title("fibonacci")
root.geometry("400x400")
input_box = Entry(root)
label_series = Label(root , text = "fibonacci series")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    num = int(input_box.get())
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter+1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    label_flower["text"] = "flower is full bloomed"
    label_spiral["text"] = "spirals in the right direction are" + str(first_no)+"and spiral in left direction are"+str(second_no)
  
	
btn = Button(root, text="show fibonacci series", command=fibonacci)
 
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
input_box.pack()
root.mainloop()      