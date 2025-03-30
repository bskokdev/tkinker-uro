import tkinter as tk
from tkinter import messagebox


class MainMenu:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.create_menu()

    def create_menu(self):
        """Create the main menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Rental", command=self.app.new_rental)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Light Theme", command=lambda: self.app.theme_manager.apply_theme('light', self.root))
        view_menu.add_command(label="Dark Theme", command=lambda: self.app.theme_manager.apply_theme('dark', self.root))
        menubar.add_cascade(label="View", menu=view_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def open_file(self):
        """Placeholder for open file functionality"""
        messagebox.showinfo("Open", "This would open a file dialog in a real implementation")

    def cut(self):
        """Placeholder for cut functionality"""
        messagebox.showinfo("Cut", "This would cut text in a real implementation")

    def copy(self):
        """Placeholder for copy functionality"""
        messagebox.showinfo("Copy", "This would copy text in a real implementation")

    def paste(self):
        """Placeholder for paste functionality"""
        messagebox.showinfo("Paste", "This would paste text in a real implementation")

    def show_about(self):
        about_text = """Karting Rental System
Version 1.0
© 2023 Karting Rental Company"""
        messagebox.showinfo("About", about_text)
