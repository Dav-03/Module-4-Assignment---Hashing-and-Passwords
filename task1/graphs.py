import csv
from pathlib import Path

import matplotlib.pyplot as plt

folder = Path(__file__).parent
results_file = folder / "final_results.csv"

bits = []
times = []
attempts = []


with open(results_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        bits.append(int(row["digest_bits"]))
        times.append(float(row["time_seconds"]))
        attempts.append(int(row["attempts"]))


# graph 1 Digest size vs collision time
plt.figure(figsize=(8, 5))
plt.plot(bits, times, marker="o")
plt.yscale("log")
plt.title("Truncated SHA-256 Digest Size vs Collision Time")
plt.xlabel("Digest size (bits)")
plt.ylabel("Collision time (seconds, log scale)")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(folder / "collision_time.png", dpi=300)
plt.close()


# graph 2 Digest size vs number of inputs
plt.figure(figsize=(8, 5))
plt.plot(bits, attempts, marker="o", color="orange")
plt.yscale("log")
plt.title("Truncated SHA-256 Digest Size vs Inputs Before Collision")
plt.xlabel("Digest size (bits)")
plt.ylabel("Number of inputs (log scale)")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(folder / "collision_inputs.png", dpi=300)
plt.close()

print("graph ran fine")