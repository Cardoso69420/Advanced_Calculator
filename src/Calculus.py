import tkinter as tk
from tkinter import messagebox
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor


class CalculusOperations:
    """Calculus operations module"""

    OPERATIONS = {
        "1": "Image f(x)",
        "2": "Function Zeros",
        "3": "Limit",
        "4": "Side Limits",
        "5": "Continuity",
        "6": "Tangent Line (via Limit)",
        "7": "Derivative",
        "8": "Tangent Line (via Derivative)",
        "9": "Extreme and Inflection Points",
        "10": "Primitive",
        "11": "Calculate Constant C",
        "12": "Defined Integral",
        "13": "Taylor Series",
        "14": "Taylor Polynomial",
    }

    # ---------- UI helpers ----------

    @staticmethod
    def _make_func_entry(parent, default="x**2"):
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text="f(x) =", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        entry = tk.Entry(frame, width=25, font=("Arial", 11))
        entry.pack(side="left", padx=5)
        entry.insert(0, default)
        return frame, entry

    @staticmethod
    def _make_value_entry(parent, label, default, width=15):
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text=label, font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        entry = tk.Entry(frame, width=width, font=("Arial", 11))
        entry.pack(side="left", padx=5)
        entry.insert(0, default)
        return frame, entry

    @staticmethod
    def _make_result_label(parent):
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=10)
        result_label = tk.Label(
            result_frame,
            text="Result: ",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333",
            justify="left",
            wraplength=480,
        )
        result_label.pack(anchor="nw", fill="both", expand=True)
        return result_label

    @staticmethod
    def _make_calc_button(parent, command):
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

    # ---------- parsing helpers ----------

    @staticmethod
    def _parse_func(text):
        x = sp.symbols('x')
        transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
        expr = parse_expr(text, transformations=transformations, local_dict={'x': x})
        if x not in expr.free_symbols and not expr.is_number:
            raise ValueError("the function must be in terms of x.")
        return x, expr

    @staticmethod
    def _to_num(text):
        return sp.sympify(text)

    # ---------- operations ----------

    @staticmethod
    def image_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**2 + 1")
        _, p_entry = CalculusOperations._make_value_entry(parent, "x =", "2")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                point = CalculusOperations._to_num(p_entry.get())
                result_label.config(text=f"f({point}) = {f.subs(x, point)}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def zero_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**2 - 4")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                result_label.config(text=f"Zeros: {sp.solve(f, x)}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def limit_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "(x**2 - 1)/(x - 1)")
        _, p_entry = CalculusOperations._make_value_entry(parent, "x →", "1")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                point = CalculusOperations._to_num(p_entry.get())
                result_label.config(text=f"lim (x→{point}) f(x) = {sp.limit(f, x, point)}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def limits_sides_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "1/x")
        _, p_entry = CalculusOperations._make_value_entry(parent, "x →", "0")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                point = CalculusOperations._to_num(p_entry.get())
                lim_left = sp.limit(f, x, point, dir='-')
                lim_right = sp.limit(f, x, point, dir='+')
                text = f"lim (x→{point}⁻) f(x) = {lim_left}\nlim (x→{point}⁺) f(x) = {lim_right}"
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def continuity_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**2")
        _, p_entry = CalculusOperations._make_value_entry(parent, "x =", "1")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                point = CalculusOperations._to_num(p_entry.get())
                lim_left = sp.limit(f, x, point, dir='-')
                lim_right = sp.limit(f, x, point, dir='+')
                try:
                    value = f.subs(x, point)
                except Exception:
                    value = None
                continuous = lim_left == lim_right == value
                text = (
                    f"lim (x→{point}⁻) f(x) = {lim_left}\n"
                    f"lim (x→{point}⁺) f(x) = {lim_right}\n"
                    f"f({point}) = {value}\n"
                    f"{'✓ Function is CONTINUOUS' if continuous else '✗ Function is NOT continuous'} at x = {point}"
                )
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def lim_tangent_line_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**2")
        _, p_entry = CalculusOperations._make_value_entry(parent, "Tangency point (x) =", "1")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                point = CalculusOperations._to_num(p_entry.get())
                f_point = f.subs(x, point)
                m = sp.limit((f - f_point) / (x - point), x, point)
                tangent = sp.simplify(m * (x - point) + f_point)
                result_label.config(text=f"declive m = {m}\nReta tangente: y = {tangent}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def derivative_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**3 - 2*x")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                result_label.config(text=f"f'(x) = {sp.diff(f, x)}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def derivative_tangent_line_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**2")
        _, p_entry = CalculusOperations._make_value_entry(parent, "Tangency point (x) =", "1")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                point = CalculusOperations._to_num(p_entry.get())
                f_point = f.subs(x, point)
                df = sp.diff(f, x)
                m = df.subs(x, point)
                tangent = sp.simplify(m * (x - point) + f_point)
                result_label.config(text=f"f'(x) = {df}\ndeclive m = {m}\nReta tangente: y = {tangent}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def extreme_inflection_points_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**3 - 3*x")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                df1 = sp.diff(f, x)
                zeros = sp.solve(df1, x)
                df2 = sp.diff(df1, x)

                lines = [f"Critical points: {zeros}", ""]
                for point in zeros:
                    second = df2.subs(x, point)
                    y = f.subs(x, point)
                    if second > 0:
                        kind = "MINIMUM"
                    elif second < 0:
                        kind = "MAXIMUM"
                    else:
                        kind = "inflection point"
                    lines.append(f"({point}, {y}) → {kind}")

                result_label.config(text="\n".join(lines))
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def primitive_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "2*x")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                C = sp.symbols('C')
                result_label.config(text=f"F(x) = {sp.integrate(f, x)} + C")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def calculate_c_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "2*x")
        _, p_entry = CalculusOperations._make_value_entry(parent, "Ponto (x) =", "1")
        _, v_entry = CalculusOperations._make_value_entry(parent, "Valor de F(x) nesse ponto =", "5")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                point = CalculusOperations._to_num(p_entry.get())
                value = CalculusOperations._to_num(v_entry.get())
                C = sp.symbols('C')
                integral = sp.integrate(f, x) + C
                c_value = sp.solve(integral.subs(x, point) - value, C)
                if not c_value:
                    raise ValueError("could not calculate C.")
                result_label.config(text=f"C = {c_value[0]}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def integral_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "x**2")
        _, a_entry = CalculusOperations._make_value_entry(parent, "Limite inferior (a) =", "0")
        _, b_entry = CalculusOperations._make_value_entry(parent, "Limite superior (b) =", "1")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                a = CalculusOperations._to_num(a_entry.get())
                b = CalculusOperations._to_num(b_entry.get())
                result_label.config(text=f"∫ f(x) dx [{a}, {b}] = {sp.integrate(f, (x, a, b))}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def taylor_series_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "exp(x)")
        _, p_entry = CalculusOperations._make_value_entry(parent, "Expansion point (x0) =", "0")
        _, n_entry = CalculusOperations._make_value_entry(parent, "Ordem (n) =", "5")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                x0 = CalculusOperations._to_num(p_entry.get())
                n = int(CalculusOperations._to_num(n_entry.get()))
                result_label.config(text=f"Taylor Series: {f.series(x, x0, n)}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def taylor_series_polynomial_calculator(parent):
        _, f_entry = CalculusOperations._make_func_entry(parent, "exp(x)")
        _, p_entry = CalculusOperations._make_value_entry(parent, "Expansion point (x0) =", "0")
        _, n_entry = CalculusOperations._make_value_entry(parent, "Ordem (n) =", "5")
        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, f = CalculusOperations._parse_func(f_entry.get())
                x0 = CalculusOperations._to_num(p_entry.get())
                n = int(CalculusOperations._to_num(n_entry.get()))
                poly = f.series(x, x0, n).removeO()
                result_label.config(text=f"Taylor Polynomial: {poly}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": CalculusOperations.image_calculator,
            "2": CalculusOperations.zero_calculator,
            "3": CalculusOperations.limit_calculator,
            "4": CalculusOperations.limits_sides_calculator,
            "5": CalculusOperations.continuity_calculator,
            "6": CalculusOperations.lim_tangent_line_calculator,
            "7": CalculusOperations.derivative_calculator,
            "8": CalculusOperations.derivative_tangent_line_calculator,
            "9": CalculusOperations.extreme_inflection_points_calculator,
            "10": CalculusOperations.primitive_calculator,
            "11": CalculusOperations.calculate_c_calculator,
            "12": CalculusOperations.integral_calculator,
            "13": CalculusOperations.taylor_series_calculator,
            "14": CalculusOperations.taylor_series_polynomial_calculator,
        }
        return calculators.get(operation_id, None)
