import tkinter as tk
from tkinter import messagebox

class LibraryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Manish's Library Management System")
        self.master.geometry("400x400")
        self.master.config(bg='#708090')
        
        self.dark_mode = False # Initialize dark mode to False

        self.books = []
        self.lend_list = []

        # Labels
        self.login_label = tk.Label(self.master, text="Manish's Library Management System", font=("Arial", 20, "bold"), bg='#708090', fg='white')
        self.login_label.pack(pady=20)
        self.username_label = tk.Label(self.master, text="Username:", font=("Arial", 14), bg='#708090', fg='white')
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.master, font=("Arial", 14))
        self.username_entry.pack(pady=5)
        self.password_label = tk.Label(self.master, text="Password:", font=("Arial", 14), bg='#708090', fg='white')
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.master, font=("Arial", 14), show="*")
        self.password_entry.pack(pady=5)
        

# Login
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Arial", 14), bg='#4CAF50', fg='white')
        self.login_button.pack(pady=10, padx=20, ipadx=10)

# Register
        self.register_button = tk.Button(self.master, text="Register", command=self.register, font=("Arial", 14), bg='#FFC107', fg='white')
        self.register_button.pack(pady=10, padx=20, ipadx=10)

        self.username = ""
        self.password = ""
        self.librarians = []      
 

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        for librarian in self.librarians:
            if self.username == librarian[0] and self.password == librarian[1]:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.login_label.destroy()
                self.username_label.destroy()
                self.username_entry.destroy()
                self.password_label.destroy()
                self.password_entry.destroy()
                self.login_button.destroy()
                self.register_button.destroy()
                self.library_management_screen()
                return
        messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.librarians.append([self.username, self.password])
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        


    def library_management_screen(self):
        self.add_book_label = tk.Label(self.master, text="Add Book", font=("Helvetica", 16), bg='#708090', fg='white')
        self.add_book_label.pack(pady=(10,0))
        self.add_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.add_book_entry.pack(pady=5)
        self.add_book_button = tk.Button(self.master, text="Add Book", command=self.add_book, font=("Helvetica", 12))
        self.add_book_button.pack(pady=5)
     
        self.remove_book_label = tk.Label(self.master, text="Remove Book", font=("Helvetica", 16), bg='#708090', fg='white')
        self.remove_book_label.pack(pady=(10,0))
        self.remove_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.remove_book_entry.pack(pady=5)
        self.remove_book_button = tk.Button(self.master, text="Remove Book", command=self.remove_book, font=("Helvetica", 12))
        self.remove_book_button.pack(pady=5)
    
        self.issue_book_label = tk.Label(self.master, text="Issue Book", font=("Helvetica", 16), bg='#708090', fg='white')
        self.issue_book_label.pack(pady=(10,0))
        self.issue_book_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.issue_book_entry.pack(pady=5)
        self.issue_book_button = tk.Button(self.master, text="Issue Book", command=self.issue_book, font=("Helvetica", 12))
        self.issue_book_button.pack(pady=5)
    
        self.view_books_button = tk.Button(self.master, text="View Books", command=self.view_books, font=("Helvetica", 12))
        self.view_books_button.pack(pady=(10,0))
    def add_book(self):
        book = self.add_book_entry.get()
        self.books.append(book)
        messagebox.showinfo("Success", "Book added Completed ")
        self.add_book_entry.delete(0, tk.END)

    def remove_book(self):
        book = self.remove_book_entry.get()
        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Success", "Book removed Completed")
        else:
            messagebox.showerror("Error", "Book not found")
        self.remove_book_entry.delete(0, tk.END)

    def issue_book(self):
        book = self.issue_book_entry.get()
        if book in self.books:
            self.lend_list.append(book)
            self.books.remove(book)
            messagebox.showinfo("Success", "Book issued Completed")
        else:
            messagebox.showerror("Error", "Book not found")
        self.issue_book_entry.delete(0, tk.END)

    def view_books(self):
        message = "\n".join(self.books)
        messagebox.showinfo("Books", message)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()
