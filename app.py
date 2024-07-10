import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr
from pydub import AudioSegment
import os


def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)
    duration = len(audio) / 1000  # Duration in seconds
    
    chunk_size = 60 * 1000  # 60 seconds per chunk
    text = ""
    
    for i in range(0, len(audio), chunk_size):
        chunk = audio[i:i + chunk_size]
        chunk.export("chunk.wav", format="wav")
        
        with sr.AudioFile("chunk.wav") as source:
            audio_data = recognizer.record(source)
            try:
                text_chunk = recognizer.recognize_google(audio_data, language='th-TH')
                text += text_chunk + " "
            except sr.UnknownValueError:
                text += "[Unrecognized] "
            except sr.RequestError as e:
                raise Exception(f"Could not request results from Google Speech Recognition service; {e}")
    
    os.remove("chunk.wav")
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
    
    try:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        for file_path in file_paths:
            text = convert_audio_to_text(file_path)
            result_text.insert(tk.END, f'ข้อความที่ได้จาก {os.path.basename(file_path)}:\n{text}\n\n')
        result_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f'เกิดข้อผิดพลาด: {e}')

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

# สร้างเมนู
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="เลือกไฟล์", command=open_file)
file_menu.add_command(label="บันทึกข้อความ", command=save_text)
file_menu.add_command(label="ล้างข้อความ", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="ออก", command=root.quit)
menubar.add_cascade(label="ไฟล์", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="ข้อมูลผู้พัฒนา", command=show_info)
menubar.add_cascade(label="ช่วยเหลือ", menu=help_menu)

entry_var = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="เลือกไฟล์เสียง:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, textvariable=entry_var, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(frame, text="Browse", command=open_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

transcribe_button = tk.Button(frame, text="แปลงเสียงเป็นข้อความ", command=transcribe_audio)
transcribe_button.grid(row=1, column=0, columnspan=3, pady=10)

result_text = tk.Text(frame, width=60, height=10, state=tk.DISABLED)
result_text.grid(row=2, column=0, columnspan=3, pady=10)

save_button = tk.Button(frame, text="บันทึกข้อความ", command=save_text)
save_button.grid(row=3, column=0, columnspan=3, pady=5)

clear_button = tk.Button(frame, text="ล้างข้อความ", command=clear_text)
clear_button.grid(row=4, column=0, columnspan=3, pady=5)

exit_button = tk.Button(frame, text="ออก", command=root.quit)
exit_button.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
