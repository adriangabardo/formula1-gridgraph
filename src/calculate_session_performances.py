import fastf1
from pandas import DataFrame, concat
from calculate_start_performances import calculate_start_performances
from concurrent.futures import ThreadPoolExecutor, as_completed

import pickle
import os

CACHE_DIR = "cache"


def save_cache(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_cache(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return None


def calculate_session_performances(year: int):
    # Define the cache file name
    cache_file = os.path.join(CACHE_DIR, f"calculate_session_performances_{year}.pkl")

    # Try to load cached results
    cached_results = load_cache(cache_file)
    if cached_results is not None:
        return cached_results

    schedule = fastf1.get_event_schedule(year, include_testing=False)

    all_results = DataFrame()

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=25) as executor:  # Adjust max_workers based on your needs
        for _, event in schedule.iterrows():
            event_name = event["EventName"]
            future = executor.submit(calculate_start_performances, event["EventDate"].year, event_name)
            result = future.result()

            # Add an EventName column to each result DataFrame
            result["EventName"] = event_name
            # Append the result to the all_results_df DataFrame
            all_results = concat([all_results, result], ignore_index=True)

    # Save the results to cache
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    print("Saving results to cache")
    save_cache(all_results, cache_file)

    print("Finished calculations")
    return all_results
