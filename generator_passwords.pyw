import random
from tkinter import messagebox, filedialog, Button, Entry, ttk, Label, Tk

class Generator():
    def __init__(self):

        self.window()


    def RemoveDupliChar(self):
        self.NewWord = ''
        for char in self.chars:
            if char not in self.NewWord:
                self.NewWord += char
        print(self.NewWord.strip())

    def skript_generator_passwords(self):
        self.wrongPasswords = []
        try:
            self.file = open(filedialog.askopenfilename(), 'r')
            self.filename = self.file.name
            for line in self.file:
                self.wrongPasswords.append(line.strip())
            self.file.close()
        except FileNotFoundError:messagebox.showerror("1101", "File not Found")

        if self.lendthpass.get() == None or self.slovar.get() == None or self.lendthpass.get() == '' or self.slovar.get() == '':
            messagebox.showerror("1402", "Одно из полей ввода пустое")
        else:
            self.length = int(self.lendthpass.get())
            self.chars = str(self.slovar.get())
            self.RemoveDupliChar()
            self.password = ""

            self.num = self.length
            self.nowcombines = len(self.wrongPasswords)
            self.result = len(self.NewWord)
            self.maxcombine = self.result

            while True:
                if self.num == 1:
                    break
                self.maxcombine = self.result * self.maxcombine
                self.num -= 1

            while True:
                self.a = 0
                self.progress['maximum'] = self.maxcombine
                self.progress['value'] = self.nowcombines
                self.tk.update_idletasks()

                self.password = ""

                for i in range(self.length):
                    self.password += random.choice(self.chars)

                if self.password not in self.wrongPasswords:
                    self.nowcombines += 1
                    self.wrongPasswords.append(self.password)
                    self.file = open(self.filename, 'a')
                    self.file.write(str(self.password) + "\n")
                    print(self.nowcombines)
                if self.nowcombines == self.maxcombine or self.nowcombines > self.maxcombine:
                    messagebox.showinfo("Ending", "You password file is generated")
                    self.progress['value'] = 0
                    break

    def window(self):
        self.tk = Tk()
        x = (self.tk.winfo_screenwidth() - self.tk.winfo_reqwidth()) / 2
        y = (self.tk.winfo_screenheight() - self.tk.winfo_reqheight()) / 2
        self.tk.wm_geometry("+%d+%d" % (x, y))
        self.tk.minsize(400, 100)
        self.tk.resizable(False, False)
        self.tk.title('Generator passwords')

        self.knopka = Button(self.tk, text="Generate", command=self.skript_generator_passwords, bg='black', fg='yellow', width=50)
        self.knopka.grid(column=1, row=6, columnspan=3)

        text1 = Label(self.tk, text="Длина пароля:")
        text1.grid(column=2, row=1)

        self.lendthpass = Entry(self.tk, width=2)
        self.lendthpass.grid(column=2, row=2)

        text2 = Label(self.tk, text="Словарь для генерации пароля")
        text2.grid(column=2, row=3)

        self.slovar = Entry(self.tk, width=40)
        self.slovar.grid(column=2, row=4)


        self.progress = ttk.Progressbar(self.tk, maximum=100, length=400)
        self.progress.grid(column=1, row=5, columnspan=3)

        self.tk.mainloop()

if __name__ == "__main__":
    Generator()