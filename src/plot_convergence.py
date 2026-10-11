import matplotlib.pyplot as plt
import pandas as pd


def main():
    df = pd.read_csv("results/pricing_comparison.csv")

    crr = df[df["method"].str.startswith("CRR")].copy()
    crr["steps"] = crr["method"].str.extract(r"(\d+)").astype(int)

    mc = df[df["method"].str.startswith("Monte Carlo")].copy()
    mc["simulations"] = (
        mc["method"].str.extract(r"(\d+)").astype(int)
    )

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].plot(crr["steps"], crr["absolute_error"], marker="o")
    axes[0].set_xscale("log")
    axes[0].set_yscale("log")
    axes[0].set_title("CRR: Absolute Pricing Error")
    axes[0].set_xlabel("Number of steps")
    axes[0].set_ylabel("Absolute error")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(
        mc["simulations"], mc["standard_error"], marker="o"
    )
    axes[1].set_xscale("log")
    axes[1].set_yscale("log")
    axes[1].set_title("Monte Carlo: Standard Error")
    axes[1].set_xlabel("Number of simulations")
    axes[1].set_ylabel("Standard error")
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig("results/pricing_convergence.png", dpi=200)
    print("Saved results/pricing_convergence.png")
    plt.show()


if __name__ == "__main__":
    main()
