from queue import Queue
from tkinter import Tk

tasks = Queue()
responses = Queue()

root = None
def get():
  global root
  if root is not None:
    root.iconify()
    root.deiconify()
    root.withdraw()
  else:
    root = Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    root.attributes('-alpha', 0)
    root.geometry("0x0")
  return root
