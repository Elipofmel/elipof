import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("countries.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    capital TEXT,
    language TEXT
)
""")

sample_data = [
    ("ایران", "تهران", "فارسی"),
    ("فرانسه", "پاریس", "فرانسوی"),
    ("آلمان", "برلین", "آلمانی"),
    ("ژاپن", "توکیو", "ژاپنی")
]

for c in sample_data:
    try:
        cur.execute("INSERT INTO countries (name, capital, language) VALUES (?, ?, ?)", c)
    except:
        pass
conn.commit()

root = tk.Tk()
root.title("کشورها و پایتخت‌ها")

var_country = tk.StringVar()
cur.execute("SELECT name FROM countries")
countries = [row[0] for row in cur.fetchall()]
dropdown = tk.OptionMenu(root, var_country, *countries)
dropdown.pack()


label_result = tk.Label(root, text="اطلاعات نمایش داده می‌شود")
label_result.pack()


def show_info():
    country = var_country.get()
    if country:
        cur.execute("SELECT capital, language FROM countries WHERE name=?", (country,))
        row = cur.fetchone()
        if row:
            label_result.config(text=f"پایتخت: {row[0]} | زبان: {row[1]}")
        else:
            label_result.config(text="کشور پیدا نشد")

btn_show = tk.Button(root, text="نمایش", command=show_info)
btn_show.pack()

entry_name = tk.Entry(root)
entry_name.insert(0, "نام کشور")
entry_name.pack()

entry_capital = tk.Entry(root)
entry_capital.insert(0, "پایتخت")
entry_capital.pack()

entry_lang = tk.Entry(root)
entry_lang.insert(0, "زبان")
entry_lang.pack()

def add_country():
    name = entry_name.get()
    cap = entry_capital.get()
    lang = entry_lang.get()
    try:
        cur.execute("INSERT INTO countries (name, capital, language) VALUES (?, ?, ?)", (name, cap, lang))
        conn.commit()
        messagebox.showinfo("موفق", "کشور اضافه شد")
        var_country.set(name)
        dropdown["menu"].add_command(label=name, command=tk._setit(var_country, name))
    except:
        messagebox.showerror("خطا", "این کشور از قبل وجود دارد")



btn_add = tk.Button(root, text="اضافه کردن", command=add_country)
btn_add.pack()

def delete_country():
    country = var_country.get()
    if country:
        cur.execute("DELETE FROM countries WHERE name=?", (country,))
        conn.commit()
        messagebox.showinfo("حذف", f"{country} حذف شد")
        dropdown["menu"].delete(0, "end")
        cur.execute("SELECT name FROM countries")
        new_list = [row[0] for row in cur.fetchall()]
        for c in new_list:
            dropdown["menu"].add_command(label=c, command=tk._setit(var_country, c))
        if new_list:
            var_country.set(new_list[0])
        else:
            var_country.set("")

btn_delete = tk.Button(root, text="حذف کشور انتخاب‌شده", command=delete_country)
btn_delete.pack()

root.mainloop()
