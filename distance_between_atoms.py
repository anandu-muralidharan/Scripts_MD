from ase.io import read
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
import numpy as np

# === GUI File Picker ===
Tk().withdraw()  # Hide the root window
xdatcar_path = filedialog.askopenfilename(
    title="Select the XDATCAR file",
    filetypes=[("XDATCAR files", "XDATCAR*"), ("All files", "*.*")]
)

if not xdatcar_path:
    raise Exception("No file selected.")

print(f"Selected XDATCAR: {xdatcar_path}")

# === SETTINGS ===
zn_index = 144  # Zn atom index (0-based)
n_index = 40    # N atom index (0-based)

# === READ TRAJECTORY ===
frames = read(xdatcar_path, index=':')
print(f"Loaded {len(frames)} frames")

# === COMPUTE DISTANCES ===
distances = [
    atoms.get_distance(zn_index, n_index, mic=True)
    for atoms in frames
]
mean_distance = np.mean(distances)

# === PLOT RESULTS ===
plt.figure(figsize=(8, 4))
plt.plot(distances, label=f'Distance: Zn[{zn_index}] – N[{n_index}]')
plt.axhline(mean_distance, color='red', linestyle='--', label=f'Mean: {mean_distance:.2f} Å')
plt.xlabel('Frame')
plt.ylabel('Distance (Å)')
plt.title(f'Zn–N Distance Over AIMD Simulation\nMean = {mean_distance:.2f} Å')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
