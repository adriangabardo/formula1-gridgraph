import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from pandas import DataFrame
import os

custom_lines = [
    Line2D([0], [0], color="green", lw=2),
    Line2D([0], [0], color="red", lw=2),
    Line2D([0], [0], marker="D", color="w", markerfacecolor="C0", markersize=10),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="C1", markersize=10),
]


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
    differences = driver_results_df["Difference"]

    # Create the stem plot
    plt.figure(figsize=(12, 6))

    for race, grid_pos, lap_pos, diff in zip(races, grid_positions, lap_positions, differences):
        color = "green" if diff > 0 else "red"
        plt.plot(
            [grid_pos, lap_pos], [race, race], color=color
        )  # Draw a line between the grid position and lap position
        plt.plot(grid_pos, race, "D", color="C0")  # Plot the grid position
        plt.plot(lap_pos, race, "o", color="C1")  # Plot the lap position

    # Adding labels and title
    plt.xlabel("Position")
    plt.ylabel("Race")
    plt.title(f"{specific_driver} {year} - Grid Position vs. Lap 1 End Position")
    plt.xticks(rotation=0)  # Rotate race names for better readability
    plt.xlim(1, 21)  # Set x-axis limits from 1 to 20
    plt.xticks(range(1, 21))  # Ensure x-axis has ticks from 1 to 20
    # plt.legend(["Grid Position", "Lap 1 End Position"])

    # Custom legend
    plt.legend(custom_lines, ["Gained Positions", "Lost Positions", "Grid Position", "Lap 1 End Position"])

    plt.grid(visible=True)
    plt.tight_layout()

    if save_to_file:
        OUTPUT_DIR = f"./output/{year}"

        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        # Save the plot to a file
        plt.savefig(f"{OUTPUT_DIR}/{specific_driver}.png", dpi=300)

    if display_figure:
        plt.show()
