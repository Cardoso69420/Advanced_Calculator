import tkinter as tk
from tkinter import messagebox
import sympy as sp


class CalculusOperations:
    """Calculus operations module"""

    OPERATIONS = {
        "1": "Function Image",
        "2": "Zeros",
        "3": "Limit",
        "4": "Lateral Limits",
        "5": "Continuity",
        "6": "Tangent Line (Limit)",
        "7": "Derivative",
        "8": "Tangent Line (Derivative)",
        "9": "Extremes and Inflection Points",
        "10": "Primitive",
        "11": "Calculate C",
        "12": "Integral",
        "13": "Taylor Series",
        "14": "Taylor Polynomial",
    }

    @staticmethod
    def _make_function_entry(parent, default="x"):
        """Helper: build a labelled function input field, return (frame, entry)."""
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text="f(x) =", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        entry = tk.Entry(frame, width=25, font=("Arial", 11))
        entry.pack(side="left", padx=5)
        entry.insert(0, default)
        return frame, entry

    @staticmethod
    def _make_value_entry(parent, label, default):
        """Helper: build a labelled numeric input field, return (frame, entry)."""
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text=label, font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        entry = tk.Entry(frame, width=15, font=("Arial", 11))
        entry.pack(side="left", padx=5)
        entry.insert(0, default)
        return frame, entry

    @staticmethod
    def _make_result_label(parent):
        """Helper: create the standard multi-line result label."""
        result_frame = tk.Frame(parent, bg="#f0f0f0")
        result_frame.pack(fill="both", expand=True, pady=10)
        result_label = tk.Label(
            result_frame,
            text="Result: ",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333",
            justify="left"
        )
        result_label.pack(anchor="nw", fill="both", expand=True)
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
    def _parse_function(entry):
        """Helper: parse a sympy expression using x as the default variable."""
        x = sp.Symbol('x')
        expr_text = entry.get()
        return x, sp.sympify(expr_text, locals={'x': x})

    @staticmethod
    def function_image_calculator(parent):
        """Evaluate f(a) for a given value a."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**2 + 2*x + 1")
        _, a_entry = CalculusOperations._make_value_entry(parent, "x =", "2")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                value = expr.subs(x, a)
                result_label.config(text=f"f({a}) = {sp.simplify(value)}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def zeros_calculator(parent):
        """Solve f(x) = 0."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**2 - 4")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                solutions = sp.solve(expr, x)
                if not solutions:
                    text = "No real solutions found."
                else:
                    lines = [f"x = {sp.nsimplify(s)}" for s in solutions]
                    text = "Zeros of f(x):\n" + "\n".join(lines)
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def limit_calculator(parent):
        """Compute lim x->a f(x)."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "(x**2 - 1)/(x - 1)")
        _, a_entry = CalculusOperations._make_value_entry(parent, "x →", "1")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                value = sp.limit(expr, x, a)
                result_label.config(text=f"lim (x→{a}) f(x) = {value}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def lateral_limits_calculator(parent):
        """Compute left and right limits at a."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "1/(x-2)")
        _, a_entry = CalculusOperations._make_value_entry(parent, "x →", "2")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                left = sp.limit(expr, x, a, '-')
                right = sp.limit(expr, x, a, '+')
                text = f"""
Left limit  (x→{a}⁻): {left}
Right limit (x→{a}⁺): {right}
                """
                if left == right:
                    text += f"\nLimit exists: lim = {left}"
                else:
                    text += "\nLimit does NOT exist (left ≠ right)."
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def continuity_calculator(parent):
        """Check continuity of f at a point a."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "(x**2 - 1)/(x - 1)")
        _, a_entry = CalculusOperations._make_value_entry(parent, "x =", "1")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                f_at_a = expr.subs(x, a)
                lim = sp.limit(expr, x, a)
                if lim == f_at_a and f_at_a != sp.zoo and f_at_a != sp.oo and f_at_a != -sp.oo:
                    text = f"f({a}) = {f_at_a}\nlim x→{a} f(x) = {lim}\n✓ f is continuous at x = {a}"
                else:
                    text = f"f({a}) = {f_at_a}\nlim x→{a} f(x) = {lim}\n✗ f is NOT continuous at x = {a}"
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def tangent_line_limit_calculator(parent):
        """Tangent line using the limit definition of the derivative."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**2")
        _, a_entry = CalculusOperations._make_value_entry(parent, "x =", "3")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                h = sp.Symbol('h')
                quotient = (expr.subs(x, a + h) - expr.subs(x, a)) / h
                slope = sp.limit(quotient, h, 0)
                intercept = expr.subs(x, a) - slope * a
                text = f"""
f(x) = {expr}
At point: a = {a}
Slope m = lim h→0 [f(a+h)-f(a)]/h = {slope}
y - f(a) = m(x - a)
Tangent line: y = {slope}*x + ({intercept})
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def derivative_calculator(parent):
        """Compute f'(x)."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**3 + 2*x")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                d1 = sp.diff(expr, x)
                d2 = sp.diff(expr, x, 2)
                text = f"""
f(x)  = {expr}
f'(x) = {sp.simplify(d1)}
f''(x)= {sp.simplify(d2)}
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def tangent_line_derivative_calculator(parent):
        """Tangent line at point a using the derivative."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**2")
        _, a_entry = CalculusOperations._make_value_entry(parent, "x =", "3")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                slope = sp.diff(expr, x).subs(x, a)
                intercept = expr.subs(x, a) - slope * a
                text = f"""
f(x)  = {expr}
f'(x) = {sp.diff(expr, x)}
At x = {a}:
  f({a}) = {expr.subs(x, a)}
  f'({a}) = {slope}
Tangent line: y = {slope}*x + ({intercept})
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def extremes_inflection_calculator(parent):
        """Find critical (extreme) points and inflection points."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**3 - 3*x**2")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                d1 = sp.diff(expr, x)
                d2 = sp.diff(expr, x, 2)
                critical = sp.solve(d1, x)
                inflections = sp.solve(d2, x)

                def classify(c):
                    val_d2 = d2.subs(x, c)
                    if val_d2 > 0:
                        return f"local min (f''({c}) > 0)"
                    if val_d2 < 0:
                        return f"local max (f''({c}) < 0)"
                    return "inconclusive (f'' = 0)"

                crit_lines = [f"x = {c}, f({c}) = {expr.subs(x, c)} → {classify(c)}"
                              for c in critical]
                infl_lines = [f"x = {i}, f({i}) = {expr.subs(x, i)}" for i in inflections]

                text = f"""
f(x)  = {expr}
f'(x) = {d1}
f''(x)= {d2}

Critical points (f'(x) = 0):
{chr(10).join(crit_lines) if crit_lines else 'None'}

Inflection points (f''(x) = 0):
{chr(10).join(infl_lines) if inflections else 'None'}
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def primitive_calculator(parent):
        """Compute the indefinite integral (primitive/antiderivative)."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "2*x + 3")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                primitive = sp.integrate(expr, x)
                text = f"""
f(x)     = {expr}
∫f(x)dx  = {primitive} + C
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def calculate_c_calculator(parent):
        """Given F(a) = b, find the constant C in F(x) + C."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**2")
        _, a_entry = CalculusOperations._make_value_entry(parent, "x =", "2")
        _, b_entry = CalculusOperations._make_value_entry(parent, "F(a) =", "7")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                b = sp.sympify(b_entry.get())
                F = sp.integrate(expr, x)
                C = b - F.subs(x, a)
                text = f"""
f(x)       = {expr}
∫f(x)dx    = {F} + C
At x = {a}: F({a}) + C = {b}
C = {b} - {F.subs(x, a)} = {sp.simplify(C)}
Final primitive: {F} + ({C}) = {F + C}
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def integral_calculator(parent):
        """Compute the definite integral ∫[a, b] f(x) dx."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "x**2")
        _, a_entry = CalculusOperations._make_value_entry(parent, "Lower limit a:", "0")
        _, b_entry = CalculusOperations._make_value_entry(parent, "Upper limit b:", "1")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                b = sp.sympify(b_entry.get())
                value = sp.integrate(expr, (x, a, b))
                text = f"""
f(x) = {expr}
∫[{a}, {b}] {expr} dx = {sp.simplify(value)}
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def taylor_series_calculator(parent):
        """Compute the Taylor series of f around point a up to order n."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "exp(x)")
        _, a_entry = CalculusOperations._make_value_entry(parent, "Around x =", "0")
        _, n_entry = CalculusOperations._make_value_entry(parent, "Order n:", "6")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                n = int(sp.sympify(n_entry.get()))
                series = sp.series(expr, x, a, n + 1).removeO()
                text = f"""
f(x) = {expr}
Taylor series around x = {a}, order {n}:

{series}
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def taylor_polynomial_calculator(parent):
        """Compute the Taylor polynomial of f of degree n at point a."""

        _, func_entry = CalculusOperations._make_function_entry(parent, "cos(x)")
        _, a_entry = CalculusOperations._make_value_entry(parent, "Around x =", "0")
        _, n_entry = CalculusOperations._make_value_entry(parent, "Degree n:", "4")

        result_label = CalculusOperations._make_result_label(parent)

        def calculate():
            try:
                x, expr = CalculusOperations._parse_function(func_entry)
                a = sp.sympify(a_entry.get())
                n = int(sp.sympify(n_entry.get()))
                poly = sum(
                    sp.diff(expr, x, k).subs(x, a) / sp.factorial(k) * (x - a) ** k
                    for k in range(n + 1)
                )
                text = f"""
f(x) = {expr}
Taylor polynomial of degree {n} around x = {a}:

P_{n}(x) = {sp.expand(poly)}
                """
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        CalculusOperations._make_calc_button(parent, calculate)

    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": CalculusOperations.function_image_calculator,
            "2": CalculusOperations.zeros_calculator,
            "3": CalculusOperations.limit_calculator,
            "4": CalculusOperations.lateral_limits_calculator,
            "5": CalculusOperations.continuity_calculator,
            "6": CalculusOperations.tangent_line_limit_calculator,
            "7": CalculusOperations.derivative_calculator,
            "8": CalculusOperations.tangent_line_derivative_calculator,
            "9": CalculusOperations.extremes_inflection_calculator,
            "10": CalculusOperations.primitive_calculator,
            "11": CalculusOperations.calculate_c_calculator,
            "12": CalculusOperations.integral_calculator,
            "13": CalculusOperations.taylor_series_calculator,
            "14": CalculusOperations.taylor_polynomial_calculator,
        }
        return calculators.get(operation_id, None)
