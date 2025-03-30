import tkinter as tk
from tkinter import ttk

from menu import MainMenu
from rental import RentalTab
from reports import ReportsTab
from settings import SettingsTab
from theme import ThemeManager


class KartingRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Karting Rental")
        self.root.geometry("1000x700")

        self.theme_manager = ThemeManager()
        self.theme_manager.apply_theme('light', self.root)

        self.sample_data = [
            ("#A1GA68", "23/09/2022", "Jacob Marcus", "$100", "$000", "$000"),
            ("#A1GA68", "23/09/2022", "Jacob Marcus", "$100", "$000", "$000"),
            ("#A1GA68", "23/09/2022", "Jacob Marcus", "$100", "$000", "$000"),
            ("#A1GA68", "23/09/2022", "Jacob Marcus", "$100", "$000", "$000"),
            ("#A1GA68", "23/09/2022", "Jacob Marcus", "$100", "$000", "$000"),
            ("#A1GA68", "23/09/2022", "Jacob Marcus", "$100", "$000", "$000"),
            ("#A1GA68", "23/09/2022", "Jacob Marcus", "$100", "$000", "$000"),
            ("#B2GB79", "24/09/2022", "Sarah Johnson", "$120", "$050", "$070"),
            ("#C3HC80", "25/09/2022", "Michael Brown", "$150", "$150", "$000"),
        ]

        self.menu = MainMenu(self.root, self)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.rental_tab = RentalTab(self.notebook, self)
        self.reports_tab = ReportsTab(self.notebook, self)
        self.settings_tab = SettingsTab(self.notebook, self)

        self.rental_tab.populate_sample_data(self.sample_data)

    def new_rental(self):
        """Clear fields for a new rental"""
        self.rental_tab.clear_fields()
        self.notebook.select(0)  # select the Rentals tab


def main():
    root = tk.Tk()
    app = KartingRentalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
