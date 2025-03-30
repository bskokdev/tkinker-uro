from tkinter import ttk, messagebox
import tkinter as tk

class SettingsTab:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.create_tab()

    def create_tab(self):
        """Create the settings tab"""
        self.tab = ttk.Frame(self.parent)
        self.parent.add(self.tab, text="Settings")

        # Add content to settings tab
        label = ttk.Label(self.tab, text="Application Settings", font=('Helvetica', 12))
        label.pack(pady=20)

        # Theme selection
        theme_frame = ttk.LabelFrame(self.tab, text="Theme", padding="10")
        theme_frame.pack(pady=10, padx=50, fill=tk.X)

        self.theme_var = tk.StringVar(value=self.app.theme_manager.current_theme)
        ttk.Radiobutton(theme_frame, text="Light", variable=self.theme_var, value="light",
                        command=lambda: self.app.theme_manager.apply_theme('light', self.app.root)).pack(anchor=tk.W, pady=2)
        ttk.Radiobutton(theme_frame, text="Dark", variable=self.theme_var, value="dark",
                        command=lambda: self.app.theme_manager.apply_theme('dark', self.app.root)).pack(anchor=tk.W, pady=2)

    def save_settings(self):
        """Save application settings"""
        self.app.theme_manager.apply_theme(self.theme_var.get(), self.app.root)
        messagebox.showinfo("Settings Saved", f"Theme set to: {self.theme_var.get()}")
