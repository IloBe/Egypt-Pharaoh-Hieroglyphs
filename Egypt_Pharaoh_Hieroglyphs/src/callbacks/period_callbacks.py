# src/callbacks/period_callbacks.py

"""
Local callbacks for the period page. All Inputs and Outputs are components
that are defined within a single page's layout.

This file is intentionally empty. All grid callback logic is now centralized
in src/main.py for robustness and clarity.

It is there for future scalability, like
"On the period pages only, add a special button that downloads the grid data as a CSV."
Then this new local callback has nothing to do with the global click-handling logic.
It is specific to the period pages. So, it provides prepared, correctly-placed "slots"
for future page-specific logic, making the project easier and safer to extend.
"""
