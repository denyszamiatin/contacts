from Tkinter import *
import tkMessageBox
import phones
import pickle_ser

class App:
  def __init__(self, master):
    self.master = master
    serializer = pickle_ser.PickleSerializer()
    self.contacts = phones.Contacts(serializer)
    master.protocol("WM_DELETE_WINDOW", self.on_closing)
    frame = Frame(master)
    frame.pack()
    self.name_label = Label(frame, text='Name',justify=LEFT)
    self.name_label.pack()
    self.name = Entry(frame)
    self.name.pack()
    self.phone_label = Label(frame, text='Phone',justify=LEFT)
    self.phone_label.pack()
    self.phone = Entry(frame)
    self.phone.pack()
    self.create = Button(frame, 
                         text="Create",
                         command=self.create_contact)
    self.create.pack(side=RIGHT)
    self.delete = Button(frame,
                         text="Delete",
                         command=self.delete_contact)
    self.delete.pack(side=RIGHT)
    self.update = Button(frame,
                         text="Update",
                         command=self.update_contact)
    self.update.pack(side=RIGHT)
    self.find = Button(frame,
                         text="Find",
                         command=self.find_contact)
    self.find.pack(side=RIGHT)
    self.contact_list = Listbox(frame)
    self.contact_list.pack()
    self.update_listbox()
    
  def update_listbox(self):
    self.contact_list.delete(0, END)
    for name, phone in self.contacts.list_contacts():
      self.contact_list.insert(END, "{}: {}".format(name, phone))
    
  def create_contact(self):
    try:
      self.contacts.add_contact(self.name.get(), self.phone.get())
      self.update_listbox()
    except KeyError as e:
        tkMessageBox.showinfo('Ok', str(e))
    
  def delete_contact(self):
    try:
      self.contacts.delete_contact(self.name.get())
      self.update_listbox()
    except KeyError as e:
        tkMessageBox.showinfo('Ok', str(e))
    
  def update_contact(self):
    try:
      self.contacts.update_contact(self.name.get(), self.phone.get())
      self.update_listbox()
    except KeyError as e:
        tkMessageBox.showinfo('Ok', str(e))

  def find_contact(self):
    try:
      tkMessageBox.showinfo('Ok', self.contacts.get_phone(self.name.get()))
    except KeyError as e:
      tkMessageBox.showinfo('Ok', str(e))
      
  def on_closing(self):
     self.contacts.save()
     tkMessageBox.showinfo('Ok', 'Exit')
     self.master.destroy()
        
root = Tk()
app = App(root)
root.mainloop()
