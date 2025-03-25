import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class KartingRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Karting Rental")
        self.root.geometry("900x650")

        # Create menu bar
        self.create_menu()

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.create_rental_tab()
        self.create_reports_tab()
        self.create_settings_tab()

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
        self.populate_sample_data()

    def create_menu(self):
        """Create the main menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Rental", command=self.new_rental)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help", command=self.show_help)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def create_rental_tab(self):
        """Create the main rental tab"""
        rental_tab = ttk.Frame(self.notebook)
        self.notebook.add(rental_tab, text="Rentals")

        # Create frames for the rental tab
        self.create_frames(rental_tab)

        # create widgets
        self.create_search_section()
        self.create_rentals_section()
        self.create_customer_section()
        self.create_messages_section()

    def create_reports_tab(self):
        """Create the reports tab"""
        reports_tab = ttk.Frame(self.notebook)
        self.notebook.add(reports_tab, text="Reports")

        # Add content to reports tab
        label = ttk.Label(reports_tab, text="Reports will be displayed here")
        label.pack(pady=50)

        # Add some sample buttons
        daily_btn = ttk.Button(reports_tab, text="Daily Report", command=lambda: self.generate_report("daily"))
        daily_btn.pack(pady=5)

        weekly_btn = ttk.Button(reports_tab, text="Weekly Report", command=lambda: self.generate_report("weekly"))
        weekly_btn.pack(pady=5)

        monthly_btn = ttk.Button(reports_tab, text="Monthly Report", command=lambda: self.generate_report("monthly"))
        monthly_btn.pack(pady=5)

    def create_settings_tab(self):
        """Create the settings tab"""
        settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(settings_tab, text="Settings")

        # Add content to settings tab
        label = ttk.Label(settings_tab, text="Application Settings")
        label.pack(pady=20)

        # Theme selection
        theme_frame = ttk.LabelFrame(settings_tab, text="Theme", padding="10")
        theme_frame.pack(pady=10, padx=10, fill=tk.X)

        self.theme_var = tk.StringVar(value="light")
        ttk.Radiobutton(theme_frame, text="Light", variable=self.theme_var, value="light").pack(anchor=tk.W)
        ttk.Radiobutton(theme_frame, text="Dark", variable=self.theme_var, value="dark").pack(anchor=tk.W)
        ttk.Radiobutton(theme_frame, text="System", variable=self.theme_var, value="system").pack(anchor=tk.W)

        # Save settings button
        save_btn = ttk.Button(settings_tab, text="Save Settings", command=self.save_settings)
        save_btn.pack(pady=20)

    def create_frames(self, parent):
        """
        Creates all the frames displayed in the application
        """
        self.main_frame = ttk.Frame(parent, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # # search
        self.top_frame = ttk.Frame(self.main_frame)
        self.top_frame.pack(fill=tk.X, pady=5)

        # rentals and customer
        self.left_frame = ttk.Frame(self.main_frame, width=300)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # messages and settings
        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_search_section(self):
        """
        Creates section which searches through the rental records
        """
        search_frame = ttk.LabelFrame(self.top_frame, text="Global Search", padding="10")
        search_frame.pack(fill=tk.X, pady=5)

        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        search_btn = ttk.Button(search_frame, text="Search", command=self.perform_search)
        search_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(search_frame, text="Clear", command=self.clear_search)
        clear_btn.pack(side=tk.LEFT, padx=5)

        # binds enter key to perform the search alongside the search button
        search_entry.bind('<Return>', lambda event: self.perform_search())

    def create_rentals_section(self):
        """
        Creates a section with the rental information to submit
        """

        rentals_frame = ttk.LabelFrame(self.left_frame, text="Rentals", padding="10")
        rentals_frame.pack(fill=tk.X, pady=5)

        calendar_btn = ttk.Button(rentals_frame, text="Calendar", command=self.show_calendar)
        calendar_btn.pack(fill=tk.X, pady=2)

        ttk.Label(rentals_frame, text="Enter Consumer Name").pack(anchor=tk.W)
        self.consumer_name_entry = ttk.Entry(rentals_frame)
        self.consumer_name_entry.pack(fill=tk.X, pady=2)

        ttk.Label(rentals_frame, text="End Date").pack(anchor=tk.W)
        self.end_date_entry = ttk.Entry(rentals_frame)
        self.end_date_entry.pack(fill=tk.X, pady=2)

    def create_customer_section(self):
        """
        Creates a section with the customer information to submit
        """
        customer_frame = ttk.LabelFrame(self.left_frame, text="Customer", padding="10")
        customer_frame.pack(fill=tk.X, pady=5)

        ttk.Label(customer_frame, text="Kart ID").pack(anchor=tk.W)
        self.kart_id_entry = ttk.Entry(customer_frame)
        self.kart_id_entry.pack(fill=tk.X, pady=2)

        ttk.Label(customer_frame, text="Start Date").pack(anchor=tk.W)
        self.start_date_entry = ttk.Entry(customer_frame)
        self.start_date_entry.pack(fill=tk.X, pady=2)

        submit_btn = ttk.Button(customer_frame, text="Submit", command=self.process_rental)
        submit_btn.pack(fill=tk.X, pady=5)

    def create_messages_section(self):
        messages_frame = ttk.LabelFrame(self.right_frame, text="Rental Records", padding="10")
        messages_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        # payments button
        payments_btn = ttk.Button(messages_frame, text="Payments", command=self.show_payments)
        payments_btn.pack(fill=tk.X, pady=2)

        # treeview for rental records
        self.tree = ttk.Treeview(messages_frame, columns=("Kart ID", "Date", "Customer", "Payable", "Paid", "Due"), show="headings")

        # Configure columns
        self.tree.heading("Kart ID", text="Kart ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Customer", text="Customer")
        self.tree.heading("Payable", text="Payable Amount")
        self.tree.heading("Paid", text="Paid Amount")
        self.tree.heading("Due", text="Due")

        self.tree.column("Kart ID", width=80)
        self.tree.column("Date", width=100)
        self.tree.column("Customer", width=150)
        self.tree.column("Payable", width=100)
        self.tree.column("Paid", width=100)
        self.tree.column("Due", width=100)

        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)

        # Scrollbar
        scrollbar = ttk.Scrollbar(messages_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

    def populate_sample_data(self):
        """This method can be seen as a list refresh"""
        self._clear_view()

        # add sample data to the treeview
        for item in self.sample_data:
            self.tree.insert("", tk.END, values=item)

    def _clear_view(self):
        """
        Clears the current treeview
        """
        for item in self.tree.get_children():
            self.tree.delete(item)

    def perform_search(self):
        search_term = self.search_var.get().lower()
        if not search_term:
            self.populate_sample_data()
            return

        self._clear_view()
        # search across all columns
        for item in self.sample_data:
            # Check if search term exists in any of the columns
            if any(search_term in str(field).lower() for field in item):
                self.tree.insert("", tk.END, values=item)

    def clear_search(self):
        """
        Clears the search bar
        """
        self.search_var.set("")
        self.populate_sample_data()

    def show_calendar(self):
        messagebox.showinfo("Calendar", "Calendar view will be implemented here")

    def process_rental(self):
        kart_id = self.kart_id_entry.get()
        start_date = self.start_date_entry.get()
        consumer_name = self.consumer_name_entry.get()
        end_date = self.end_date_entry.get()

        if not all([kart_id, start_date, consumer_name, end_date]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # adds to the sample data list, and refreshes the list
        new_entry = (kart_id, start_date, consumer_name, "$100", "$000", "$000")
        self.sample_data.append(new_entry)
        self.populate_sample_data()

        messagebox.showinfo("Success", f"Rental processed for {consumer_name}\nKart: {kart_id}\nDates: {start_date} to {end_date}")

        # clear fields
        self.kart_id_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.consumer_name_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)

    def show_payments(self):
        messagebox.showinfo("Payments", "payment details would be displayed here")

    def show_help(self):
        help_text = """Karting Rental System Help
            1. Enter rental details in the Customer section
            2. View rental history in the Messages section
            3. Use Calendar to check availability
            4. Use Global Search to find specific rentals
               - Searches across all fields (Kart ID, Date, Customer, etc.)
               - Press Enter or click Search to perform search
               - Click Clear to show all records"""
        messagebox.showinfo("Help", help_text)

    def show_about(self):
        about_text = """Karting Rental System
Version 1.0
© 2023 Karting Rental Company"""
        messagebox.showinfo("About", about_text)

    def new_rental(self):
        """Clear fields for a new rental"""
        self.kart_id_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.consumer_name_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)
        self.notebook.select(0)  # Select the Rentals tab

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

    def generate_report(self, report_type):
        """Generate different types of reports"""
        messagebox.showinfo("Report Generated", f"{report_type.capitalize()} report has been generated")

    def save_settings(self):
        """Save application settings"""
        messagebox.showinfo("Settings Saved", f"Theme set to: {self.theme_var.get()}")

def main():
    root = tk.Tk()
    app = KartingRentalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
