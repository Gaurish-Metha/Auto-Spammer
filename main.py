import pyautogui as pg
import time
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import threading
import winsound  # For built-in beep sound (Windows only)

# ==============================
# 💣 UNIVERSAL SPAMMER with SOUND FX
# All in one .py file — Coded by Gaurish Metha
# ==============================

# 🔥 Spam Logic
def start_spam(msg, count, sound_enabled, log_fn):
    log_fn(f"💥 Spammer initiated at {datetime.now().strftime('%H:%M:%S')}")
    log_fn("⏳ You have 5 seconds to place your cursor in the chat/text field.")
    time.sleep(5)

    for i in range(count):
        pg.write(msg)
        pg.press("Enter")
        if sound_enabled:
            winsound.Beep(900, 100)  # (freq, duration in ms)
        log_fn(f"📤 Sent: '{msg}' ({i + 1}/{count})")
        time.sleep(0.2)

    log_fn("✅ All messages successfully launched!")
    messagebox.showinfo("Mission Complete", "Spamming is done 😎")

# 💻 GUI Class
class SpammerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💣 Universal Message Spammer v9003 PRO MAX")
        self.root.geometry("520x430")
        self.root.configure(bg="#111111")
        self.root.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#111111", foreground="#ffffff", font=("Segoe UI", 10))
        style.configure("TEntry", padding=5)
        style.configure("TButton", background="#ff4444", foreground="#ffffff", font=("Segoe UI", 10, "bold"))
        style.configure("TCombobox", fieldbackground="#1e1e1e", background="#1e1e1e", foreground="white")

        # 🔤 Message input
        ttk.Label(self.root, text="Enter your message to spam:").pack(pady=(20, 5))
        self.msg_entry = ttk.Entry(self.root, width=50)
        self.msg_entry.insert(0, "Wake up babe, new spam just dropped 💅")
        self.msg_entry.pack(pady=5)

        # 🔁 Times dropdown
        ttk.Label(self.root, text="How many times to spam:").pack(pady=(15, 5))
        self.count_var = tk.IntVar()
        self.count_combo = ttk.Combobox(self.root, textvariable=self.count_var, width=10, state="readonly")
        self.count_combo["values"] = [10, 20, 30, 50, 100]
        self.count_combo.current(2)
        self.count_combo.pack()

        # 🎭 Presets
        ttk.Label(self.root, text="Choose a preset (optional):").pack(pady=(15, 5))
        self.preset_combo = ttk.Combobox(self.root, state="readonly", width=40)
        self.preset_combo["values"] = [
            "💅 Wake up babe, new spam just dropped",
            "🧠💥 ur brain has been hacked by GaurishTheGoat",
            "💀💀💀💀💀💀💀💀💀💀💀💀💀",
            "😂 Why u ignoring me bro??",
            "🐐 Gaurish is HIM 🔥🔥"
        ]
        self.preset_combo.pack()
        self.preset_combo.bind("<<ComboboxSelected>>", self.fill_preset)

        # 🔊 Sound FX
        self.sound_fx = tk.BooleanVar(value=True)
        sound_check = tk.Checkbutton(self.root, text="🔊 Enable Sound FX", variable=self.sound_fx, bg="#111111", fg="white", activebackground="#111111", activeforeground="white", font=("Segoe UI", 10))
        sound_check.pack(pady=(15, 5))

        # 🚀 Start Button
        self.start_btn = ttk.Button(self.root, text="🚀 Start Spamming", command=self.run_spammer)
        self.start_btn.pack(pady=20)

        # 🧾 Console Output
        ttk.Label(self.root, text="📜 Log Console:").pack(pady=(5, 2))
        self.console = tk.Text(self.root, height=8, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 9), relief="flat")
        self.console.pack(padx=15, pady=(0, 15), fill="both")

    def fill_preset(self, event):
        selected = self.preset_combo.get()
        self.msg_entry.delete(0, "end")
        self.msg_entry.insert(0, selected)

    def log(self, msg):
        self.console.insert("end", msg + "\n")
        self.console.see("end")

    def run_spammer(self):
        msg = self.msg_entry.get()
        count = self.count_var.get()
        sound = self.sound_fx.get()

        if not msg or count <= 0:
            messagebox.showerror("Oops!", "Please enter a valid message and number.")
            return

        threading.Thread(target=start_spam, args=(msg, count, sound, self.log), daemon=True).start()

# 🎬 App Start
if __name__ == "__main__":
    root = tk.Tk()
    app = SpammerApp(root)
    root.mainloop()
