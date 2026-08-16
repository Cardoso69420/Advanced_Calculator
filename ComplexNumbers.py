import tkinter as tk
from tkinter import messagebox
import cmath
import math


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
    def _parse_complex(entry):
        """Helper: parse a complex number from an entry widget."""
        user_input = entry.get().replace('i', 'j').replace(' ', '')
        return complex(user_input)

    @staticmethod
    def _make_result_label(parent):
        """Helper: create the standard result label."""
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=20)
        result_label = tk.Label(
            result_frame,
            text="Result: ",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333",
            justify="left"
        )
        result_label.pack(anchor="center")
        return result_label

    @staticmethod
    def _make_calc_button(parent, command):
        """Helper: create the standard green Calculate button."""
        calc_btn = tk.Button(
            parent,
            text="Calculate",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=command,
            relief="raised",
            borderwidth=0
        )
        calc_btn.pack(pady=10)

    @staticmethod
    def complex_info_calculator(parent):
        """Complex number real and imaginary parts"""

        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                z = ComplexNumbersOperations._parse_complex(complex_entry)
                results_text = f"""
Real Part: {z.real:.4f}
Imaginary Part: {z.imag:.4f}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def modulus_calculator(parent):
        """Distance from origin (modulus)"""

        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                z = ComplexNumbersOperations._parse_complex(complex_entry)
                modulus = abs(z)
                result_label.config(text=f"|z| = {modulus:.4f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def argument_calculator(parent):
        """Angle of a complex number (argument)"""

        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                z = ComplexNumbersOperations._parse_complex(complex_entry)
                arg_rad = cmath.phase(z)
                arg_deg = math.degrees(arg_rad)
                results_text = f"""
arg(z) = {arg_rad:.4f} rad
arg(z) = {arg_deg:.4f}°
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def conjugate_calculator(parent):
        """Conjugate of a complex number"""

        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                z = ComplexNumbersOperations._parse_complex(complex_entry)
                z_conj = z.conjugate()
                results_text = f"""
z = {z}
z̄ = {z_conj}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def coordinates_calculator(parent):
        """Coordinates in the complex plane"""

        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                z = ComplexNumbersOperations._parse_complex(complex_entry)
                results_text = f"""
