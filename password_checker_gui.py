import tkinter as tk

root = tk.Tk()
root.title("Password Checker")
root.geometry("350x200")

entry = tk.Entry(root, show="*", width=25)
entry.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=20)

def check_password():
    pwd = entry.get()  # pwd means password
    errors = []

    if len(pwd) < 8:
        errors.append("Too short")
    if not any(c.isupper() for c in pwd):
        errors.append("No uppercase")
    if not any(c.islower() for c in pwd):
        errors.append("No lowercase")
    if not any(c.isdigit() for c in pwd):
        errors.append("No number")
    if not any(not c.isalnum() for c in pwd):
        errors.append("No special char")

    if errors:
        result_label.config(
            text="❌ " + ", ".join(errors),
            fg="red"
        )
    else:
        result_label.config(
            text="✅ Strong password!",
            fg="green"
        )

check_btn = tk.Button(root, text="Check Password", command=check_password)
check_btn.pack()

root.mainloop()
