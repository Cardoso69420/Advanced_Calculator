# Quick Start - Modular Math Calculator

## 30 Seconds to Launch

### 1. Make sure all files are in same folder:
```
Calculator.py
Geometry.py
ComplexNumbers.py
Sequences.py
Calculus.py
Probability.py
```

### 2. Run:
```bash
python Calculator.py
```

### 3. Click buttons!

---

## File Organization

Each math topic is a **separate file** with a **separate class**:

| File | Class | Operations |
|------|-------|------------|
| `Calculator.py` | `MathCalculator` | GUI controller (main) |
| `Geometry.py` | `GeometryOperations` | 7 geometry operations ✅ |
| `ComplexNumbers.py` | `ComplexNumbersOperations` | 10 complex number operations ✅ |
| `Sequences.py` | `SequencesOperations` | 8 sequence operations ✅ |
| `Calculus.py` | `CalculusOperations` | 14 calculus operations ✅ |
| `Probability.py` | `ProbabilityOperations` | 34 probability operations ✅ |

---

## Currently Working

✅ **All Modules** - All 73 operations fully implemented and working:
1. Geometry and Trigonometry (7 operations)
2. Complex Numbers (10 operations)
3. Sequences and Series (8 operations)
4. Calculus (14 operations)
5. Probability and Combinatorics (34 operations)

---

## How to Add More Operations

### Example: Add 8th Geometry Operation

**File:** `Geometry.py`

**Step 1:** Add to operations dictionary
```python
OPERATIONS = {
    "1": "Area",
    "2": "Pythagorean Theorem",
    # ... existing ...
    "8": "My New Operation",  # ← Add this
}
```

**Step 2:** Create calculator method
```python
@staticmethod
def my_new_operation_calculator(parent):
    """My new operation description"""
    
    # Input
    input_frame = tk.Frame(parent, bg="#f0f0f0")
    input_frame.pack(fill="x", pady=10)
    
    tk.Label(input_frame, text="Input:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
    input_entry = tk.Entry(input_frame, width=15, font=("Arial", 11))
    input_entry.pack(side="left", padx=5)
    
    # Result
    result_frame = tk.Frame(parent, bg="#f0f0f0")
    result_frame.pack(fill="both", expand=True, pady=20)
    
    result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 12), bg="#f0f0f0", fg="#333")
    result_label.pack(anchor="center")
    
    # Calculate function
    def calculate():
        try:
            value = float(input_entry.get())
            result = value * 2  # Your calculation
            result_label.config(text=f"Result: {result:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")
    
    # Button
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
```

**Step 3:** Add to get_calculator()
```python
@staticmethod
def get_calculator(operation_id):
    calculators = {
        "1": GeometryOperations.area_calculator,
        # ... existing ...
        "8": GeometryOperations.my_new_operation_calculator,  # ← Add this
    }
    return calculators.get(operation_id, None)
```

**Step 4:** Done! Run Calculator.py and see your operation in the list

---

## How to Create a New Module

Example: Adding "Linear Algebra" module

### Step 1: Create `LinearAlgebra.py`

```python
import tkinter as tk
from tkinter import messagebox


class LinearAlgebraOperations:
    """Linear Algebra operations module"""
    
    OPERATIONS = {
        "1": "Matrix Addition",
        "2": "Matrix Multiplication",
        "3": "Determinant",
    }
    
    @staticmethod
    def matrix_addition_calculator(parent):
        # Your calculator code here
        label = tk.Label(parent, text="Coming soon!", font=("Arial", 14), bg="#f0f0f0")
        label.pack(expand=True)
    
    @staticmethod
    def get_calculator(operation_id):
        calculators = {
            "1": LinearAlgebraOperations.matrix_addition_calculator,
            "2": lambda p: LinearAlgebraOperations.placeholder(p, "Matrix Multiplication"),
            "3": lambda p: LinearAlgebraOperations.placeholder(p, "Determinant"),
        }
        return calculators.get(operation_id, None)
    
    @staticmethod
    def placeholder(parent, name):
        label = tk.Label(parent, text=f"{name}\n(Coming soon!)", font=("Arial", 14), bg="#f0f0f0")
        label.pack(expand=True)
```

### Step 2: Add to `Calculator.py`

At the top, add import:
```python
from LinearAlgebra import LinearAlgebraOperations
```

