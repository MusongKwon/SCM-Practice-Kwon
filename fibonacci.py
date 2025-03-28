import tkinter as tk

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def generate_fibonacci():
    n = int(entry.get())
    result_label.config(text=str(fibonacci(n)))

root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("400x300")

instruction_label = tk.Label(root, text="Enter the number of Fibonacci numbers to generate:")
instruction_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Enter", command=generate_fibonacci)
generate_button.pack(pady=5)

result_label = tk.Label(root, text="", wraplength=350, justify="center")
result_label.pack(pady=10)

root.mainloop()
