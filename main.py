import time
import tkinter as tk
from tkinter import ttk
import math
from data import Data, special_characters

LARGEFONT = ("Verdana", 35)
data = Data()
Difficulty = ""
Time : int


BG = '#F6F1F1'
SECOND_BG = '#AFD3E2'
THIRD_BG = '#19A7CE'
FOURTH_BG = '#146C94'


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('750x350')

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - 750) // 2
        y = (screen_height - 350) // 2

        self.geometry(f"{750}x{350}+{x}+{y}")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Test):

            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        try:
            frame.populate_text()
            frame.set_time(self.container)
        except:
            pass
        frame.tkraise()

    def refresh(self):
        self.destroy()
        self.__init__()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background=BG)

        label = ttk.Label(self, text="Typing Tutor", font=LARGEFONT, background=BG, foreground=SECOND_BG)
        label.grid(row=0, column=1, pady=10)

        self.options_list = {"30 sec" : 30, "1 min" : 60, "1.5 min" : 90, "2 min" : 120}

        self.value_inside = tk.StringVar(self)

        self.value_inside.set("Select Time")

        question_menu = tk.OptionMenu(self, self.value_inside, *self.options_list.keys())
        question_menu.grid(row=1, column=1, padx=5, pady=50)

        button1 = tk.Button(self, text="Easy",command=lambda: [self.set_difficulty("Easy"), controller.show_frame(Test)], width=10, bg=SECOND_BG, font=('calibri', 18, 'bold'))
        button1.grid(row=2, column=0, padx=40, pady=20)

        button2 = tk.Button(self, text="Medium", command=lambda: [self.set_difficulty("Medium"), controller.show_frame(Test)], width=10, bg=SECOND_BG,
                            font=('calibri', 18, 'bold'))
        button2.grid(row=2, column=1, padx=0, pady=20)

        button3 = tk.Button(self, text="Hard", command=lambda: [self.set_difficulty("Hard"), controller.show_frame(Test)], width=10, bg=SECOND_BG,
                            font=('calibri', 18, 'bold'))
        button3.grid(row=2, column=2, padx=40, pady=20)




    def set_difficulty(self, difficulty):
        global Difficulty, Time
        Difficulty = difficulty
        Time = self.options_list.get(self.value_inside.get())
        if Time == None:
            Time = 60