In `__init__` method, update modules:
```python
self.modules = {
    "1": ("Geometry and Trigonometry", GeometryOperations),
    "2": ("Probability and Combinatorics", ProbabilityOperations),
    "3": ("Sequences and Series", SequencesOperations),
    "4": ("Calculus", CalculusOperations),
    "5": ("Complex Numbers", ComplexNumbersOperations),
    "6": ("Linear Algebra", LinearAlgebraOperations),  # ← Add this
}
```

### Step 3: Done!

Now "Linear Algebra" appears in the home screen!

---

## File Structure Visualization

```
When you run Calculator.py:

1. Calculator.py loads
   ├── Imports all module classes
   ├── Creates MathCalculator GUI
   └── Shows home screen
   
2. User clicks "Geometry"
   ├── Calculator.py calls show_module_menu()
   ├── Passes GeometryOperations class
   ├── Gets list from GeometryOperations.OPERATIONS
   └── Displays 7 operation buttons
   
3. User clicks "Area"
   ├── Calculator.py calls show_calculator()
   ├── Calls GeometryOperations.get_calculator("1")
   ├── Gets GeometryOperations.area_calculator
   ├── Calls area_calculator(frame)
   └── UI appears for area calculation
```

---

## What Each File Does

### Calculator.py (Main File)
- **Job:** Control GUI navigation
- **Contains:** MathCalculator class
- **Does:** Switches between screens, calls module calculators
- **When to edit:** If you want to change appearance, colors, or navigation

### Geometry.py (Example Module)
- **Job:** All geometry operations
- **Contains:** GeometryOperations class (7 methods)
- **Does:** Each method creates a calculator UI
- **When to edit:** To add/modify geometry operations

### Other Module Files
- **Pattern:** Same as Geometry.py
- **Status:** Fully implemented, same as Geometry.py
- **Requires:** Sympy for symbolic math (Sequences, Calculus)

---

## Common Tasks

### Change a button color
```python
# Find the button creation, change bg color
btn = tk.Button(
    parent,
    text="Calculate",
    bg="#4CAF50",  # Change this (green)
    # ...
)
```

### Add another input field
```python
# Duplicate the input_frame section:
input2_frame = tk.Frame(parent, bg="#f0f0f0")
input2_frame.pack(fill="x", pady=10)

tk.Label(input2_frame, text="Input 2:", font=("Arial", 11), bg="#f0f0f0").pack(side="left", padx=5)
input2_entry = tk.Entry(input2_frame, width=15, font=("Arial", 11))
input2_entry.pack(side="left", padx=5)

# In calculate function:
def calculate():
    value1 = float(input_entry.get())
    value2 = float(input2_entry.get())  # ← Use both
    # ...
```

### Show multiple results
```python
# Instead of single result:
result_label.config(text=f"Result: {result:.4f}")

# Use formatted text:
results = f"""
Area: {area:.4f}
Perimeter: {perimeter:.4f}
Diagonal: {diagonal:.4f}
"""
result_label.config(text=results)
```

---

## Troubleshooting

### "ImportError: cannot import name 'GeometryOperations'"
- Make sure `Geometry.py` is in same folder
- Check spelling: `Geometry.py` not `geometry.py`

### "ModuleNotFoundError: No module named 'sympy'"
- Install sympy: `pip install sympy`
- Needed for Sequences, Calculus modules

### Button doesn't appear
- Check indentation
- Make sure you added operation to OPERATIONS dict
- Make sure you added method to get_calculator()
- Make sure method is @staticmethod

### GUI doesn't respond
- Check for infinite loops in calculate()
- Make sure messagebox is imported: `from tkinter import messagebox`

---

## Project Status

```
Total Operations: 73/73 (100%)

✅ Geometry:           7/7  (100%)
✅ Complex Numbers:    10/10 (100%)
✅ Sequences:          8/8  (100%)
✅ Calculus:           14/14 (100%)
✅ Probability:        34/34 (100%)

Status: All modules complete and working
```

---

## Next Steps

1. **Run it:** `python Calculator.py`
2. **Test all modules:** Try operations across all 5 topics
3. **Add to existing:** Pick a module and add new operations
4. **Create new:** Add a completely new module

---

## Documentation Files

- **README.md** - Detailed overview
- **ARCHITECTURE.md** - How everything connects
- **QUICK_START_MODULAR.md** - This file! Quick reference
- **Geometry.py** - Example of completed module

---

**You're ready to go! Launch Calculator.py and start exploring.**
