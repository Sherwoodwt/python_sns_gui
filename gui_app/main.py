import tkinter

from .sns_functions import (
  list_subscriptions,
  create_topic,
  create_subscription,
)

root = tkinter.Tk()

class TestBox(tkinter.Frame):

  def list_subs(self):
    subs = list_subscriptions(self.topic)
    output = ''
    for sub in subs:
      output += sub['Endpoint'] + '\n'
    self.textbox.insert(tkinter.INSERT, output)

  def subscribe(self):
    # WRITE THIS FUNCTION YOU STUPID ANIMAL

  def setup(self):
    self.display = tkinter.Button(self, text='Display', command=self.list_subs)
    self.display.pack(side='top')

    self.signup = tkinter.Button(self, text='Sign up', command=self.subscribe)
    self.signup.pack(side='top')
    
    self.textbox = tkinter.Text(self, height=20, width=80)
    self.textbox.pack(side='top')

    self.exit = tkinter.Button(self, text='Exit', command=root.destroy)
    self.exit.pack(side='bottom')

  def __init__(self, master=None):
    super().__init__(master)
    self.pack()
    self.setup()
    self.topic = create_topic('notification_gui')


def run():
  box = TestBox(master=root)
  box.mainloop()
