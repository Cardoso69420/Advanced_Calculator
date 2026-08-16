import tkinter as tk
from tkinter import messagebox

# Import all math modules
from Geometry import GeometryOperations
from ComplexNumbers import ComplexNumbersOperations
from Sequences import SequencesOperations
from Calculus import CalculusOperations
from Probability import ProbabilityOperations


class MathCalculator:
    """Main calculator that combines all math modules"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Math Calculator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Module definitions
        self.modules = {
            "1": ("Geometry and Trigonometry", GeometryOperations),
            "2": ("Probability and Combinatorics", ProbabilityOperations),
            "3": ("Sequences and Series", SequencesOperations),
            "4": ("Calculus", CalculusOperations),
            "5": ("Complex Numbers", ComplexNumbersOperations),
        }
        
        self.current_frame = None
        self.show_home_screen()
    
    def clear_frame(self):
        """Remove current frame"""
        if self.current_frame:
            self.current_frame.destroy()
    
    def show_home_screen(self):
        """Display main menu with module selection"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(fill="both", expand=True)
        
        # Title
        title = tk.Label(
            self.current_frame,
            text="Math Calculator",
            font=("Arial", 28, "bold"),
            bg="#f0f0f0"
        )
        title.pack(pady=30)
        
        # Subtitle
        subtitle = tk.Label(
            self.current_frame,
            text="Select a topic",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#666"
        )
        subtitle.pack(pady=10)
        
        # Buttons container
        buttons_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        buttons_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        for key, (name, module_class) in self.modules.items():
            btn = tk.Button(
                buttons_frame,
                text=name,
                font=("Arial", 14),
                bg="#4CAF50",
                fg="white",
                height=2,
                command=lambda k=key, n=name, m=module_class: self.show_module_menu(k, n, m),
                relief="raised",
                borderwidth=0
            )
            btn.pack(fill="both", expand=True, pady=8, padx=10)
        
        # Exit button
        exit_btn = tk.Button(
            buttons_frame,
            text="Exit",
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            height=1,
            command=self.root.quit,
            relief="raised",
            borderwidth=0
        )
        exit_btn.pack(fill="both", pady=8, padx=10)
    
    def show_module_menu(self, module_key, module_name, module_class):
        """Show operations menu for selected module"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = tk.Frame(self.current_frame, bg="#4CAF50")
        header_frame.pack(fill="x")
        
        back_btn = tk.Button(
            header_frame,
            text="← Back",
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white",
            command=self.show_home_screen,
            relief="flat",
            borderwidth=0
        )
        back_btn.pack(side="left", padx=10, pady=10)
        
        title = tk.Label(
            header_frame,
            text=module_name,
            font=("Arial", 16, "bold"),
            bg="#4CAF50",
            fg="white"
        )
        title.pack(side="left", padx=20, pady=10, expand=True)
        
        # Operations scroll area
        canvas = tk.Canvas(self.current_frame, bg="#f0f0f0", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.current_frame, orient="vertical", command=canvas.yview)
        operations_frame = tk.Frame(canvas, bg="#f0f0f0")

        operations_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=operations_frame, anchor="nw", width=560)
        canvas.configure(yscrollcommand=scrollbar.set)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        canvas.pack(side="left", fill="both", expand=True, padx=(20, 0), pady=20)
        scrollbar.pack(side="right", fill="y", pady=20, padx=(0, 20))

        # Create buttons for each operation
        for op_key, op_name in module_class.OPERATIONS.items():
            btn = tk.Button(
                operations_frame,
                text=op_name,
                font=("Arial", 12),
                bg="#FF9800",
                fg="white",
                height=2,
                command=lambda ok=op_key, on=op_name, mc=module_class: self.show_calculator(ok, on, mc),
                relief="raised",
                borderwidth=0
            )
            btn.pack(fill="x", pady=8)
    
    def show_calculator(self, operation_id, operation_name, module_class):
        """Show calculator for specific operation"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(fill="both", expand=True)
        
        # Header
        header_frame = tk.Frame(self.current_frame, bg="#FF9800")
        header_frame.pack(fill="x")
        
        back_btn = tk.Button(
            header_frame,
            text="← Back",
            font=("Arial", 10),
            bg="#FF9800",
            fg="white",
            command=lambda: self.show_module_menu(
                None,
                list(self.modules.values())[list(module_class.OPERATIONS.keys()).index("1")][0] if hasattr(module_class, "OPERATIONS") else "Module",
                module_class
            ),
            relief="flat",
            borderwidth=0
        )
        back_btn.pack(side="left", padx=10, pady=10)
        
        title = tk.Label(
            header_frame,
            text=operation_name,
            font=("Arial", 14, "bold"),
            bg="#FF9800",
            fg="white"
        )
        title.pack(side="left", padx=20, pady=10, expand=True)
        
        # Content frame (scrollable, for operations with many input fields)
        content_canvas = tk.Canvas(self.current_frame, bg="#f0f0f0", highlightthickness=0)
        content_scrollbar = tk.Scrollbar(self.current_frame, orient="vertical", command=content_canvas.yview)
        content_frame = tk.Frame(content_canvas, bg="#f0f0f0")

        content_frame.bind(
            "<Configure>",
            lambda e: content_canvas.configure(scrollregion=content_canvas.bbox("all"))
        )

        content_canvas.create_window((0, 0), window=content_frame, anchor="nw", width=560)
        content_canvas.configure(yscrollcommand=content_scrollbar.set)

        def _on_mousewheel(event):
            content_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        content_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        content_canvas.pack(side="left", fill="both", expand=True, padx=(20, 0), pady=20)
        content_scrollbar.pack(side="right", fill="y", pady=20, padx=(0, 20))
        
        # Get and display calculator
        calculator = module_class.get_calculator(operation_id)
        if calculator:
            calculator(content_frame)
        else:
            error_label = tk.Label(
                content_frame,
                text="Calculator not available",
                font=("Arial", 12),
                bg="#f0f0f0",
                fg="#f44336"
            )
            error_label.pack(expand=True)
    
    def find_module_name(self, module_class):
        """Find module name from module class"""
        for key, (name, mod_class) in self.modules.items():
            if mod_class == module_class:
                return name
        return "Module"


def main():
    """Launch the calculator"""
    root = tk.Tk()
    app = MathCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
