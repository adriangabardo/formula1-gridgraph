from calculate_session_performances import calculate_session_performances
from plot_for_driver import plot_for_driver

year = 2023
results = calculate_session_performances(year)

print("Finished")
print(results)

drivers_to_plot = ["HAM", "VER", "NOR", "LEC", "SAI"]

for specific_driver in drivers_to_plot:
    plot_for_driver(
        season_results=results, year=year, specific_driver=specific_driver, save_to_file=True, display_figure=False
    )
