import tkinter as tk
from tkinter import messagebox


class ComplexNumbersOperations:
    """Complex Numbers operations module"""
    
    OPERATIONS = {
        "1": "Complex Number Info",
        "2": "Distance (Modulus)",
        "3": "Angle (Argument)",
        "4": "Conjugate",
        "5": "Coordinates",
        "6": "Advanced Calculation",
        "7": "Trigonometric Form",
        "8": "Sine with Euler",
        "9": "Cosine with Euler",
        "10": "Tangent with Euler",
    }
    
    @staticmethod
    def complex_info_calculator(parent):
        """Complex number real and imaginary parts"""
        
        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)
        
        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")
        
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 11), bg="#f0f0f0", fg="#333")
        result_label.pack(anchor="center")
        
        def calculate():
            try:
                user_input = complex_entry.get().replace('i', 'j')
                z = complex(user_input)
                
                results_text = f"""
Real Part: {z.real:.4f}
Imaginary Part: {z.imag:.4f}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")
        
        calc_btn = tk.Button(
            parent,
            text="Calculate",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=calculate,
            relief="raised",
            borderwidth=0
        )
        calc_btn.pack(pady=10)
    
    @staticmethod
    def modulus_calculator(parent):
        """Distance from origin (modulus)"""
        
        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)
        
        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")
        
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        result_label.pack(anchor="center")
        
        def calculate():
            try:
                user_input = complex_entry.get().replace('i', 'j')
                z = complex(user_input)
                modulus = abs(z)
                
                result_label.config(text=f"|z| = {modulus:.4f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")
        
        calc_btn = tk.Button(
            parent,
            text="Calculate",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=calculate,
            relief="raised",
            borderwidth=0
        )
        calc_btn.pack(pady=10)
    
    @staticmethod
    def placeholder_calculator(parent, operation_name):
        """Placeholder for operations requiring sympy"""
        
        label = tk.Label(
            parent,
            text=f"{operation_name}\n\n(Requires sympy integration)",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#999"
        )
        label.pack(expand=True)
    
    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": ComplexNumbersOperations.complex_info_calculator,
            "2": ComplexNumbersOperations.modulus_calculator,
            "3": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Angle Calculation"),
            "4": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Conjugate"),
            "5": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Coordinates"),
            "6": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Advanced Calculation"),
            "7": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Trigonometric Form"),
            "8": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Sine with Euler"),
            "9": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Cosine with Euler"),
            "10": lambda p: ComplexNumbersOperations.placeholder_calculator(p, "Tangent with Euler"),
        }
        return calculators.get(operation_id, None)