z = {z.real:.4f} + {z.imag:.4f}i
Point in plane: ({z.real:.4f}, {z.imag:.4f})
Quadrant: {ComplexNumbersOperations._get_quadrant(z)}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def _get_quadrant(z):
        """Helper: determine which quadrant a complex number is in."""
        if z.real > 0 and z.imag > 0:
            return "I"
        elif z.real < 0 and z.imag > 0:
            return "II"
        elif z.real < 0 and z.imag < 0:
            return "III"
        elif z.real > 0 and z.imag < 0:
            return "IV"
        elif z.real == 0 and z.imag != 0:
            return "Imaginary axis"
        elif z.real != 0 and z.imag == 0:
            return "Real axis"
        else:
            return "Origin"

    @staticmethod
    def advanced_calculation_calculator(parent):
        """Advanced operations: +, -, *, / on two complex numbers"""

        z1_frame = tk.Frame(parent, bg="#f0f0f0")
        z1_frame.pack(fill="x", pady=5)
        tk.Label(z1_frame, text="First complex (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        z1_entry = tk.Entry(z1_frame, width=15, font=("Arial", 11))
        z1_entry.pack(side="left", padx=5)
        z1_entry.insert(0, "3+4j")

        z2_frame = tk.Frame(parent, bg="#f0f0f0")
        z2_frame.pack(fill="x", pady=5)
        tk.Label(z2_frame, text="Second complex (c+di):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        z2_entry = tk.Entry(z2_frame, width=15, font=("Arial", 11))
        z2_entry.pack(side="left", padx=5)
        z2_entry.insert(0, "1-2j")

        op_frame = tk.Frame(parent, bg="#f0f0f0")
        op_frame.pack(fill="x", pady=5)
        tk.Label(op_frame, text="Operation:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        from tkinter import ttk
        op_var = tk.StringVar(value="+")
        op_menu = ttk.Combobox(op_frame, textvariable=op_var, values=["+", "-", "*", "/"], state="readonly", width=5)
        op_menu.pack(side="left", padx=5)

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                z1 = ComplexNumbersOperations._parse_complex(z1_entry)
                z2 = ComplexNumbersOperations._parse_complex(z2_entry)
                op = op_var.get()
                if op == "+":
                    result = z1 + z2
                elif op == "-":
                    result = z1 - z2
                elif op == "*":
                    result = z1 * z2
                elif op == "/":
                    if z2 == 0:
                        messagebox.showerror("Error", "Division by zero.")
                        return
                    result = z1 / z2
                results_text = f"""
z1 = {z1}
z2 = {z2}
z1 {op} z2 = {result}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def trigonometric_form_calculator(parent):
        """Convert to trigonometric form: r(cos θ + i sin θ)"""

        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Complex Number (a+bi):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        complex_entry = tk.Entry(info_frame, width=20, font=("Arial", 11))
        complex_entry.pack(side="left", padx=5)
        complex_entry.insert(0, "3+4j")

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                z = ComplexNumbersOperations._parse_complex(complex_entry)
                r = abs(z)
                theta = cmath.phase(z)
                results_text = f"""
z = {z}
|z| = r = {r:.4f}
arg(z) = θ = {theta:.4f} rad
Trigonometric form: {r:.4f}(cos({theta:.4f}) + i·sin({theta:.4f}))
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid complex number format. Use a+bi format.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def _euler_trig_helper(parent, operation_name, formula_text, compute_fn):
        """Shared UI for sine/cosine/tangent via Euler's formula."""
        info_frame = tk.Frame(parent, bg="#f0f0f0")
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Angle (radians):", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        angle_entry = tk.Entry(info_frame, width=15, font=("Arial", 11))
        angle_entry.pack(side="left", padx=5)
        angle_entry.insert(0, str(math.pi / 4))

        formula_label = tk.Label(
            parent,
            text=formula_text,
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666"
        )
        formula_label.pack(pady=5)

        result_label = ComplexNumbersOperations._make_result_label(parent)

        def calculate():
            try:
                theta = float(angle_entry.get())
                result = compute_fn(theta)
                real_check = compute_fn.__name__ + "_real" if hasattr(compute_fn, "__name__") else ""
                if "sin" in operation_name.lower():
                    check = math.sin(theta)
                elif "cos" in operation_name.lower():
                    check = math.cos(theta)
                else:
                    check = math.tan(theta)
                results_text = f"""
θ = {theta:.4f} rad
Euler result: {result}
Python result: {check:.4f}
                """
                result_label.config(text=results_text)
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Enter a numeric value for the angle.")

        ComplexNumbersOperations._make_calc_button(parent, calculate)

    @staticmethod
    def sine_euler_calculator(parent):
        """Sine using Euler's formula: sin(θ) = (e^(iθ) - e^(-iθ)) / (2i)"""
        ComplexNumbersOperations._euler_trig_helper(
            parent,
            "sine",
            "Euler's formula: sin(θ) = (e^(iθ) - e^(-iθ)) / (2i)",
            lambda theta: (cmath.exp(1j * theta) - cmath.exp(-1j * theta)) / (2j)
        )

    @staticmethod
    def cosine_euler_calculator(parent):
        """Cosine using Euler's formula: cos(θ) = (e^(iθ) + e^(-iθ)) / 2"""
        ComplexNumbersOperations._euler_trig_helper(
            parent,
            "cosine",
            "Euler's formula: cos(θ) = (e^(iθ) + e^(-iθ)) / 2",
            lambda theta: (cmath.exp(1j * theta) + cmath.exp(-1j * theta)) / 2
        )

    @staticmethod
    def tangent_euler_calculator(parent):
        """Tangent via Euler: tan(θ) = sin(θ) / cos(θ)"""
        ComplexNumbersOperations._euler_trig_helper(
            parent,
            "tangent",
            "tan(θ) = sin(θ) / cos(θ) via Euler",
            lambda theta: ((cmath.exp(1j * theta) - cmath.exp(-1j * theta)) / (2j)) /
                          ((cmath.exp(1j * theta) + cmath.exp(-1j * theta)) / 2)
        )

    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": ComplexNumbersOperations.complex_info_calculator,
            "2": ComplexNumbersOperations.modulus_calculator,
            "3": ComplexNumbersOperations.argument_calculator,
            "4": ComplexNumbersOperations.conjugate_calculator,
            "5": ComplexNumbersOperations.coordinates_calculator,
            "6": ComplexNumbersOperations.advanced_calculation_calculator,
            "7": ComplexNumbersOperations.trigonometric_form_calculator,
            "8": ComplexNumbersOperations.sine_euler_calculator,
            "9": ComplexNumbersOperations.cosine_euler_calculator,
            "10": ComplexNumbersOperations.tangent_euler_calculator,
        }
        return calculators.get(operation_id, None)
