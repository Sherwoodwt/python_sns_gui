import tkinter

root = tkinter.Tk()

class TestBox(tkinter.Frame):

  def display_hello(self):
    print('Hello World')

  def setup(self):
    self.display = tkinter.Button(self, text='Display', command=self.display_hello)
    self.display.pack(side='top')

    self.exit = tkinter.Button(self, text='Exit', command=root.destroy)
    self.exit.pack(side='bottom')

  def __init__(self, master=None):
    super().__init__(master)
    self.pack()
    self.setup()


def run():
  box = TestBox(master=root)
  box.mainloop()
