from tkinter import ttk

class ThemeManager:
    def __init__(self):
        self.current_theme = 'light'
        self.theme_colors = {
            'light': {
                'bg': '#f0f0f0',
                'fg': '#333333',
                'header_bg': '#4a6baf',
                'header_fg': 'white',
                'entry_bg': 'white',
                'entry_fg': '#333333',
                'button_bg': '#4a6baf',
                'button_fg': 'white',
                'active_button_bg': '#3a5a9f',
                'tree_bg': 'white',
                'tree_fg': '#333333',
                'tree_header_bg': '#4a6baf',
                'tree_header_fg': 'white',
                'selected_bg': '#4a6baf',
                'selected_fg': 'white'
            },
            'dark': {
                'bg': '#2d2d2d',
                'fg': '#e0e0e0',
                'header_bg': '#1a3a6e',
                'header_fg': 'white',
                'entry_bg': '#3d3d3d',
                'entry_fg': 'white',
                'button_bg': '#1a3a6e',
                'button_fg': 'white',
                'active_button_bg': '#0a2a5e',
                'tree_bg': '#3d3d3d',
                'tree_fg': '#e0e0e0',
                'tree_header_bg': '#1a3a6e',
                'tree_header_fg': 'white',
                'selected_bg': '#1a3a6e',
                'selected_fg': 'white'
            }
        }
        self.style = ttk.Style()
        self.style.theme_use('clam')

    def apply_theme(self, theme_name, root=None):
        """Apply the selected theme to all widgets"""
        self.current_theme = theme_name
        colors = self.theme_colors[theme_name]

        # update style configurations
        self.style.configure('.', background=colors['bg'], foreground=colors['fg'])
        self.style.configure('TFrame', background=colors['bg'])
        self.style.configure('Header.TFrame', background=colors['header_bg'])

        self.style.configure('Header.TLabel',
                             background=colors['header_bg'],
                             foreground=colors['header_fg'],
                             font=('Helvetica', 12, 'bold'),
                             padding=5)

        self.style.configure('Section.TLabel',
                             background=colors['bg'],
                             foreground=colors['fg'],
                             font=('Helvetica', 10, 'bold'),
                             padding=5)

        self.style.configure('TButton',
                             font=('Helvetica', 9),
                             padding=5,
                             relief='flat')

        self.style.configure('Primary.TButton',
                             background=colors['button_bg'],
                             foreground=colors['button_fg'],
                             font=('Helvetica', 9, 'bold'),
                             padding=8)

        self.style.map('Primary.TButton',
                       background=[('active', colors['active_button_bg']),
                                   ('pressed', colors['active_button_bg'])])

        self.style.configure('TEntry',
                             fieldbackground=colors['entry_bg'],
                             foreground=colors['entry_fg'],
                             padding=5,
                             relief='solid',
                             bordercolor='#cccccc')

        self.style.configure('Treeview',
                             background=colors['tree_bg'],
                             foreground=colors['tree_fg'],
                             fieldbackground=colors['tree_bg'],
                             rowheight=25)

        self.style.configure('Treeview.Heading',
                             background=colors['tree_header_bg'],
                             foreground=colors['tree_header_fg'],
                             font=('Helvetica', 9, 'bold'),
                             padding=5)

        self.style.map('Treeview',
                       background=[('selected', colors['selected_bg'])],
                       foreground=[('selected', colors['selected_fg'])])

        if root:
            root.config(bg=colors['bg'])
