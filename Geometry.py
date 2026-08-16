import tkinter as tk
from tkinter import messagebox
import math


class GeometryOperations:
    """Geometry and Trigonometry operations module"""
    
    OPERATIONS = {
        "1": "Area",
        "2": "Pythagorean Theorem",
        "3": "SOHCAHTOA",
        "4": "Fundamental Trigonometric Formula",
        "5": "Calculate Sine (FFT)",
        "6": "Calculate Cosine (FFT)",
        "7": "Calculate Tangent",
    }
    
    @staticmethod
    def area_calculator(parent):
        """Area calculation tool"""
        from tkinter import ttk
        
        # Figure selection
        fig_frame = tk.Frame(parent, bg="#f0f0f0")
        fig_frame.pack(fill="x", pady=10)
        
        tk.Label(fig_frame, text="Figure:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        figure_var = tk.StringVar(value="square")
        figures = ["square", "rectangle", "triangle", "circle"]
        figure_menu = ttk.Combobox(fig_frame, textvariable=figure_var, values=figures, state="readonly", width=15)
        figure_menu.pack(side="left", padx=5)
        
        # Base input
        base_frame = tk.Frame(parent, bg="#f0f0f0")
        base_frame.pack(fill="x", pady=10)
        
        tk.Label(base_frame, text="Base (b):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        base_entry = tk.Entry(base_frame, width=15, font=("Arial", 11))
        base_entry.pack(side="left", padx=5)
        
        # Height input
        height_frame = tk.Frame(parent, bg="#f0f0f0")
        height_frame.pack(fill="x", pady=10)
        
        tk.Label(height_frame, text="Height (h):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        height_entry = tk.Entry(height_frame, width=15, font=("Arial", 11))
        height_entry.pack(side="left", padx=5)
        
        # Result display
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        result_label.pack(anchor="center")
        
        def calculate():
            try:
                figure = figure_var.get()
                base = float(base_entry.get())
                height = float(height_entry.get())
                
                if figure == "square":
                    area = base ** 2
                elif figure == "rectangle":
                    area = base * height
                elif figure == "triangle":
                    area = (base * height) / 2
                elif figure == "circle":
                    area = math.pi * (base ** 2)
                
                result_label.config(text=f"Result: {area:.4f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter numeric values.")
        
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
    def pythagorean_calculator(parent):
        """Pythagorean theorem calculator"""
        
        # Input A
        a_frame = tk.Frame(parent, bg="#f0f0f0")
        a_frame.pack(fill="x", pady=10)
        
        tk.Label(a_frame, text="Cathetus A:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        a_entry = tk.Entry(a_frame, width=15, font=("Arial", 11))
        a_entry.pack(side="left", padx=5)
        
        # Input B
        b_frame = tk.Frame(parent, bg="#f0f0f0")
        b_frame.pack(fill="x", pady=10)
        
        tk.Label(b_frame, text="Cathetus B:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        b_entry = tk.Entry(b_frame, width=15, font=("Arial", 11))
        b_entry.pack(side="left", padx=5)
        
        # Result display
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(result_frame, text="Hypotenuse: ", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        result_label.pack(anchor="center")
        
        def calculate():
            try:
                a = float(a_entry.get())
                b = float(b_entry.get())
                c = math.sqrt(a**2 + b**2)
                result_label.config(text=f"Hypotenuse: {c:.4f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter numeric values.")
        
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
    def sohcahtoa_calculator(parent):
        """SOHCAHTOA trigonometric ratios calculator"""
        
        # Adjacent input
        adj_frame = tk.Frame(parent, bg="#f0f0f0")
        adj_frame.pack(fill="x", pady=10)
        
        tk.Label(adj_frame, text="Adjacent Side:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        adj_entry = tk.Entry(adj_frame, width=15, font=("Arial", 11))
        adj_entry.pack(side="left", padx=5)
        
        # Opposite input
        opp_frame = tk.Frame(parent, bg="#f0f0f0")
        opp_frame.pack(fill="x", pady=10)
        
        tk.Label(opp_frame, text="Opposite Side:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        opp_entry = tk.Entry(opp_frame, width=15, font=("Arial", 11))
        opp_entry.pack(side="left", padx=5)
        
        # Hypotenuse input
        hyp_frame = tk.Frame(parent, bg="#f0f0f0")
        hyp_frame.pack(fill="x", pady=10)
        
        tk.Label(hyp_frame, text="Hypotenuse:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        hyp_entry = tk.Entry(hyp_frame, width=15, font=("Arial", 11))
        hyp_entry.pack(side="left", padx=5)
        
        # Results display
        results_frame = tk.Frame(parent, bg="#f0f0f0")
        results_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(
            results_frame,
            text="Results will appear here",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333",
            justify="left"
        )
        result_label.pack(anchor="nw", fill="both", expand=True)
        
        def calculate():
            try:
                adjacent = float(adj_entry.get())
                opposite = float(opp_entry.get())
                hypotenuse = float(hyp_entry.get())
                
                sine = opposite / hypotenuse
                cosine = adjacent / hypotenuse
                tangent = opposite / adjacent
                
                results_text = f"""
Sin(θ) = {sine:.4f}
Cos(θ) = {cosine:.4f}
Tan(θ) = {tangent:.4f}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter numeric values.")
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero. Check your values.")
        
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
    def fft_calculator(parent):
        """FFT: sin²(x) + cos²(x) = 1"""
        
        info_label = tk.Label(
            parent,
            text="Fundamental Trigonometric Formula\nsin²(θ) + cos²(θ) = 1",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        info_label.pack(pady=20)
        
        # Angle input
        angle_frame = tk.Frame(parent, bg="#f0f0f0")
        angle_frame.pack(fill="x", pady=10)
        
        tk.Label(angle_frame, text="Angle (radians):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        angle_entry = tk.Entry(angle_frame, width=15, font=("Arial", 11))
        angle_entry.pack(side="left", padx=5)
        angle_entry.insert(0, "0.5")
        
        # Results display
        results_frame = tk.Frame(parent, bg="#f0f0f0")
        results_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(
            results_frame,
            text="Enter angle and click Calculate",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333",
            justify="left"
        )
        result_label.pack(anchor="nw", fill="both", expand=True)
        
        def calculate():
            try:
                theta = float(angle_entry.get())
                
                sin_val = math.sin(theta)
                cos_val = math.cos(theta)
                result = sin_val**2 + cos_val**2
                
                results_text = f"""
θ = {theta:.4f} rad

sin(θ) = {sin_val:.4f}
cos(θ) = {cos_val:.4f}

sin²(θ) = {sin_val**2:.4f}
cos²(θ) = {cos_val**2:.4f}

sin²(θ) + cos²(θ) = {result:.4f}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter numeric value for angle.")
        
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
    def sine_fft_calculator(parent):
        """Calculate Sine using FFT"""
        
        info_label = tk.Label(
            parent,
            text="Calculate Sine from FFT\nsin(θ) = √(1 - cos²(θ))",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        info_label.pack(pady=20)
        
        # Cosine input
        cos_frame = tk.Frame(parent, bg="#f0f0f0")
        cos_frame.pack(fill="x", pady=10)
        
        tk.Label(cos_frame, text="Cos(θ):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        cos_entry = tk.Entry(cos_frame, width=15, font=("Arial", 11))
        cos_entry.pack(side="left", padx=5)
        cos_entry.insert(0, "0.5")
        
        # Result display
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        result_label.pack(anchor="center")
        
        def calculate():
            try:
                cos_val = float(cos_entry.get())
                
                if cos_val**2 > 1:
                    messagebox.showerror("Error", "cos²(θ) cannot be greater than 1.")
                    return
                
                sin_val = math.sqrt(1 - cos_val**2)
                result_label.config(text=f"Sin(θ) = {sin_val:.4f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter numeric value.")
        
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
    def cosine_fft_calculator(parent):
        """Calculate Cosine using FFT"""
        
        info_label = tk.Label(
            parent,
            text="Calculate Cosine from FFT\ncos(θ) = √(1 - sin²(θ))",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        info_label.pack(pady=20)
        
        # Sine input
        sin_frame = tk.Frame(parent, bg="#f0f0f0")
        sin_frame.pack(fill="x", pady=10)
        
        tk.Label(sin_frame, text="Sin(θ):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        sin_entry = tk.Entry(sin_frame, width=15, font=("Arial", 11))
        sin_entry.pack(side="left", padx=5)
        sin_entry.insert(0, "0.5")
        
        # Result display
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        result_label.pack(anchor="center")
        
        def calculate():
            try:
                sin_val = float(sin_entry.get())
                
                if sin_val**2 > 1:
                    messagebox.showerror("Error", "sin²(θ) cannot be greater than 1.")
                    return
                
                cos_val = math.sqrt(1 - sin_val**2)
                result_label.config(text=f"Cos(θ) = {cos_val:.4f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter numeric value.")
        
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
    def tangent_calculator(parent):
        """Calculate Tangent"""
        
        # Angle input
        angle_frame = tk.Frame(parent, bg="#f0f0f0")
        angle_frame.pack(fill="x", pady=10)
        
        tk.Label(angle_frame, text="Angle (radians):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        angle_entry = tk.Entry(angle_frame, width=15, font=("Arial", 11))
        angle_entry.pack(side="left", padx=5)
        angle_entry.insert(0, "0.5")
        
        # Result display
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        
        result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 12), bg="#f0f0f0", fg="#333")
        result_label.pack(anchor="center")
        
        def calculate():
            try:
                theta = float(angle_entry.get())
                
                cos_val = math.cos(theta)
                if abs(cos_val) < 1e-10:
                    messagebox.showerror("Error", "cos(θ) is zero, tangent is undefined.")
                    return
                
                tan_val = math.tan(theta)
                result_label.config(text=f"Tan(θ) = {tan_val:.4f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter numeric value for angle.")
        
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
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": GeometryOperations.area_calculator,
            "2": GeometryOperations.pythagorean_calculator,
            "3": GeometryOperations.sohcahtoa_calculator,
            "4": GeometryOperations.fft_calculator,
            "5": GeometryOperations.sine_fft_calculator,
            "6": GeometryOperations.cosine_fft_calculator,
            "7": GeometryOperations.tangent_calculator,
        }
        return calculators.get(operation_id, None)
