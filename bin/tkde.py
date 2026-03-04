import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("vpyOS v1.2")
    root.attributes('-fullscreen', True)
    root.configure(bg="#00AAAA")

    # --- TOP BAR (NO CLOCK) ---
    top_bar = tk.Frame(root, bg="white", bd=1, relief="solid")
    top_bar.pack(side="top", fill="x")

    tk.Label(top_bar, text="vpyOS v1.2", bg="white", font=("Courier", 10, "bold"), padx=10).pack(side="left")

    def system_exit():
        if messagebox.askyesno("vpyOS", "Are you sure to end tk session?"):
            root.destroy()

    tk.Button(top_bar, text="EXIT", bg="#AAAAAA", font=("Courier", 10, "bold"), 
              relief="solid", bd=1, command=system_exit, padx=10).pack(side="right")

    # --- DESKTOP ---
    desktop = tk.Frame(root, bg="#00AAAA")
    desktop.pack(fill="both", expand=True)

    # --- WINDOW DRAG LOGIC ---
    def make_draggable(win, t_bar):
        def start_move(event):
            win.x = event.x
            win.y = event.y
        def do_move(event):
            x = win.winfo_x() + event.x - win.x
            y = win.winfo_y() + event.y - win.y
            win.place(x=x, y=y)
        t_bar.bind("<Button-1>", start_move)
        t_bar.bind("<B1-Motion>", do_move)

    # --- WINDOW BUILDER ---
    def create_window(title):
        win = tk.Frame(desktop, bg="white", bd=2, relief="solid")
        t_bar = tk.Frame(win, bg="#0000AA", bd=1, relief="solid", cursor="fleur")
        t_bar.pack(fill="x")
        
        tk.Label(t_bar, text=title, fg="white", bg="#0000AA", font=("Courier", 10, "bold")).pack(side="left", padx=5)
        tk.Button(t_bar, text="▼", bg="#AAAAAA", font=("Courier", 8), bd=1,
                  command=win.place_forget).pack(side="right")
        
        make_draggable(win, t_bar)
        return win

    # --- CALC.APP ---
    calc_win = create_window("Calc.app")
    calc_entry = tk.Entry(calc_win, bg="white", font=("Courier", 14), justify="right", bd=2, relief="solid")
    calc_entry.pack(fill="x", padx=5, pady=5)
    
    btns_frame = tk.Frame(calc_win, bg="white")
    btns_frame.pack(fill="both", expand=True, padx=5, pady=5)
    
    calc_buttons = ['7','8','9','/','4','5','6','*','1','2','3','-','C','0','=','+']
    for i, b in enumerate(calc_buttons):
        def cmd(x=b):
            if x == '=':
                try:
                    res = eval(calc_entry.get())
                    calc_entry.delete(0, "end")
                    calc_entry.insert("end", str(res))
                except:
                    calc_entry.delete(0, "end")
                    calc_entry.insert("end", "ERROR")
            elif x == 'C':
                calc_entry.delete(0, "end")
            else:
                calc_entry.insert("end", x)
        tk.Button(btns_frame, text=b, width=4, height=2, bg="#AAAAAA", relief="solid", command=cmd).grid(row=i//4, column=i%4, sticky="nsew")

    # --- WRITE.APP ---
    write_win = create_window("Write.app")
    tk.Text(write_win, bg="white", font=("Courier", 12), bd=1, relief="solid").pack(fill="both", expand=True, padx=2, pady=2)

    # --- DOCK (BOTTOM PANEL) ---
    dock = tk.Frame(root, bg="#AAAAAA", bd=2, relief="solid")
    dock.pack(side="bottom", fill="x")

    tk.Button(dock, text="Calc.app", bg="white", font=("Courier", 10, "bold"), relief="sunken", 
              command=lambda: calc_win.place(x=50, y=50, width=250, height=320)).pack(side="left", padx=5, pady=5)
    
    tk.Button(dock, text="Write.app", bg="white", font=("Courier", 10, "bold"), relief="sunken", 
              command=lambda: write_win.place(x=350, y=50, width=500, height=400)).pack(side="left", padx=5, pady=5)

    root.bind("<Escape>", lambda e: system_exit())
    root.mainloop()