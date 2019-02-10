import  tkinter as tk
from socketserver import BaseRequestHandler, TCPServer
from threading import Thread
import Server


class UI:


    def element(self):
        self.label1Txt = tk.StringVar()
        self.label1=tk.Label(text='label1Txt')
    def __init__(self):

        window = tk.Tk()
        window.title('Server')
        window.geometry('400x200')
        self.window=window
        self.element()
    def main(self):


        self.window.mainloop()

if __name__ == '__main__':
    x=UI()
    x.main()