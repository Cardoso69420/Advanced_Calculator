import tkinter as tk
from tkinter import messagebox
import math
import sympy as sp


class ProbabilityOperations:
    """Probability and Combinatorics operations module"""

    OPERATIONS = {
        "1": "Permutations",
        "2": "Combinations",
        "3": "Factorial",
        "4": "Probability",
        "5": "Binomial Distribution",
        "6": "Normal Distribution",
    }

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
    def permutations_calculator(parent):
        """P(n, r) = n! / (n-r)!"""

        _, n_entry = ProbabilityOperations._make_value_entry(parent, "n =", "10")
        _, r_entry = ProbabilityOperations._make_value_entry(parent, "r =", "3")

        result_label = ProbabilityOperations._make_result_label(parent)

        def calculate():
            try:
                n = int(sp.sympify(n_entry.get()))
                r = int(sp.sympify(r_entry.get()))
                if n < 0 or r < 0 or r > n:
                    messagebox.showerror("Error", "Need 0 ≤ r ≤ n.")
                    return
                result = math.perm(n, r)
                result_label.config(text=f"P({n}, {r}) = n!/(n-r)! = {result}")
            except (ValueError, TypeError, sp.SympifyError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        ProbabilityOperations._make_calc_button(parent, calculate)

    @staticmethod
    def combinations_calculator(parent):
        """C(n, r) = n! / (r!(n-r)!)"""

        _, n_entry = ProbabilityOperations._make_value_entry(parent, "n =", "10")
        _, r_entry = ProbabilityOperations._make_value_entry(parent, "r =", "3")

        result_label = ProbabilityOperations._make_result_label(parent)

        def calculate():
            try:
                n = int(sp.sympify(n_entry.get()))
                r = int(sp.sympify(r_entry.get()))
                if n < 0 or r < 0 or r > n:
                    messagebox.showerror("Error", "Need 0 ≤ r ≤ n.")
                    return
                result = math.comb(n, r)
                result_label.config(text=f"C({n}, {r}) = n!/(r!(n-r)!) = {result}")
            except (ValueError, TypeError, sp.SympifyError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        ProbabilityOperations._make_calc_button(parent, calculate)

    @staticmethod
    def factorial_calculator(parent):
        """n!"""

        _, n_entry = ProbabilityOperations._make_value_entry(parent, "n =", "5")

        result_label = ProbabilityOperations._make_result_label(parent)

        def calculate():
            try:
                n = int(sp.sympify(n_entry.get()))
                if n < 0:
                    messagebox.showerror("Error", "n must be a non-negative integer.")
                    return
                result = math.factorial(n)
                # Show step-by-step for small n
                if n <= 10:
                    steps = " × ".join(str(i) for i in range(1, n + 1)) if n > 0 else "1"
                    text = f"{n}! = {steps} = {result}"
                else:
                    text = f"{n}! = {result}"
                result_label.config(text=text)
            except (ValueError, TypeError, sp.SympifyError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        ProbabilityOperations._make_calc_button(parent, calculate)

    @staticmethod
    def probability_calculator(parent):
        """Classical probability P = favorable / total."""

        _, fav_entry = ProbabilityOperations._make_value_entry(parent, "Favorable outcomes =", "5")
        _, total_entry = ProbabilityOperations._make_value_entry(parent, "Total outcomes =", "20")

        result_label = ProbabilityOperations._make_result_label(parent)

        def calculate():
            try:
                fav = float(sp.sympify(fav_entry.get()))
                total = float(sp.sympify(total_entry.get()))
                if total == 0:
                    messagebox.showerror("Error", "Total outcomes cannot be zero.")
                    return
                if fav < 0 or fav > total:
                    messagebox.showerror("Error", "Need 0 ≤ favorable ≤ total.")
                    return
                p = fav / total
                complement = 1 - p
                text = f"""
P(A)         = {fav} / {total} = {p:.6f}
P(Aᶜ)        = 1 − P(A) = {complement:.6f}
Percentage   = {p * 100:.4f}%
                """
                result_label.config(text=text)
            except (ValueError, TypeError, sp.SympifyError, ZeroDivisionError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        ProbabilityOperations._make_calc_button(parent, calculate)

    @staticmethod
    def binomial_distribution_calculator(parent):
        """Binomial distribution: P(X=k), E[X], Var(X)."""

        _, n_entry = ProbabilityOperations._make_value_entry(parent, "n (trials) =", "10")
        _, k_entry = ProbabilityOperations._make_value_entry(parent, "k (successes) =", "3")
        _, p_entry = ProbabilityOperations._make_value_entry(parent, "p (success prob.) =", "0.5")

        result_label = ProbabilityOperations._make_result_label(parent)

        def calculate():
            try:
                n = int(sp.sympify(n_entry.get()))
                k = int(sp.sympify(k_entry.get()))
                p = float(sp.sympify(p_entry.get()))
                if n < 0 or k < 0 or k > n:
                    messagebox.showerror("Error", "Need 0 ≤ k ≤ n.")
                    return
                if p < 0 or p > 1:
                    messagebox.showerror("Error", "Need 0 ≤ p ≤ 1.")
                    return
                prob = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
                expected = n * p
                variance = n * p * (1 - p)
                std = math.sqrt(variance)
                text = f"""
P(X = {k})    = C({n},{k}) · {p}^{k} · (1−{p})^({n}−{k}) = {prob:.6f}
E[X]          = n · p = {expected:.4f}
Var(X)        = n · p · (1−p) = {variance:.4f}
σ             = √Var(X) = {std:.4f}
                """
                result_label.config(text=text)
            except (ValueError, TypeError, sp.SympifyError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        ProbabilityOperations._make_calc_button(parent, calculate)

    @staticmethod
    def normal_distribution_calculator(parent):
        """Normal distribution: PDF and CDF values at x."""

        _, x_entry = ProbabilityOperations._make_value_entry(parent, "x =", "1.96")
        _, mu_entry = ProbabilityOperations._make_value_entry(parent, "μ (mean) =", "0")
        _, sigma_entry = ProbabilityOperations._make_value_entry(parent, "σ (std. dev.) =", "1")

        result_label = ProbabilityOperations._make_result_label(parent)

        def calculate():
            try:
                x = float(sp.sympify(x_entry.get()))
                mu = float(sp.sympify(mu_entry.get()))
                sigma = float(sp.sympify(sigma_entry.get()))
                if sigma <= 0:
                    messagebox.showerror("Error", "σ must be > 0.")
                    return
                # PDF: f(x) = 1/(σ√2π) · exp(-(x-μ)²/(2σ²))
                pdf = (1 / (sigma * math.sqrt(2 * math.pi))) * \
                      math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
                # CDF: F(x) = 0.5 · (1 + erf((x-μ)/(σ√2)))
                z = (x - mu) / (sigma * math.sqrt(2))
                cdf = 0.5 * (1 + math.erf(z))
                z_score = (x - mu) / sigma
                text = f"""
x            = {x}
μ            = {mu}
σ            = {sigma}
Z-score      = (x−μ)/σ = {z_score:.4f}
PDF f(x)     = {pdf:.6f}
CDF F(x)     = P(X ≤ {x}) = {cdf:.6f}
                """
                result_label.config(text=text)
            except (ValueError, TypeError, sp.SympifyError) as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        ProbabilityOperations._make_calc_button(parent, calculate)

    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": ProbabilityOperations.permutations_calculator,
            "2": ProbabilityOperations.combinations_calculator,
            "3": ProbabilityOperations.factorial_calculator,
            "4": ProbabilityOperations.probability_calculator,
            "5": ProbabilityOperations.binomial_distribution_calculator,
            "6": ProbabilityOperations.normal_distribution_calculator,
        }
        return calculators.get(operation_id, None)
