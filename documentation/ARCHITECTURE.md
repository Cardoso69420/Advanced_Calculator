# Calculator Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Calculator.py (Main)                     │
│                                                               │
│  - Tkinter GUI Framework                                    │
│  - Navigation Logic                                          │
│  - Module Orchestration                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
          ┌──────────┼──────────┬────────────┬────────────┐
          │          │          │            │            │
    ┌─────▼─┐  ┌────▼──┐  ┌───▼───┐  ┌────▼──┐  ┌──────▼┐
    │ Geom. │  │Complex│  │Sequen.│  │Calcul.│  │Probab.│
    │  .py  │  │ .py   │  │  .py  │  │  .py  │  │  .py  │
    └───────┘  └───────┘  └───────┘  └───────┘  └───────┘
```

## Call Flow

### Launch Sequence
```
1. User runs: python Calculator.py
   ↓
2. MathCalculator.__init__() called
   ↓
3. show_home_screen() displays 5 module options
   ↓
4. User clicks module button
```

### Module Selection Flow
```
User clicks "Geometry and Trigonometry"
   ↓
show_module_menu(key, name, GeometryOperations)
   ↓
Display list of 7 operations from GeometryOperations.OPERATIONS
   ↓
User clicks operation (e.g., "Area")
```

### Calculator Display Flow
```
User clicks "Area"
   ↓
show_calculator(operation_id="1", operation_name="Area", module_class=GeometryOperations)
   ↓
Get calculator: GeometryOperations.get_calculator("1")
   ↓
Returns: GeometryOperations.area_calculator
   ↓
area_calculator(content_frame) is called
   ↓
GUI displays input fields and calculate button
```

## Data Flow

### From User Interaction to Result

```
User Input
    ↓
    │ (Input validation)
    ↓
Calculation
    ↓
    │ (Error handling)
    ↓
Display Result
    ↓
    │ (Can do another operation or go back)
    ↓
Back to previous screen
```

## Module Structure (Each Module)

Every module follows this pattern:

```
YourModule.py
│
├── Import statements
│
├── class YourModuleOperations:
│   │
│   ├── OPERATIONS = {
│   │       "1": "Operation Name",
│   │       "2": "Another Operation",
│   │       ...
│   │   }
│   │
│   ├── @staticmethod
│   │   def operation_1_calculator(parent):
│   │       # Create UI
│   │       # Handle input
│   │       # Calculate result
│   │       # Display result
│   │
│   ├── @staticmethod
│   │   def operation_2_calculator(parent):
│   │       ...
│   │
│   └── @staticmethod
│       def get_calculator(operation_id):
│           calculators = {
│               "1": YourModuleOperations.operation_1_calculator,
│               "2": YourModuleOperations.operation_2_calculator,
│           }
│           return calculators.get(operation_id, None)
│
```

## How Calculator.py Orchestrates Everything

### 1. Initialization
```python
self.modules = {
    "1": ("Geometry and Trigonometry", GeometryOperations),
    "2": ("Probability and Combinatorics", ProbabilityOperations),
    "3": ("Sequences and Series", SequencesOperations),
    "4": ("Calculus", CalculusOperations),
    "5": ("Complex Numbers", ComplexNumbersOperations),
}
```

### 2. Module Selection
```python
for key, (name, module_class) in self.modules.items():
    # Create button for each module
    btn = tk.Button(
        text=name,
        command=lambda: self.show_module_menu(key, name, module_class)
    )
```

### 3. Operation Selection
```python
for op_key, op_name in module_class.OPERATIONS.items():
    # Create button for each operation
    btn = tk.Button(
        text=op_name,
        command=lambda: self.show_calculator(op_key, op_name, module_class)
    )
```

### 4. Calculator Display
```python
calculator = module_class.get_calculator(operation_id)
calculator(content_frame)  # Display the calculator UI
```

## Class Hierarchy

```
Calculator
├── MathCalculator (main GUI controller)
│   ├── show_home_screen()
│   ├── show_module_menu()
│   ├── show_calculator()
│   └── find_module_name()
│
└── Separate Module Files
    ├── GeometryOperations
    ├── ComplexNumbersOperations
    ├── SequencesOperations
    ├── CalculusOperations
    └── ProbabilityOperations
    
    Each with:
    ├── OPERATIONS (dict)
    ├── Multiple calculator methods (static)
    └── get_calculator() (static factory method)
