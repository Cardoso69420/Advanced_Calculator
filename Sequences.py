import tkinter as tk
from tkinter import messagebox


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
        
        info_label = tk.Label(
            parent,
            text="Sympy setup needed for symbolic math operations",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666"
        )
        info_label.pack(pady=10)
    
    @staticmethod
    def get_calculator(operation_id):
        """Return calculator method based on operation ID"""
        calculators = {
            "1": lambda p: SequencesOperations.placeholder_calculator(p, "Calculate Term"),
            "2": lambda p: SequencesOperations.placeholder_calculator(p, "First K Terms"),
            "3": lambda p: SequencesOperations.placeholder_calculator(p, "Sequence Limit"),
            "4": lambda p: SequencesOperations.placeholder_calculator(p, "Sum First K Terms"),
            "5": lambda p: SequencesOperations.placeholder_calculator(p, "Infinite Sum"),
            "6": lambda p: SequencesOperations.placeholder_calculator(p, "Symbolic Series"),
            "7": lambda p: SequencesOperations.placeholder_calculator(p, "Convergence (Sequence)"),
            "8": lambda p: SequencesOperations.placeholder_calculator(p, "Convergence (Series)"),
        }
        return calculators.get(operation_id, None)
