import tkinter as tk



start = datetime.datetime(2022,1,28)

class reamin:
    def __init__(self):

        self.today = datetime.datetime.today()
        self.fin = datetime.datetime(2022,2,28)

        self.screen = tk.Tk()
        self.screen.geometry("200x100")
        self.screen.title("Reminder")
        self.Label = tk.Label(self.screen, text = "Remaining Days :")
        self.Label.pack(side = "top")

        self.diff = self.fin - self.today
        self.Lab = tk.Label(self.screen, text = f"{self.diff.days} day(s)")
        self.Lab.pack(side ="top")

        self.diffs = self.today - start
        self.Lab1 = tk.Label(self.screen, text =f"\nSpended day(s)\n{self.diffs.days}")
        self.Lab1.pack(side ="top")
        self.screen.mainloop()


reamin()