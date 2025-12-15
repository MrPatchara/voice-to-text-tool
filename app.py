import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment
import os
import threading
from tkinter import ttk
import tempfile

def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)
    duration = len(audio) / 1000  # Duration in seconds
    
    chunk_size = 60 * 1000  # 60 seconds per chunk
    text = ""
    # Use a temporary wav per chunk to avoid conflicts and ensure cleanup
    for i in range(0, len(audio), chunk_size):
        chunk = audio[i:i + chunk_size]
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp_path = tmp.name
        try:
            chunk.export(tmp_path, format="wav")
            with sr.AudioFile(tmp_path) as source:
                audio_data = recognizer.record(source)
                try:
                    text_chunk = recognizer.recognize_google(audio_data, language='th-TH')
                    text += text_chunk + " "
                except sr.UnknownValueError:
                    text += "[Unrecognized] "
                except sr.RequestError as e:
                    raise Exception(f"Could not request results from Google Speech Recognition service; {e}")
        finally:
            try:
                os.remove(tmp_path)
            except Exception:
                pass
    return text.strip()

def open_file():
    file_paths = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.wav *.mp3")])
    if file_paths:
        entry_var.set(";".join(file_paths))

def transcribe_audio():
    file_paths = entry_var.get().split(";")
    if not file_paths or file_paths == ['']:
        messagebox.showwarning("Warning", "กรุณาเลือกไฟล์เสียง")
        return
    
    def worker(paths):
        try:
            progress_bar.config(mode="indeterminate")
            progress_bar.start()
            set_busy(True, "กำลังประมวลผล...")
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            for idx, file_path in enumerate(paths):
                if not file_path:
                    continue
                try:
                    text = convert_audio_to_text(file_path)
                    result_text.insert(tk.END, f'ข้อความที่ได้จาก {os.path.basename(file_path)}:\n{text}\n\n')
                except Exception as e:
                    result_text.insert(tk.END, f'เกิดข้อผิดพลาดจาก {os.path.basename(file_path)}: {e}\n\n')
            result_text.config(state=tk.DISABLED)
        finally:
            progress_bar.stop()
            set_busy(False, "เสร็จสิ้น")

    threading.Thread(target=worker, args=(file_paths,), daemon=True).start()

def set_busy(is_busy, status=""):
    # Disable/enable UI while processing and update status
    browse_button.config(state=tk.DISABLED if is_busy else tk.NORMAL)
    transcribe_button.config(state=tk.DISABLED if is_busy else tk.NORMAL)
    save_button.config(state=tk.DISABLED if is_busy else tk.NORMAL)
    clear_button.config(state=tk.DISABLED if is_busy else tk.NORMAL)
    exit_button.config(state=tk.DISABLED if is_busy else tk.NORMAL)
    progress_label.config(text=status)

def save_text():
    text_content = result_text.get(1.0, tk.END)
    if not text_content.strip():
        messagebox.showwarning("Warning", "ไม่มีข้อความให้บันทึก")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_content)
        messagebox.showinfo("Information", "บันทึกข้อความสำเร็จ")

def clear_text():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.config(state=tk.DISABLED)

def show_info():
    messagebox.showinfo("ติดต่อผู้พัฒนา", "Email: Patcharaalumaree@gmail.com\nGitHub: https://github.com/MrPatchara")

root = tk.Tk()
root.title("โปรแกรมแปลงเสียงเป็นข้อความ")
root.geometry("700x600")
root.minsize(600, 500)

# Formal dark mode palette and fonts
DARK_BG = "#121212"          # background
DARK_PANEL = "#1e1e1e"       # panel
DARK_INPUT = "#232323"       # input
DARK_TEXT = "#e0e0e0"        # text
ACCENT = "#3d77ff"           # primary accent
ACCENT2 = "#5a8aff"          # hover accent
HUD_GREEN = "#84d88e"        # status green (subtle)
STEEL_GRAY = "#3a3a3a"       # divider

RETRO_FONT = ("Segoe UI", 10)
RETRO_TITLE_FONT = ("Segoe UI Semibold", 13)

root.configure(bg=DARK_BG)

style = ttk.Style()
style.theme_use("clam")

# Frames
style.configure("TFrame", background=DARK_BG)
style.configure("Panel.TFrame", background=DARK_PANEL)
style.configure("Header.TFrame", background=DARK_BG)

# Labels
style.configure("TLabel", background=DARK_BG, foreground=DARK_TEXT, font=RETRO_FONT)
style.configure("Hint.TLabel", background=DARK_BG, foreground="#b0b0b0", font=("Segoe UI", 9))
style.configure("Title.TLabel", background=DARK_BG, foreground=ACCENT, font=RETRO_TITLE_FONT)

# Buttons
style.configure("TButton", background=DARK_PANEL, foreground=DARK_TEXT, padding=8, font=RETRO_FONT, borderwidth=1)
style.map("TButton",
          background=[("active", ACCENT2), ("focus", ACCENT)],
          foreground=[("active", "#ffffff"), ("focus", "#ffffff")])

