import threading
import tkinter as tk
import time
from tkinter import messagebox

sentence = "fondue cheeseburger blue castello. feta swiss danish fontina ricotta goat cheesecake fromage frais macaroni cheese. cheese on toast airedale squirty cheese cheese and biscuits emmental cheesy grin babybel cow. jarlsberg brie rubber cheese ricotta roquefort chalk and cheese danish fontina goat. croque monsieur cheeseburger portsalut."
sentence_position = 0
tag_name = 0
tag_position1 = 0
tag_position2 = 1
mistake_count = 0

class MyApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("600x500")
        frame = tk.Frame(self.master)
        frame.pack()
        self.time_label = tk.Label(frame, text="", font=("", 20))
        self.time_label.pack()
        self.text = tk.Text(frame, font=("Meiryo", 20))
        self.text.insert(0., sentence)
        self.text.pack()
        self.master.bind("<KeyPress>", self.typing_check)

        t = threading.Thread(target=self.timer)
        t.start()

    def typing_check(self, event):
        global sentence_position
        global tag_name
        global tag_position1
        global tag_position2
        global mistake_count
        index1 = f"1.{tag_position1}"
        index2 = f"1.{tag_position2}"
        self.text.tag_add(str(tag_name), index1, index2)
        if sentence_position == 333 and event.keycode == 190:
            self.flag = False
            minute = round(self.second / 60, 2)
            wpm = round((334 / 5) / minute, 2)
            messagebox.showinfo("リザルト", f"あなたのwpmは:{wpm}\nかかった時間:{self.second}秒\n間違い:{mistake_count}個")
        elif sentence[sentence_position] == event.keysym:
            self.text.tag_config(str(tag_name), foreground="green")
            sentence_position += 1
            tag_name += 1
            tag_position1 += 1
            tag_position2 += 1
        elif sentence[sentence_position] == "\u0020" and event.keysym == "space":
            sentence_position += 1
            tag_name += 1
            tag_position1 += 1
            tag_position2 += 1
        elif sentence[sentence_position] == "." and event.keycode == 190:
            sentence_position += 1
            tag_name += 1
            tag_position1 += 1
            tag_position2 += 1
        else:
            self.text.tag_config(str(tag_name), foreground="red")
            mistake_count += 1

    def timer(self):
        self.second = 0
        self.flag = True
        while self.flag:
            self.second += 1
            self.time_label.configure(text=f"経過時間:{self.second}秒")
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("タイピングテスト！")
    app = MyApp(master=root)
    app.mainloop()
