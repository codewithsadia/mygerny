import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

class GrowthMindsetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Growth Mindset Challenge App")
        self.geometry("600x600")
        self.configure(bg="lightblue")

        # Countdown Timer Section
        self.countdown_time = 10  # seconds
        self.countdown_label = tk.Label(self, text=f"Countdown: {self.countdown_time}", 
                                        font=("Arial", 20, "bold"), bg="lightblue", fg="darkblue")
        self.countdown_label.pack(pady=15)
        self.update_countdown()

        # To-Do List Section
        todo_frame = tk.Frame(self, bg="lightblue")
        todo_frame.pack(pady=10)

        self.todo_entry = tk.Entry(todo_frame, font=("Arial", 14), width=30)
        self.todo_entry.pack(side="left", padx=5)

        add_button = tk.Button(todo_frame, text="Add ToDo", font=("Arial", 14), bg="green", fg="white",
                               command=self.add_todo)
        add_button.pack(side="left", padx=5)

        self.todo_listbox = tk.Listbox(self, font=("Arial", 14), width=50, height=6)
        self.todo_listbox.pack(pady=10)

        # API Data Fetch Section
        api_button = tk.Button(self, text="Fetch API Data", font=("Arial", 14), bg="purple", fg="white",
                               command=self.fetch_api_data)
        api_button.pack(pady=10)

        self.api_data_label = tk.Label(self, text="", font=("Arial", 12), bg="lightblue", wraplength=500)
        self.api_data_label.pack(pady=10)

        # Image Display Section
        try:
            # Ensure the image file exists in your project directory or update the path accordingly
            img = Image.open("jewelry.png")
            img = img.resize((200, 200))
            self.photo = ImageTk.PhotoImage(img)
            image_label = tk.Label(self, image=self.photo, bg="lightblue")
            image_label.pack(pady=15)
        except Exception as e:
            print("Image load error:", e)
            error_label = tk.Label(self, text="Image not available", font=("Arial", 12), bg="lightblue", fg="red")
            error_label.pack(pady=15)

    def update_countdown(self):
        if self.countdown_time >= 0:
            self.countdown_label.config(text=f"Countdown: {self.countdown_time}")
            self.countdown_time -= 1
            self.after(1000, self.update_countdown)
        else:
            self.countdown_label.config(text="Time's up!")

    def add_todo(self):
        todo_text = self.todo_entry.get()
        if todo_text:
            self.todo_listbox.insert(tk.END, todo_text)
            self.todo_entry.delete(0, tk.END)

    def fetch_api_data(self):
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
            if response.status_code == 200:
                data = response.json()
                # Display the fetched data in a formatted way
                display_text = f"API Data:\nID: {data.get('id')}\nTitle: {data.get('title')}\nCompleted: {data.get('completed')}"
                self.api_data_label.config(text=display_text)
            else:
                self.api_data_label.config(text="Error fetching data")
        except Exception as e:
            self.api_data_label.config(text=f"Error: {e}")

if __name__ == "__main__":
    app = GrowthMindsetApp()
    app.mainloop()
