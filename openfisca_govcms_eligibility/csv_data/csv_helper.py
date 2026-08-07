"""Helper functions for working with CSV files in OpenFisca rules."""

import csv
import logging

import numpy as np
import pandas as pd

log = logging.getLogger(__name__)


def load_csv_file(file_path, header_column=None, column_map=None):
    """Load a CSV file into a DataFrame, dynamically skipping metadata rows.

    Args:
        file_path (Path): Path to the CSV file.
        header_column (str): A value expected anywhere in the header row.
            If provided, all rows before that row are skipped automatically, so
            source CSVs with title/metadata rows can be used without modification.
        column_map (dict): Optional mapping of source column names to the names
            expected by the codebase, applied after loading.
    """
    if not file_path.exists():
        log.error("File does not exist: %s", file_path)
        return None
    try:
        skip = 0
        if header_column:
            with open(file_path, newline="", encoding="utf-8-sig") as f:
                for i, row in enumerate(csv.reader(f)):
                    if header_column in [cell.strip() for cell in row]:
                        skip = i
                        break
                else:
                    log.error("Header column '%s' not found in %s", header_column, file_path)
                    return None
        df = pd.read_csv(file_path, skiprows=skip, encoding="utf-8-sig")
        if column_map:
            df = df.rename(columns=column_map)
    except Exception:
        log.exception("Error loading %s", file_path)
        return None
    else:
        return df


def filter_csv_data(data_frame, people, period, result_key, result_is_array, filter_keys):  # noqa: PLR0913
    """Filter the given DataFrame based on the provided filter criteria and return the specified column's values for each input combination.

    Args:
        data_frame (pandas.DataFrame): The DataFrame to be filtered.
        people (function): A function that returns an array of values for each key and period combination.
        period (str): The period for which the filter criteria should be applied.
        result_key (str): The column key for which the values should be retrieved.
        result_is_array (bool): A flag indicating whether the result should be returned as an array or a single value.
        filter_keys (list): A list of column keys to be used as filter criteria.

    Returns:
        list: A list containing the specified column's values for each input combination.
    """
    if data_frame is None:
        # return an empty array if the DataFrame is not loaded the size of the people array
        return [""] * people.count
    # Initialize a list to store the results for each combination
    results = []

    # Create the filter arrays using the `people` object
    filter_arrays = [people(key, period) for key in filter_keys]

    # Loop through each combination of values in the input arrays
    for values in zip(*filter_arrays):
        # Create the filter criteria for the current combination of filter values
        filtered_criteria = True
        for key, value in zip(filter_keys, values):
            # Update the filter criteria based on the current key and value
            filtered_criteria &= data_frame[key] == value

        # Filter the DataFrame based on the current combination of values
        filtered_df = data_frame.loc[filtered_criteria]

        # Retrieve the specified column's value for the first match
        if not filtered_df.empty:
            result_values = filtered_df[result_key].to_numpy() if result_is_array else filtered_df[result_key].to_numpy()[0]
        # Handle case where no match is found
        elif result_is_array:
            result_values = ["no_results"]
        else:
            result_values = "no_results"

        # Append the result to the results list
        results.append(result_values)

    # The results array now contains the specified column's values for each input combination
    if result_is_array:
        # return the results as a array of comma separated strings
        results = [",".join(map(str, result)) for result in results]

    return results


def value_exists_in_csv(data_frame, people, period, key):
    """Check if a value exists in a given column of a filtered DataFrame.

    Args:
        data_frame (pd.DataFrame): The DataFrame containing the CSV data.
        people (list): List of people to filter by.
        period (str): The period to filter by.
        key (str): The column name to check the value in.

    Returns:
        bool: True if the value exists in the column, False otherwise.
    """
    # Ensure the DataFrame has the necessary columns
    if key not in data_frame.columns:
        msg = f"The DataFrame must contain '{key}' column."
        raise ValueError(msg)

    # Check if each person's value exists in the key column (vectorial)
    return np.isin(people(key, period), data_frame[key].to_numpy())