# Entry fields
style.configure("TEntry", fieldbackground=DARK_INPUT, foreground=DARK_TEXT, insertcolor=DARK_TEXT, padding=6, font=RETRO_FONT)
style.map("TEntry", fieldbackground=[("focus", "#2a2a2a")])

# Progress bar in hazard orange
style.configure("TProgressbar", troughcolor=DARK_PANEL, background=ACCENT)

# Menus in formal colors
menubar = tk.Menu(root, bg=DARK_PANEL, fg=DARK_TEXT, activebackground=ACCENT, activeforeground="#ffffff")
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0, bg=DARK_PANEL, fg=DARK_TEXT, activebackground=ACCENT, activeforeground="#ffffff")
file_menu.add_command(label="เลือกไฟล์", command=open_file)
file_menu.add_command(label="บันทึกข้อความ", command=save_text)
file_menu.add_command(label="ล้างข้อความ", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="ออก", command=root.quit)
menubar.add_cascade(label="ไฟล์", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0, bg=DARK_PANEL, fg=DARK_TEXT, activebackground=ACCENT, activeforeground="#ffffff")
help_menu.add_command(label="ข้อมูลผู้พัฒนา", command=show_info)
menubar.add_cascade(label="ช่วยเหลือ", menu=help_menu)

entry_var = tk.StringVar()

# Main container
frame = ttk.Frame(root, style="TFrame", padding=12)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Header with formal Thai labels
header = ttk.Frame(frame, style="Header.TFrame", padding=(4, 2))
header.grid(row=0, column=0, sticky="ew", pady=(0, 6))
header.columnconfigure(0, weight=1)
title = ttk.Label(header, text="ระบบแปลงเสียงเป็นข้อความ", style="Title.TLabel")
title.grid(row=0, column=0, sticky="w")
subtitle = ttk.Label(header, text="ภาษาไทย | ความคมชัดสูง", style="Hint.TLabel")
subtitle.grid(row=1, column=0, sticky="w")

# Industrial separator
sep = ttk.Frame(frame, style="Panel.TFrame", padding=0)
sep.grid(row=1, column=0, sticky="ew")
sep.configure(height=2)
sep.grid_propagate(False)

# Input panel
input_panel = ttk.Frame(frame, style="Panel.TFrame", padding=12)
input_panel.grid(row=2, column=0, sticky="ew")
input_panel.columnconfigure(1, weight=1)

label = ttk.Label(input_panel, text="เลือกไฟล์เสียง:")
label.grid(row=0, column=0, padx=6, pady=6, sticky="w")

entry = ttk.Entry(input_panel, textvariable=entry_var)
entry.grid(row=0, column=1, padx=6, pady=6, sticky="ew")

browse_button = ttk.Button(input_panel, text="Browse", command=open_file)
browse_button.grid(row=0, column=2, padx=6, pady=6)

transcribe_button = ttk.Button(input_panel, text="แปลงเสียงเป็นข้อความ", command=transcribe_audio)
transcribe_button.grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")

# Progress area
progress_panel = ttk.Frame(frame, style="Panel.TFrame", padding=12)
progress_panel.grid(row=3, column=0, sticky="ew", pady=(8, 0))
progress_panel.columnconfigure(0, weight=1)

progress_label = ttk.Label(progress_panel, text="สถานะ: พร้อมทำงาน", style="Hint.TLabel")
progress_label.grid(row=0, column=0, sticky="w")

progress_bar = ttk.Progressbar(progress_panel, mode="indeterminate")
progress_bar.grid(row=1, column=0, sticky="ew", pady=(6, 0))

# Result text panel (add missing container and layout)
text_panel = ttk.Frame(frame, style="Panel.TFrame", padding=12)
text_panel.grid(row=4, column=0, sticky="nsew", pady=(8, 0))
frame.rowconfigure(4, weight=1)
text_panel.columnconfigure(0, weight=1)
text_panel.rowconfigure(0, weight=1)

# Result text console styling
result_text = tk.Text(text_panel, bg=DARK_INPUT, fg=DARK_TEXT, insertbackground=DARK_TEXT,
                   relief="sunken", bd=1, highlightthickness=1,
                   highlightbackground=STEEL_GRAY, highlightcolor=ACCENT)
result_text.grid(row=0, column=0, sticky="nsew")

# Action buttons
actions_panel = ttk.Frame(frame, style="Panel.TFrame", padding=12)
actions_panel.grid(row=5, column=0, sticky="ew", pady=(8, 0))
actions_panel.columnconfigure((0,1,2,3), weight=1)

save_button = ttk.Button(actions_panel, text="บันทึกข้อความ", command=save_text)
save_button.grid(row=0, column=0, padx=6, pady=6, sticky="ew")

clear_button = ttk.Button(actions_panel, text="ล้างข้อความ", command=clear_text)
clear_button.grid(row=0, column=1, padx=6, pady=6, sticky="ew")

exit_button = ttk.Button(actions_panel, text="ออก", command=root.quit)
exit_button.grid(row=0, column=2, padx=6, pady=6, sticky="ew")

# Buttons slight width and emphasis
save_button.config(width=16)
clear_button.config(width=16)
exit_button.config(width=12)
browse_button.config(style="TButton")
transcribe_button.config(style="TButton")

root.mainloop()
