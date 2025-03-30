from tkinter import ttk, messagebox
import tkinter as tk

class ReportsTab:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.create_tab()

    def create_tab(self):
        """Create the reports tab"""
        self.tab = ttk.Frame(self.parent)
        self.parent.add(self.tab, text="Reports")

        # Add content to reports tab
        label = ttk.Label(self.tab, text="Reports will be displayed here", font=('Helvetica', 12))
        label.pack(pady=50)

        # Add some sample buttons
        daily_btn = ttk.Button(self.tab, text="Daily Report", command=lambda: self.generate_report("daily"), style='Primary.TButton')
        daily_btn.pack(pady=5, padx=50, fill=tk.X)

        weekly_btn = ttk.Button(self.tab, text="Weekly Report", command=lambda: self.generate_report("weekly"), style='Primary.TButton')
        weekly_btn.pack(pady=5, padx=50, fill=tk.X)

        monthly_btn = ttk.Button(self.tab, text="Monthly Report", command=lambda: self.generate_report("monthly"), style='Primary.TButton')
        monthly_btn.pack(pady=5, padx=50, fill=tk.X)

    def generate_report(self, report_type):
        """Generate different types of reports"""
        messagebox.showinfo("Report Generated", f"{report_type.capitalize()} report has been generated")
