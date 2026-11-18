
import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        price = float(entry_price.get())
        discount = float(entry_discount.get())
        quantity = int(entry_quantity.get())

        if price < 0 or quantity <= 0:
            messagebox.showerror("Error", "Price must be non-negative and quantity must be positive!")
            return

        if discount < 0 or discount > 100:
            messagebox.showerror("Error", "Discount must be between 0 and 100!")
            return

        subtotal = price * quantity
        discount_amount = subtotal * (discount / 100)
        total_price = subtotal - discount_amount

        result_label.config(
            text=f"Subtotal: Rp {subtotal:,.2f}\n"
                 f"Discount: Rp {discount_amount:,.2f}\n"
                 f"Final Amount: Rp {total_price:,.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def reset():
    entry_price.delete(0, tk.END)
    entry_discount.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x450")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="DISCOUNT CALCULATOR",
    font=("Arial", 18, "bold")
).pack(pady=20)

# Price input
tk.Label(root, text="Item Price (Rp)").pack()
entry_price = tk.Entry(root, width=30)
entry_price.pack(pady=5)

# Discount input
tk.Label(root, text="Discount Rate (%)").pack()
entry_discount = tk.Entry(root, width=30)
entry_discount.pack(pady=5)

# Quantity input
tk.Label(root, text="Quantity").pack()
entry_quantity = tk.Entry(root, width=30)
entry_quantity.pack(pady=5)

# Calculate button
tk.Button(
    root,
    text="Calculate",
    command=calculate_discount,
    bg="#2563EB",
    fg="white",
    width=20
).pack(pady=15)

# Reset button
tk.Button(
    root,
    text="Reset",
    command=reset,
    width=20
).pack()

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)

# Run application
root.mainloop()
