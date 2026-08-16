import tkinter as tk
from tkinter import messagebox
import sympy as sp


class SequencesOperations:
    """Sequences and Series operations module"""

    OPERATIONS = {
        "1": "Calculate Term",
        "2": "First K Terms",
        "3": "Sequence Limit",
        "4": "Sum First K Terms",
        "5": "Infinite Sum",
        "6": "Symbolic Series",
        "7": "Convergence (Sequence)",
        "8": "Convergence (Series)",
    }

    @staticmethod
    def _make_term_entry(parent, default="n**2 + 1"):
        """Helper: input for the general term a_n."""
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text="a_n =", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        entry = tk.Entry(frame, width=25, font=("Arial", 11))
        entry.pack(side="left", padx=5)
        entry.insert(0, default)
        return frame, entry

    @staticmethod
    def _make_value_entry(parent, label, default):
        """Helper: labelled numeric input."""
        frame = tk.Frame(parent, bg="#f0f0f0")
        frame.pack(fill="x", pady=5)
        tk.Label(frame, text=label, font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
        entry = tk.Entry(frame, width=15, font=("Arial", 11))
        entry.pack(side="left", padx=5)
        entry.insert(0, default)
        return frame, entry

    @staticmethod
    def _make_result_label(parent):
        """Helper: multi-line result label."""
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
        """Helper: green Calculate button."""
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
    def _parse_term(entry):
        """Helper: parse a_n as a sympy expression of n."""
        n = sp.Symbol('n', integer=True, positive=True)
        text = entry.get()
        return n, sp.sympify(text, locals={'n': n})

    @staticmethod
    def calculate_term_calculator(parent):
        """Compute a_k for a given k."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "n**2 + 1")
        _, k_entry = SequencesOperations._make_value_entry(parent, "n =", "5")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                k = int(sp.sympify(k_entry.get()))
                value = expr.subs(n, k)
                result_label.config(text=f"a_{k} = {sp.simplify(value)}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def first_k_terms_calculator(parent):
        """List the first k terms of a sequence."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "n**2")
        _, k_entry = SequencesOperations._make_value_entry(parent, "k =", "5")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                k = int(sp.sympify(k_entry.get()))
                if k > 100:
                    messagebox.showerror("Error", "k must be ≤ 100 to keep the output readable.")
                    return
                lines = [f"a_{i} = {sp.simplify(expr.subs(n, i))}" for i in range(1, k + 1)]
                result_label.config(text="First " + str(k) + " terms:\n" + "\n".join(lines))
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def sequence_limit_calculator(parent):
        """lim n→∞ of a_n."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "(n + 1) / n")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                value = sp.limit(expr, n, sp.oo)
                result_label.config(text=f"lim (n→∞) a_n = {value}")
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def sum_k_terms_calculator(parent):
        """Sum of the first k terms."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "n**2")
        _, k_entry = SequencesOperations._make_value_entry(parent, "k =", "5")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                k = int(sp.sympify(k_entry.get()))
                total = sp.summation(expr, (n, 1, k))
                result_label.config(
                    text=f"Σ (n=1 to {k}) a_n = {sp.simplify(total)}"
                )
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def infinite_sum_calculator(parent):
        """Sum of the series from n=1 to ∞."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "1 / 2**n")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                value = sp.summation(expr, (n, 1, sp.oo))
                if value == sp.oo or value == -sp.oo:
                    text = f"Σ (n=1 to ∞) a_n diverges ({value})"
                else:
                    text = f"Σ (n=1 to ∞) a_n = {value}"
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def symbolic_series_calculator(parent):
        """Closed-form sum of a symbolic series from n=1 to n."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "n")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                # Find the partial sum as a symbolic function of the upper bound
                upper = sp.Symbol('n', positive=True, integer=True)
                partial = sp.summation(expr.subs(n, sp.Symbol('i', integer=True, positive=True)),
                                       (sp.Symbol('i', integer=True, positive=True), 1, upper))
                result_label.config(
                    text=f"a_n = {expr}\n\nS_n (closed form) = {sp.simplify(partial)}"
                )
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def sequence_convergence_calculator(parent):
        """Test whether a sequence converges as n→∞."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "(1 + 1/n)**n")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                value = sp.limit(expr, n, sp.oo)
                if value == sp.oo or value == -sp.oo or value == sp.zoo:
                    text = (
                        f"a_n = {expr}\n"
                        f"lim (n→∞) a_n = {value}\n"
                        f"✗ Sequence DIVERGES (limit is infinite or undefined)."
                    )
                else:
                    text = (
                        f"a_n = {expr}\n"
                        f"lim (n→∞) a_n = {value}\n"
                        f"✓ Sequence CONVERGES to {value}."
                    )
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def series_convergence_calculator(parent):
        """Test whether the series Σ a_n converges."""

        _, term_entry = SequencesOperations._make_term_entry(parent, "1 / n**2")

        result_label = SequencesOperations._make_result_label(parent)

        def calculate():
            try:
                n, expr = SequencesOperations._parse_term(term_entry)
                total = sp.summation(expr, (n, 1, sp.oo))
                if total == sp.oo or total == -sp.oo or total == sp.zoo:
                    text = (
                        f"a_n = {expr}\n"
                        f"Σ (n=1 to ∞) a_n = diverges\n"
                        f"✗ Series DIVERGES."
                    )
                else:
                    text = (
                        f"a_n = {expr}\n"
                        f"Σ (n=1 to ∞) a_n = {total}\n"
                        f"✓ Series CONVERGES to {total}."
                    )
                result_label.config(text=text)
            except (sp.SympifyError, TypeError, ValueError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        SequencesOperations._make_calc_button(parent, calculate)

    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": SequencesOperations.calculate_term_calculator,
            "2": SequencesOperations.first_k_terms_calculator,
            "3": SequencesOperations.sequence_limit_calculator,
            "4": SequencesOperations.sum_k_terms_calculator,
            "5": SequencesOperations.infinite_sum_calculator,
            "6": SequencesOperations.symbolic_series_calculator,
            "7": SequencesOperations.sequence_convergence_calculator,
            "8": SequencesOperations.series_convergence_calculator,
        }
        return calculators.get(operation_id, None)
