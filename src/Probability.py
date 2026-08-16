import tkinter as tk
from tkinter import messagebox
import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor


class ProbabilityOperations:
    """Probability and Combinatorics operations module"""

    OPERATIONS = {
        "1": "Simple Permutation (n!)",
        "2": "Permutation with Repetition",
        "3": "Simple Arrangement",
        "4": "Arrangement with Repetition",
        "5": "Combination with Repetition",
        "6": "Pascal's Triangle Element",
        "7": "Pascal's Triangle Row Sum",
        "8": "Generate Pascal's Triangle",
        "9": "Derangements (!n)",
        "10": "Pigeonhole Principle",
        "11": "Stirling Numbers (2nd Kind)",
        "12": "Classical Probability (Laplace)",
        "13": "Kolmogorov Axioms",
        "14": "Complementary Event",
        "15": "Union of Events",
        "16": "Inclusion-Exclusion (3 events)",
        "17": "Set Difference",
        "18": "De Morgan (neither event occurs)",
        "19": "Conditional Probability",
        "20": "Multiplication Rule",
        "21": "Independent Events",
        "22": "Law of Total Probability",
        "23": "Bayes' Theorem",
        "24": "Expected Value (Discrete)",
        "25": "Variance (Discrete)",
        "26": "Interval Probability (Continuous)",
        "27": "Expected Value (Continuous)",
        "28": "Variance (Continuous)",
        "29": "Standard Deviation",
        "30": "Bernoulli Distribution",
        "31": "Binomial Distribution",
        "32": "Poisson Distribution",
        "33": "Geometric Distribution",
        "34": "Z-score (Standard Normal)",
    }

    # ---------- UI helpers ----------

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
    def _to_int(s):
        value = sp.sympify(s)
        if not value.is_number or int(value) != value:
            raise ValueError("an integer is required.")
        return int(value)

    @staticmethod
    def _to_float(s):
        return float(sp.sympify(s))

    @staticmethod
    def _to_list(s):
        parts = [p.strip() for p in s.split(",") if p.strip() != ""]
        if not parts:
            raise ValueError("lista vazia.")
        return [sp.sympify(p) for p in parts]

    @staticmethod
    def _to_expr(s):
        x = sp.symbols('x')
        transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
        expr = parse_expr(s, transformations=transformations, local_dict={'x': x})
        if not expr.free_symbols.issubset({x}):
            raise ValueError("use only the variable 'x'.")
        return x, expr

    @staticmethod
    def _validate_prob(value, name="probabilidade"):
        if value < 0 or value > 1:
            raise ValueError(f"{name} must be between 0 and 1.")

    # ---------- generic form builder ----------

    @staticmethod
    def _build_generic(parent, fields, compute_fn, format_fn=None, widths=None):
        entries = []
        for i, (label, default) in enumerate(fields):
            width = widths[i] if widths else 15
            _, e = ProbabilityOperations._make_value_entry(parent, label, default, width)
            entries.append(e)

        result_label = ProbabilityOperations._make_result_label(parent)

        def calculate():
            try:
                values = [e.get() for e in entries]
                result = compute_fn(values)
                text = format_fn(result) if format_fn else f"Resultado: {result}"
                result_label.config(text=text)
            except (ValueError, TypeErrorr, ZeroDivisionErrorr, sp.SympifyErrorr, IndexErrorr) as err:
                messagebox.showerror("Error", f"Invalid input: {err}")

        ProbabilityOperations._make_calc_button(parent, calculate)

    # ---------- operations ----------

    @staticmethod
    def simple_permutation_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            if n < 0:
                raise ValueError("n must be ≥ 0.")
            return math.factorial(n)

        P._build_generic(parent, [("n =", "5")], compute, lambda r: f"n! = {r}")

    @staticmethod
    def repetition_permutation_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            reps = [int(r) for r in P._to_list(v[1])]
            denom = 1
            for r in reps:
                denom *= math.factorial(r)
            return math.factorial(n) / denom

        P._build_generic(
            parent,
            [("n =", "5"), ("Repetitions (comma-separated) =", "2,1")],
            compute,
            lambda r: f"Permutation with repetition = {r}",
            widths=[15, 25],
        )

    @staticmethod
    def simple_arrangement_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            p = P._to_int(v[1])
            return math.perm(n, p)

        P._build_generic(parent, [("n =", "5"), ("p =", "2")], compute, lambda r: f"A(n,p) = {r}")

    @staticmethod
    def repetition_arrangement_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            p = P._to_int(v[1])
            return n ** p

        P._build_generic(parent, [("n =", "5"), ("p =", "2")], compute, lambda r: f"Arrangement with repetition = {r}")

    @staticmethod
    def repetition_combination_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            p = P._to_int(v[1])
            return math.comb(n + p - 1, p)

        P._build_generic(parent, [("n =", "5"), ("p =", "2")], compute, lambda r: f"Combination with repetition = {r}")

    @staticmethod
    def pascal_element_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            p = P._to_int(v[1])
            return math.comb(n, p)

        P._build_generic(parent, [("Linha (n) =", "5"), ("Coluna (p) =", "2")], compute, lambda r: f"C(n,p) = {r}")

    @staticmethod
    def pascal_line_sum_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            return 2 ** n

        P._build_generic(parent, [("n =", "5")], compute, lambda r: f"Soma da linha n = {r}")

    @staticmethod
    def generate_pascal_triangle_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            lines = P._to_int(v[0])
            if lines < 1 or lines > 15:
                raise ValueError("use between 1 and 15 rows (to fit on screen).")
            triangle = []
            for n in range(lines):
                triangle.append([math.comb(n, k) for k in range(n + 1)])
            return triangle

        def fmt(rows):
            return "\n".join(" ".join(str(x) for x in row) for row in rows)

        P._build_generic(parent, [("Number of rows =", "6")], compute, fmt)

    @staticmethod
    def derangement_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            p = sp.symbols('p')
            total = sp.summation((-1) ** p / sp.factorial(p), (p, 0, n))
            return sp.simplify(sp.factorial(n) * total)

        P._build_generic(parent, [("n =", "5")], compute, lambda r: f"!n = {r}")

    @staticmethod
    def pigeonhole_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            m = P._to_int(v[0])
            k = P._to_int(v[1])
            return k * (m - 1) + 1

        P._build_generic(
            parent,
            [("Objetos (m) =", "10"), ("Gavetas (k) =", "3")],
            compute,
            lambda r: f"Worst case = {r} items guarantee a bin with ≥2.",
        )

    @staticmethod
    def stirling_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            k = P._to_int(v[1])
            j = sp.symbols('j', integer=True, nonnegative=True)
            total = sp.summation((-1) ** (k - j) * sp.binomial(k, j) * j ** n, (j, 0, k))
            return sp.simplify(total / sp.factorial(k))

        P._build_generic(parent, [("n =", "4"), ("k =", "2")], compute, lambda r: f"S(n,k) = {r}")

    @staticmethod
    def classical_probability_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            fav = P._to_float(v[0])
            total = P._to_float(v[1])
            if total == 0:
                raise ValueError("total cannot be zero.")
            return fav / total

        P._build_generic(
            parent,
            [("Favorable outcomes =", "5"), ("Total outcomes =", "20")],
            compute,
            lambda r: f"P(A) = {r:.6f}",
        )

    @staticmethod
    def kolmogorov_axioms_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            p = P._to_float(v[0])
            return 0 <= p <= 1

        P._build_generic(
            parent,
            [("Probabilidade a validar =", "0.5")],
            compute,
            lambda r: "Valid (0 ≤ P ≤ 1)" if r else "Invalid (outside [0, 1])",
        )

    @staticmethod
    def complementary_event_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            p = P._to_float(v[0])
            P._validate_prob(p, "P(A)")
            return 1 - p

        P._build_generic(parent, [("P(A) =", "0.3")], compute, lambda r: f"P(Aᶜ) = {r}")

    @staticmethod
    def addition_rule_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            a, b, i = (P._to_float(x) for x in v)
            for val, name in ((a, "P(A)"), (b, "P(B)"), (i, "P(A∩B)")):
                P._validate_prob(val, name)
            return a + b - i

        P._build_generic(
            parent,
            [("P(A) =", "0.4"), ("P(B) =", "0.3"), ("P(A∩B) =", "0.1")],
            compute,
            lambda r: f"P(A∪B) = {r}",
        )

    @staticmethod
    def inclusion_exclusion_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            a, b, c, ab, ac, bc, abc = (P._to_float(x) for x in v)
            for val, name in ((a, "P(A)"), (b, "P(B)"), (c, "P(C)"), (ab, "P(A∩B)"),
                              (ac, "P(A∩C)"), (bc, "P(B∩C)"), (abc, "P(A∩B∩C)")):
                P._validate_prob(val, name)
            return a + b + c - (ab + ac + bc) + abc

        P._build_generic(
            parent,
            [("P(A) =", "0.3"), ("P(B) =", "0.3"), ("P(C) =", "0.3"),
             ("P(A∩B) =", "0.1"), ("P(A∩C) =", "0.1"), ("P(B∩C) =", "0.1"), ("P(A∩B∩C) =", "0.05")],
            compute,
            lambda r: f"P(A∪B∪C) = {r}",
            widths=[10] * 7,
        )

    @staticmethod
    def set_difference_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            a, i = (P._to_float(x) for x in v)
            P._validate_prob(a, "P(A)")
            P._validate_prob(i, "P(A∩B)")
            return a - i

        P._build_generic(parent, [("P(A) =", "0.5"), ("P(A∩B) =", "0.2")], compute, lambda r: f"P(A\\B) = {r}")

    @staticmethod
    def demorgan_neither_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            a, b, i = (P._to_float(x) for x in v)
            for val, name in ((a, "P(A)"), (b, "P(B)"), (i, "P(A∩B)")):
                P._validate_prob(val, name)
            return 1 - (a + b - i)

        P._build_generic(
            parent,
            [("P(A) =", "0.4"), ("P(B) =", "0.3"), ("P(A∩B) =", "0.1")],
            compute,
            lambda r: f"P(Aᶜ∩Bᶜ) = {r}",
        )

    @staticmethod
    def conditional_probability_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            i, b = (P._to_float(x) for x in v)
            P._validate_prob(i, "P(A∩B)")
            P._validate_prob(b, "P(B)")
            if b == 0:
                raise ValueError("P(B) tem de ser maior que zero.")
            return i / b

        P._build_generic(parent, [("P(A∩B) =", "0.2"), ("P(B) =", "0.5")], compute, lambda r: f"P(A|B) = {r}")

    @staticmethod
    def multiplication_rule_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            b, cond = (P._to_float(x) for x in v)
            P._validate_prob(b, "P(B)")
            P._validate_prob(cond, "P(A|B)")
            return b * cond

        P._build_generic(parent, [("P(B) =", "0.5"), ("P(A|B) =", "0.4")], compute, lambda r: f"P(A∩B) = {r}")

    @staticmethod
    def independent_events_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            a, b = (P._to_float(x) for x in v)
            P._validate_prob(a, "P(A)")
            P._validate_prob(b, "P(B)")
            return a * b

        P._build_generic(parent, [("P(A) =", "0.5"), ("P(B) =", "0.4")], compute, lambda r: f"P(A∩B) = {r}")

    @staticmethod
    def law_of_total_probability_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            priors = [float(x) for x in P._to_list(v[0])]
            likelihoods = [float(x) for x in P._to_list(v[1])]
            if len(priors) != len(likelihoods):
                raise ValueError("the lists must have the same length.")
            for p in priors:
                P._validate_prob(p, "P(B_i)")
            for l in likelihoods:
                P._validate_prob(l, "P(A|B_i)")
            return sum(p * l for p, l in zip(priors, likelihoods))

        P._build_generic(
            parent,
            [("Priors P(B_i), comma-separated =", "0.2,0.3,0.5"),
             ("Likelihoods P(A|B_i), comma-separated =", "0.4,0.6,0.2")],
            compute,
            lambda r: f"P(A) = {r}",
            widths=[30, 30],
        )

    @staticmethod
    def bayes_theorem_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            k = P._to_int(v[0])
            priors = [float(x) for x in P._to_list(v[1])]
            likelihoods = [float(x) for x in P._to_list(v[2])]
            if len(priors) != len(likelihoods):
                raise ValueError("the lists must have the same length.")
            denom = sum(p * l for p, l in zip(priors, likelihoods))
            if denom == 0:
                raise ValueError("the denominator cannot be zero.")
            return (priors[k] * likelihoods[k]) / denom

        P._build_generic(
            parent,
            [("Index k (starts at 0) =", "0"),
             ("Priors P(B_i) =", "0.2,0.3,0.5"),
             ("Likelihoods P(A|B_i) =", "0.4,0.6,0.2")],
            compute,
            lambda r: f"P(B_k|A) = {r}",
            widths=[10, 30, 30],
        )

    @staticmethod
    def discrete_expected_value_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            xs = [float(x) for x in P._to_list(v[0])]
            ps = [float(x) for x in P._to_list(v[1])]
            if len(xs) != len(ps):
                raise ValueError("the lists must have the same length.")
            if abs(sum(ps) - 1) > 1e-9:
                raise ValueError("the probabilities must sum to 1.")
            return sum(x * p for x, p in zip(xs, ps))

        P._build_generic(
            parent,
            [("Values x_i =", "1,2,3"), ("Probabilities P(X=x_i) =", "0.2,0.5,0.3")],
            compute,
            lambda r: f"E[X] = {r}",
            widths=[25, 25],
        )

    @staticmethod
    def discrete_variance_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            xs = [float(x) for x in P._to_list(v[0])]
            ps = [float(x) for x in P._to_list(v[1])]
            if len(xs) != len(ps):
                raise ValueError("the lists must have the same length.")
            if abs(sum(ps) - 1) > 1e-9:
                raise ValueError("the probabilities must sum to 1.")
            mean = sum(x * p for x, p in zip(xs, ps))
            e_sq = sum((x ** 2) * p for x, p in zip(xs, ps))
            return e_sq - mean ** 2

        P._build_generic(
            parent,
            [("Values x_i =", "1,2,3"), ("Probabilities P(X=x_i) =", "0.2,0.5,0.3")],
            compute,
            lambda r: f"Var(X) = {r}",
            widths=[25, 25],
        )

    @staticmethod
    def interval_probability_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            x, f = P._to_expr(v[0])
            a = P._to_float(v[1])
            b = P._to_float(v[2])
            return sp.integrate(f, (x, a, b))

        P._build_generic(
            parent,
            [("f(x) =", "3*x**2"), ("a =", "0"), ("b =", "1")],
            compute,
            lambda r: f"P(a ≤ X ≤ b) = {r}",
            widths=[25, 10, 10],
        )

    @staticmethod
    def continuous_expected_value_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            x, f = P._to_expr(v[0])
            a = P._to_float(v[1])
            b = P._to_float(v[2])
            return sp.integrate(x * f, (x, a, b))

        P._build_generic(
            parent,
            [("f(x) =", "3*x**2"), ("Lower bound =", "0"), ("Upper bound =", "1")],
            compute,
            lambda r: f"E[X] = {r}",
            widths=[25, 10, 10],
        )

    @staticmethod
    def continuous_variance_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            x, f = P._to_expr(v[0])
            a = P._to_float(v[1])
            b = P._to_float(v[2])
            expected = sp.integrate(x * f, (x, a, b))
            e_sq = sp.integrate((x ** 2) * f, (x, a, b))
            return e_sq - expected ** 2

        P._build_generic(
            parent,
            [("f(x) =", "3*x**2"), ("Lower bound =", "0"), ("Upper bound =", "1")],
            compute,
            lambda r: f"Var(X) = {r}",
            widths=[25, 10, 10],
        )

    @staticmethod
    def standard_deviation_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            var = P._to_float(v[0])
            if var < 0:
                raise ValueError("variance cannot be negative.")
            return sp.sqrt(var)

        P._build_generic(parent, [("Variance =", "4")], compute, lambda r: f"σ = {r}")

    @staticmethod
    def bernoulli_distribution_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            k = P._to_int(v[0])
            p = P._to_float(v[1])
            P._validate_prob(p, "p")
            prob = (p ** k) * ((1 - p) ** (1 - k))
            return prob, p, p * (1 - p)

        P._build_generic(
            parent,
            [("k (0 ou 1) =", "1"), ("p =", "0.5")],
            compute,
            lambda r: f"P(X=k) = {r[0]}\nE[X] = {r[1]}\nVar(X) = {r[2]}",
        )

    @staticmethod
    def binomial_distribution_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            n = P._to_int(v[0])
            k = P._to_int(v[1])
            p = P._to_float(v[2])
            P._validate_prob(p, "p")
            prob = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
            return prob, n * p, n * p * (1 - p)

        P._build_generic(
            parent,
            [("n =", "10"), ("k =", "3"), ("p =", "0.5")],
            compute,
            lambda r: f"P(X=k) = {r[0]:.6f}\nE[X] = {r[1]}\nVar(X) = {r[2]}",
        )

    @staticmethod
    def poisson_distribution_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            k = P._to_int(v[0])
            lam = P._to_float(v[1])
            if lam <= 0:
                raise ValueError("λ must be greater than zero.")
            prob = (lam ** k) * math.exp(-lam) / math.factorial(k)
            return prob, lam, lam

        P._build_generic(
            parent,
            [("k =", "2"), ("λ =", "3")],
            compute,
            lambda r: f"P(X=k) = {r[0]:.6f}\nE[X] = {r[1]}\nVar(X) = {r[2]}",
        )

    @staticmethod
    def geometric_distribution_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            k = P._to_int(v[0])
            p = P._to_float(v[1])
            if p <= 0 or p > 1:
                raise ValueError("p must be between 0 (exclusive) and 1.")
            prob = ((1 - p) ** (k - 1)) * p
            return prob, 1 / p, (1 - p) / (p ** 2)

        P._build_generic(
            parent,
            [("k =", "3"), ("p =", "0.3")],
            compute,
            lambda r: f"P(X=k) = {r[0]:.6f}\nE[X] = {r[1]:.4f}\nVar(X) = {r[2]:.4f}",
        )

    @staticmethod
    def normal_standard_zscore_calculator(parent):
        P = ProbabilityOperations

        def compute(v):
            x = P._to_float(v[0])
            mu = P._to_float(v[1])
            sigma = P._to_float(v[2])
            if sigma == 0:
                raise ValueError("σ cannot be zero.")
            return (x - mu) / sigma, 0, 1

        P._build_generic(
            parent,
            [("x =", "1.96"), ("μ =", "0"), ("σ =", "1")],
            compute,
            lambda r: f"Z-score = {r[0]:.4f}\nE[Z] = {r[1]}\nVar(Z) = {r[2]}",
        )

    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": ProbabilityOperations.simple_permutation_calculator,
            "2": ProbabilityOperations.repetition_permutation_calculator,
            "3": ProbabilityOperations.simple_arrangement_calculator,
            "4": ProbabilityOperations.repetition_arrangement_calculator,
            "5": ProbabilityOperations.repetition_combination_calculator,
            "6": ProbabilityOperations.pascal_element_calculator,
            "7": ProbabilityOperations.pascal_line_sum_calculator,
            "8": ProbabilityOperations.generate_pascal_triangle_calculator,
            "9": ProbabilityOperations.derangement_calculator,
            "10": ProbabilityOperations.pigeonhole_calculator,
            "11": ProbabilityOperations.stirling_calculator,
            "12": ProbabilityOperations.classical_probability_calculator,
            "13": ProbabilityOperations.kolmogorov_axioms_calculator,
            "14": ProbabilityOperations.complementary_event_calculator,
            "15": ProbabilityOperations.addition_rule_calculator,
            "16": ProbabilityOperations.inclusion_exclusion_calculator,
            "17": ProbabilityOperations.set_difference_calculator,
            "18": ProbabilityOperations.demorgan_neither_calculator,
            "19": ProbabilityOperations.conditional_probability_calculator,
            "20": ProbabilityOperations.multiplication_rule_calculator,
            "21": ProbabilityOperations.independent_events_calculator,
            "22": ProbabilityOperations.law_of_total_probability_calculator,
            "23": ProbabilityOperations.bayes_theorem_calculator,
            "24": ProbabilityOperations.discrete_expected_value_calculator,
            "25": ProbabilityOperations.discrete_variance_calculator,
            "26": ProbabilityOperations.interval_probability_calculator,
            "27": ProbabilityOperations.continuous_expected_value_calculator,
            "28": ProbabilityOperations.continuous_variance_calculator,
            "29": ProbabilityOperations.standard_deviation_calculator,
            "30": ProbabilityOperations.bernoulli_distribution_calculator,
            "31": ProbabilityOperations.binomial_distribution_calculator,
            "32": ProbabilityOperations.poisson_distribution_calculator,
            "33": ProbabilityOperations.geometric_distribution_calculator,
            "34": ProbabilityOperations.normal_standard_zscore_calculator,
        }
        return calculators.get(operation_id, None)