```

## Screen Navigation Tree

```
                    Home Screen
                        │
        ┌───────────────┼───────────────┐
        │               │               │
      Geometry       Probability    Sequences
        │               │               │
    ┌───┴───┐       ┌───┴───┐       ┌──┴──┐
   Area  Pytha...  Combo  Permu...  Term  Sum
    │       │        │       │        │     │
   [Cal]  [Cal]    [Cal]   [Cal]   [Cal] [Cal]
    │       │        │       │        │     │
    └───────┴────────┴───────┴────────┴─────┘
             (Back button at each level)
```

## File Dependencies

```
Calculator.py (requires all below):
├── from Geometry import GeometryOperations
├── from ComplexNumbers import ComplexNumbersOperations
├── from Sequences import SequencesOperations
├── from Calculus import CalculusOperations
└── from Probability import ProbabilityOperations

Each Module:
├── import tkinter as tk
├── from tkinter import messagebox
├── (optional) import sympy as sp
└── (optional) import math
```

## State Management

### No Global State
- Each screen is self-contained
- Current frame is cleared before showing new screen
- No persistent data between operations (by design)

### User State Flow
```
Home Screen
    ↓
[User selects module]
    ↓
Module Operations List
    ↓
[User selects operation]
    ↓
Calculator UI
    ↓
[User enters data and clicks Calculate]
    ↓
Display Result
    ↓
[User can: Calculate again, Go back]
```

## Extension Points

### Adding a New Module
1. Create `NewModule.py`
2. Define `NewModuleOperations` class
3. Define `OPERATIONS` dictionary
4. Create calculator methods
5. Add `get_calculator()` method
6. Import in `Calculator.py`
7. Add to `self.modules` dictionary

### Adding a New Operation to Existing Module
1. Open module file (e.g., `Geometry.py`)
2. Add entry to `OPERATIONS` dictionary
3. Create calculator method
4. Add mapping in `get_calculator()`
5. Done! No changes to `Calculator.py` needed

### Customizing Appearance
1. Edit colors (search for `#4CAF50`, `#FF9800`, etc.)
2. Change fonts (search for `"Arial"`)
3. Adjust sizes (search for `.geometry()`)
4. Modify button heights/widths

## Error Handling Strategy

### Input Validation
```
User enters data
    ↓
try: Convert to appropriate type
except ValueError: Show error message "Invalid input"
    ↓
if value_invalid: Show error message with reason
    ↓
Calculate and display result
```

### Calculator-Specific Errors
```
- Empty input → ValueError caught
- Non-numeric input → ValueError caught
- Division by zero → ZeroDivisionError caught
- Sympy errors → Exception caught
```

## Performance Considerations

### Current Optimizations
- Tkinter (lightweight GUI framework)
- Static methods (no instance creation overhead)
- No unnecessary redraws
- Lazy loading (modules loaded only when needed)

### Future Optimizations
- Cache sympy compilations
- Parallel calculation for complex operations
- Result history/caching
- Custom plotting for visualizations

## Security Considerations

### Input Validation
- All numeric inputs validated
- Sympy expressions sanitized (when implemented)
- No file I/O
- No network requests

### Safe Defaults
- Operations are math-only
- No system calls
- No data persistence
- Clean exit handling

## Scaling Considerations

### Current Capacity
- 5 modules × ~10 operations each = 50+ calculators
- Easily supports this scale
- Navigation is intuitive at this level

### Future Scaling
- Could use tree view for deeply nested operations
- Could implement tabs for frequently used operations
- Could add favorites/bookmarks feature

---

## Summary

This architecture provides:
- ✅ Clean separation of concerns
- ✅ Easy to extend with new modules
- ✅ Easy to add operations to existing modules
- ✅ Single responsibility principle
- ✅ DRY (Don't Repeat Yourself) code
- ✅ Intuitive user navigation
- ✅ Minimal dependencies