class Test(tk.Frame):

    def __init__(self, parent: tk.Frame, controller : MainWindow):
        tk.Frame.__init__(self, parent)
        self.configure(background=BG)

        self.timer = None
        self.root = controller

        self.current_index = 0
        self.mistakes = 0
        self.correct = 0
        self.count_min = None
        self.count_sec = None

        label = ttk.Label(self, text="Time : ", background=BG, font=('calibri', 18, 'bold'), foreground=THIRD_BG)
        label.grid(row=0, column=0, padx=10, pady=10)

        self.time = ttk.Label(self, text='00:00', background=BG, font=('calibri', 18, 'bold'), foreground=THIRD_BG)
        self.time.grid(row=0, column=1, pady=10)


        self.prompt = tk.Text(self, background=BG, font=('calibri', 18, 'bold'), foreground=SECOND_BG, borderwidth=0, width=40, height=5, wrap=tk.WORD)

        self.prompt.tag_configure("center", justify='center')
        self.prompt.tag_add("center", "1.0", "end")
        self.prompt.grid(row=1, column=2, pady=20, columnspan=2)

        self.prompt.tag_configure("red", foreground='red')
        self.prompt.tag_configure("green", foreground='green')
        self.prompt.tag_configure("highlight", font=('calibri', 18, 'bold' and 'underline'))

        self.entry = tk.Text(self, width=50, height=3, wrap=tk.WORD, undo=True)
        self.entry.grid(row=2, column=3, pady=10, padx=30)
        self.entry.configure(font=('calibri', 12, 'bold'), background=SECOND_BG, foreground=FOURTH_BG)

        self.entry.bind("<BackSpace>", lambda event : 'break')


        self.entry.focus_set()


    def set_time(self, parent):

        self.count_min = math.floor(Time/ 60)
        self.count_sec = Time % 60
        self.entry.bind("<KeyPress>", self.check_typing)

        if self.count_sec < 10:
            self.count_sec = f"0{self.count_sec}"

        self.time.configure(text=f"{self.count_min}:{self.count_sec}")
        self.entry.bind("<KeyRelease>", lambda event: self.count_down(Time, parent))

    def populate_text(self):

        prom = data.give_prompt(Difficulty)
        self.prompt.insert(tk.END, prom.strip())
        self.prompt.tag_add("highlight", "1.0")
        self.prompt.tag_add("center", "1.0", "end")
        self.prompt.configure(state='disabled')

    def count_down(self, count, parent):

        self.count_min = math.floor(count / 60)
        self.count_sec = count % 60

        if len(self.entry.get("1.0", tk.END).strip()) == 0:
            self.entry.focus_set()
            return

        if self.count_sec < 10:
            self.count_sec = f"0{self.count_sec}"

        self.time.configure(text=f"{self.count_min}:{self.count_sec}")

        if count > 0:
            self.timer = parent.after(1000, self.count_down, count - 1, parent)
            self.entry.unbind("<KeyRelease>")
        else:
            self.open_progress_window()
            self.entry.configure(state='disabled')



    def check_typing(self, event):

        text = self.prompt.get("1.0", tk.END).strip()

        if event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
            return

        self.prompt.tag_add("highlight", f"1.{self.current_index + 1}")
        self.prompt.tag_remove("highlight", f"1.{self.current_index}")


        if event.keysym == text[self.current_index] or special_characters.get(text[self.current_index]) == event.keysym:
            self.prompt.tag_add("green", f"1.{self.current_index}")
            self.current_index += 1
            self.correct += 1

        else:
            self.prompt.tag_add("red", f"1.{self.current_index}")
            self.current_index += 1
            self.mistakes += 1


        if self.current_index == len(text):

            self.entry.delete("1.0", tk.END)
            self.prompt.configure(state='normal')
            self.prompt.delete("1.0", tk.END)
            self.populate_text()
            self.prompt.configure(state='disabled')
            self.current_index = 0
            self.prompt.tag_add("center", "1.0", "end")

    def show_result(self, parent):

        self.progress_label.pack_forget()
        self.progress_bar.pack_forget()

        TOTAL_CHARCTERS = self.correct + self.mistakes
        GROSS_WPM = round((TOTAL_CHARCTERS / 5) / (Time / 60), 2)
        NET_WPM = round(GROSS_WPM - (self.mistakes / (Time / 60)), 2)
        ACCURACY = round(self.correct / TOTAL_CHARCTERS * 100, 2)

        gross_wpm = tk.Label(parent, text=f"Gross WPM : {GROSS_WPM}", foreground=THIRD_BG, font=('calibri', 18, 'bold'))
        gross_wpm.grid(column=0, row=0, pady=5, padx=80)

        net_wpm = tk.Label(parent, text=f"Net WPM : {NET_WPM}", foreground=THIRD_BG, font=('calibri', 18, 'bold'))
        net_wpm.grid(column=0, row=1, pady=5, padx=80)

        mistakes = tk.Label(parent, text=f"Mistakes : {self.mistakes}", foreground=THIRD_BG, font=('calibri', 18, 'bold'))
        mistakes.grid(column=0, row=2, pady=5, padx=80)

        accuracy = tk.Label(parent, text=f"Accuracy : {ACCURACY}%", foreground=THIRD_BG, font=('calibri', 18, 'bold'))
        accuracy.grid(column=0, row=3, pady=5, padx=80)

        back = tk.Button(parent, text="Back", command=lambda: [self.root.refresh()] , width=10, bg=SECOND_BG, font=('calibri', 12, 'bold') )
        back.grid(column=0, row=4, pady=5, padx=80)

    def open_progress_window(self):

        progress_window = tk.Toplevel(self)
        progress_window.title("Progress")

        progress_window.focus_set()
        screen_width = progress_window.winfo_screenwidth()
        screen_height = progress_window.winfo_screenheight()

        x = (screen_width - 350) // 2
        y = (screen_height - 250) // 2

        progress_window.configure(background=BG)
        progress_window.geometry(f"{350}x{250}+{x}+{y}")


        self.progress_label = tk.Label(progress_window, text="Calculating Results...", padx=20, pady=20, background=BG, borderwidth=0, font=('calibri', 12, 'bold'))
        self.progress_label.pack()

        self.progress_bar = ttk.Progressbar(progress_window, length=300)
        self.progress_bar.pack(pady=20)

        def begin_progress():
            for i in range(101):
                self.progress_bar['value'] = i

                progress_window.update()

                time.sleep(0.05)
                if i > 70:
                    self.progress_label.configure(text='Finalizing Report...')

                elif i > 50:
                    self.progress_label.configure(text='Checking Mistakes..')

                elif i > 25:
                    self.progress_label.configure(text='Analyzing Speed...')

                if i == 100:
                    self.show_result(progress_window)

        progress_window.after(0, begin_progress)


app = MainWindow()

app.mainloop()
