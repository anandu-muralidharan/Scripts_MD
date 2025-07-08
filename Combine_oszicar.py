import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pathlib import Path

def get_oszicar_files(num_files):
    root = tk.Tk()
    root.withdraw()
    oszicar_files = []
    for i in range(num_files):
        file_path = filedialog.askopenfilename(title=f"Select OSZICAR file #{i+1}")
        if not file_path:
            messagebox.showerror("Error", "File selection cancelled.")
            return []
        oszicar_files.append(file_path)
    return oszicar_files

def get_save_location():
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(
        title="Save Combined OSZICAR As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    return save_path

def combine_oszicars_with_gui():
    root = tk.Tk()
    root.withdraw()

    try:
        num_files = simpledialog.askinteger(
            "How Many Files?",
            "Enter the number of OSZICAR files to combine:",
            minvalue=2,
            maxvalue=50
        )
    except:
        messagebox.showerror("Error", "Invalid input.")
        return

    if not num_files:
        return

    file_paths = get_oszicar_files(num_files)
    if not file_paths:
        return

    output_file = get_save_location()
    if not output_file:
        return

    all_lines = []
    step_offset = 0

    for i, path in enumerate(file_paths):
        with open(path, 'r') as f:
            lines = f.readlines()

        adjusted_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) > 0 and parts[0].isdigit():
                try:
                    old_step = int(parts[0])
                    new_step = old_step + step_offset
                    new_line = line.replace(parts[0], str(new_step), 1)
                    adjusted_lines.append(new_line)
                except ValueError:
                    adjusted_lines.append(line)
            else:
                adjusted_lines.append(line)

        all_lines.extend(adjusted_lines)

        # Estimate how many steps this file had (look at highest step)
        last_step = 0
        for line in lines[::-1]:
            if line.strip().split() and line.strip().split()[0].isdigit():
                last_step = int(line.strip().split()[0])
                break
        step_offset += last_step

    with open(output_file, 'w') as fout:
        fout.writelines(all_lines)

    messagebox.showinfo("Success", f"✅ Combined OSZICAR saved to:\n{output_file}")

# --- Run the script ---
if __name__ == "__main__":
    combine_oszicars_with_gui()
