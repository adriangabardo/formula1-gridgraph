import fastf1


# Function to calculate the difference
def calculate_difference(row):
    lap1_position = row["Position"]
    grid_position = row["GridPosition"]
    if lap1_position < grid_position:
        return abs(
            grid_position - lap1_position
        )  # Positive difference if Lap 1 position is better (lower) than GridPosition
    else:
        return -(lap1_position - grid_position)  # Negative difference otherwise


def calculate_start_performances(year: int, gp: str | int, identifier: int | str | None = "R"):
    print(f"Getting session grid diff for - {year} - {gp} - {identifier}")

    session = fastf1.get_session(year, gp, identifier)
    session.load(laps=True)

    # Retrieve drivers grid positions
    grid_positions = session.results.GridPosition

    # Retrieve drivers end of lap 1 positions
    lap_1_end_positions = session.laps[session.laps["LapNumber"] == 1][["DriverNumber", "Driver", "Position"]]

    # Ensure DriverNumber is of the same type in both DataFrames for the merge
    grid_positions = grid_positions.rename_axis("DriverNumber").reset_index()

    # Merge GridPosition with Lap 1 positions
    merged_positions = lap_1_end_positions.merge(
        grid_positions, on="DriverNumber", suffixes=("_Lap1", "_Grid")
    ).sort_values(by="GridPosition")

    # Calculate the difference and add it to the DataFrame
    merged_positions["Difference"] = merged_positions.apply(calculate_difference, axis=1)

    return merged_positions
