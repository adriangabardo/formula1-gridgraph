import argparse
from calculate_session_performances import calculate_session_performances
from plot_for_driver import plot_for_driver


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Process Formula 1 season data.")
    parser.add_argument("--year", type=int, required=True, help="The year of the season to process")
    parser.add_argument(
        "--drivers", nargs="+", required=True, help="List of drivers to plot (e.g., HAM VER NOR LEC SAI)"
    )
    args = parser.parse_args()

    # Use the parsed year argument
    year = args.year
    results = calculate_session_performances(year)

    print("Finished")
    print(results)

    for specific_driver in args.drivers:
        plot_for_driver(
            season_results=results, year=year, specific_driver=specific_driver, save_to_file=True, display_figure=False
        )


if __name__ == "__main__":
    main()
