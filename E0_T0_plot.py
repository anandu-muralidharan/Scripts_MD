from pathlib import Path
from tkinter import Tk, filedialog
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

# Hide the main tkinter window
root = Tk()
root.withdraw()

# Open file dialog to select input file
input_file_path = filedialog.askopenfilename(title="Select input text file")

if not input_file_path:
    print("No file selected. Exiting.")
else:
    output_file = Path("file.txt")
    
    with open(input_file_path, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            if "T=" in line:
                outfile.write(line)

    abs_path = output_file.resolve()
    print("Output saved to:", abs_path)

with open(abs_path, "r") as file:
    data = file.read()

E0_string_values = re.findall(r'E0=\s+(\S+)', data)
E0_float_values = [float(x) for x in E0_string_values]

T0_string_values = re.findall(r'T=\s+(\S+)', data)
T0_float_values = [float(y) for y in T0_string_values]

data_E0 = []
for i in range(len(E0_float_values)):
    data_E0.append([i + 1, E0_float_values[i]])

data_T0 = []
for i in range(len(T0_float_values)):
    data_T0.append([i + 1, T0_float_values[i]])

# Create DataFrames
df_E0 = pd.DataFrame(data_E0, columns=["Step", "E0"])
df_T0 = pd.DataFrame(data_T0, columns=["Step", "T0"])

# Create the plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot E0 on the first y-axis
color = 'tab:blue'
ax1.set_xlabel("Step")
ax1.set_ylabel("E0 (Energy)", color=color)
ax1.plot(df_E0["Step"], df_E0["E0"], linestyle='-', color=color, label="E0")
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True)

# Create a second y-axis for T0
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel("T0 (Temperature)", color=color)
ax2.plot(df_T0["Step"], df_T0["T0"], linestyle='-', color=color, label="T0")
ax2.tick_params(axis='y', labelcolor=color)

# Title
plt.title("Variation of E0 and T0 with Steps")
fig.tight_layout()
plt.show()

os.remove(abs_path)
print(f"Deleted temporary file: {abs_path}")
