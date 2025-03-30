from tkinter import ttk, messagebox
import tkinter as tk

class RentalTab:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.create_tab()

    def create_tab(self):
        """Create the main rental tab"""
        self.tab = ttk.Frame(self.parent)
        self.parent.add(self.tab, text="Rentals")

        # create frames for the rental tab
        self.create_frames()

        # create widgets
        self.create_search_section()
        self.create_rentals_section()
        self.create_messages_section()

    def create_frames(self):
        """
        Creates all the frames displayed in the application
        """
        self.main_frame = ttk.Frame(self.tab, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # search frame
        self.top_frame = ttk.Frame(self.main_frame)
        self.top_frame.pack(fill=tk.X, pady=(0, 10))

        # left frame (rentals and customer)
        self.left_frame = ttk.Frame(self.main_frame, width=300)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        # right frame (messages)
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

        search_btn = ttk.Button(search_frame, text="Search", command=self.perform_search, style='Primary.TButton')
        search_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(search_frame, text="Clear", command=self.clear_search, style='TButton')
        clear_btn.pack(side=tk.LEFT, padx=5)

        # binds enter key to perform the search alongside the search button
        search_entry.bind('<Return>', lambda event: self.perform_search())

    def create_rentals_section(self):
        """
        Creates a section with the rental information to submit
        """
        rentals_frame = ttk.LabelFrame(self.left_frame, text="Rentals", padding="10")
        rentals_frame.pack(fill=tk.X, pady=5)

        ttk.Label(rentals_frame, text="Kart ID").pack(anchor=tk.W)
        self.kart_id_entry = ttk.Entry(rentals_frame)
        self.kart_id_entry.pack(fill=tk.X, pady=2)

        ttk.Label(rentals_frame, text="Enter Consumer Name").pack(anchor=tk.W)
        self.consumer_name_entry = ttk.Entry(rentals_frame)
        self.consumer_name_entry.pack(fill=tk.X, pady=2)

        ttk.Label(rentals_frame, text="Start Date").pack(anchor=tk.W)
        self.start_date_entry = ttk.Entry(rentals_frame)
        self.start_date_entry.pack(fill=tk.X, pady=2)

        ttk.Label(rentals_frame, text="End Date").pack(anchor=tk.W)
        self.end_date_entry = ttk.Entry(rentals_frame)
        self.end_date_entry.pack(fill=tk.X, pady=2)


        submit_btn = ttk.Button(rentals_frame, text="Submit", command=self.process_rental, style='Primary.TButton')
        submit_btn.pack(fill=tk.X, pady=5)


    def create_messages_section(self):
        messages_frame = ttk.LabelFrame(self.right_frame, text="Rental Records", padding="10")
        messages_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        # treeview for rental records
        self.tree = ttk.Treeview(messages_frame, columns=("Kart ID", "Date", "Customer", "Payable", "Paid", "Due"), show="headings")

        self.tree.heading("Kart ID", text="Kart ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Customer", text="Customer")
        self.tree.heading("Payable", text="Payable Amount")
        self.tree.heading("Paid", text="Paid Amount")
        self.tree.heading("Due", text="Due")

        self.tree.column("Kart ID", width=80, anchor=tk.CENTER)
        self.tree.column("Date", width=100, anchor=tk.CENTER)
        self.tree.column("Customer", width=150, anchor=tk.W)
        self.tree.column("Payable", width=100, anchor=tk.E)
        self.tree.column("Paid", width=100, anchor=tk.E)
        self.tree.column("Due", width=100, anchor=tk.E)

        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)

        # scrollbar
        scrollbar = ttk.Scrollbar(messages_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

    def populate_sample_data(self, sample_data):
        """This method can be seen as a list refresh"""
        self._clear_view()

        # add sample data to the treeview
        for item in sample_data:
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
            self.populate_sample_data(self.app.sample_data)
            return

        self._clear_view()
        # search across all columns
        for item in self.app.sample_data:
            # check if search term exists in any of the columns
            if any(search_term in str(field).lower() for field in item):
                self.tree.insert("", tk.END, values=item)

    def clear_search(self):
        """
        Clears the search bar
        """
        self.search_var.set("")
        self.populate_sample_data(self.app.sample_data)


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
        self.app.sample_data.append(new_entry)
        self.populate_sample_data(self.app.sample_data)

        messagebox.showinfo("Success", f"Rental processed for {consumer_name}\nKart: {kart_id}\nDates: {start_date} to {end_date}")

        # clear fields
        self.kart_id_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.consumer_name_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)

    def clear_fields(self):
        """Clear all input fields"""
        self.kart_id_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.consumer_name_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)
