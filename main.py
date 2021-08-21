#Author Name: Holly Bancroft
# Date: 4/26/2021
#Program Name: Bancroft_OrderFoodGUI.py
#Purpose: Allow user to select food items, and display food items and cost in a GUI

import tkinter
import tkinter.messagebox

class MyGUI:

  def __init__(self):
   self.main_window = tkinter.Tk()

   self.top_frame = tkinter.Frame(self.main_window)
   self.bottom_frame = tkinter.Frame(self.main_window)

   self.cb_var1 = tkinter.IntVar()
   self.cb_var2 = tkinter.IntVar()
   self.cb_var3 = tkinter.IntVar()
   self.cb_var4 = tkinter.IntVar()
   self.cb_var5 = tkinter.IntVar()
   self.cb_var6 = tkinter.IntVar()

   self.cb_var1.set(0)
   self.cb_var2.set(0)
   self.cb_var3.set(0)
   self.cb_var4.set(0)
   self.cb_var5.set(0)
   self.cb_var6.set(0)

   self.cb1 = tkinter.Checkbutton(self.top_frame, text="Burger", variable=self.cb_var1)
   self.cb2 = tkinter.Checkbutton(self.top_frame, text="Chicken Sandwich", variable=self.cb_var2)
   self.cb3 = tkinter.Checkbutton(self.top_frame, text="Fries", variable=self.cb_var3)
   self.cb4 = tkinter.Checkbutton(self.top_frame, text="Soda", variable=self.cb_var4)
   self.cb5 = tkinter.Checkbutton(self.top_frame, text="No pickle", variable=self.cb_var5)
   self.cb6 = tkinter.Checkbutton(self.top_frame, text="Extra pickle", variable=self.cb_var6)

   self.cb1.pack()
   self.cb2.pack()
   self.cb3.pack()
   self.cb4.pack()
   self.cb5.pack()
   self.cb6.pack()

   self.order_button = tkinter.Button(self.bottom_frame, text="Order", command=self.show_order)
   self.cancel_button = tkinter.Button(self.bottom_frame, text="Cancel", command=self.main_window.destroy)

   self.order_button.pack(side="left")
   self.cancel_button.pack(side="left")

   self.top_frame.pack()
   self.bottom_frame.pack()

   tkinter.mainloop()

  def show_order(self):

    total = 0
    self.message = "Your order and total is \n"

    if self.cb_var1.get() == 1:
      total += 5
      self.message = self.message + "Burger ($5.00)\n"
    if self.cb_var2.get() == 1:
      total += 6
      self.message = self.message + "Chicken sandwich ($6.00)\n"
    if self.cb_var3.get() == 1:
      total += 2
      self.message= self.message + "Fries ($2.00)\n"
    if self.cb_var4.get()== 1:
      total += 1
      self.message= self.message + "Soda ($1.00)\n"
    if self.cb_var5.get()==1:
      total -= .25
      self.message= self.message + "No pickle (-$0.25)\n"
    if self.cb_var6.get()==1:
      total+= .25
      self.message= self.message + "Extra pickle (+$0.25)\n"

    self.message = self.message + " Total: " + str(total)

    tkinter.messagebox.showinfo("Order: ", self.message)


my_gui = MyGUI()

