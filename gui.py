import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from threading import Thread
import sys
import os

class VoiceAssistantGUI:
    def _init_(self, master):
        self.master = master
        master.title("Voice Assistant")

        self.output_text = scrolledtext.ScrolledText(master, width=50, height=15)
        self.output_text.pack(pady=10)

        self.input_label = tk.Label(master, text="Enter your command:")
        self.input_label.pack()

        self.input_entry = tk.Entry(master, width=50)
        self.input_entry.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.process_command)
        self.submit_button.pack(pady=5)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_output)
        self.clear_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_program)
        self.exit_button.pack(pady=5)

    def process_command(self):
        command = self.input_entry.get()
        if command:
            self.output_text.insert(tk.END, f"User: {command}\n")
            self.input_entry.delete(0, tk.END)
            self.execute_command(command)
        else:
            messagebox.showinfo("Error", "Please enter a command.")

    def execute_command(self, command):
        # Here you can call your voice assistant functions based on the command
        # For example:
        if command == "jarvis":
            speak("Hello! How can I assist you today?")
        pass

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def exit_program(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            sys.exit()

def main():
    root = tk.Tk()
    root.geometry("400x400")
    app = VoiceAssistantGUI(root)
    root.mainloop()

if __name__== "_main_":
    main()