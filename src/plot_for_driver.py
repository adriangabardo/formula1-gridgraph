import matplotlib.pyplot as plt
from pandas import DataFrame
import os


def plot_for_driver(
    season_results: DataFrame,
    specific_driver: str,
    year: int,
    save_to_file: bool = False,
    display_figure: bool = False,
):
    driver_results_df = season_results[season_results["Driver"] == specific_driver]

    # Extract the necessary data
    races = driver_results_df["EventName"]
    grid_positions = driver_results_df["GridPosition"]
    lap_positions = driver_results_df["Position"]

    # Create the stem plot
    plt.figure(figsize=(12, 6))

    plt.stem(races, grid_positions, linefmt="C0-", markerfmt="D", basefmt=" ", bottom=1, orientation="horizontal")
    plt.stem(races, lap_positions, linefmt="C1-", markerfmt="C1o", basefmt=" ", bottom=1, orientation="horizontal")

    # Adding labels and title
    plt.xlabel("Position")
    plt.ylabel("Race")
    plt.title(f"Grid Position vs. Lap 1 Position for {specific_driver} - {year} Season")
    plt.xticks(rotation=0)  # Rotate race names for better readability
    plt.xlim(1, 20)  # Set x-axis limits from 1 to 20
    plt.xticks(range(1, 21))  # Ensure x-axis has ticks from 1 to 20
    plt.legend(["Grid Position", "Lap 1 End Position"])
    plt.grid(True)
    plt.tight_layout()

    if save_to_file:
        OUTPUT_DIR = f"./output/{year}"

        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        # Save the plot to a file
        plt.savefig(f"{OUTPUT_DIR}/{specific_driver}.png", dpi=300)

    if display_figure:
        plt.show()
