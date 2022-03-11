"""
This module defines what will happen in stage_2.
"""
from datetime import datetime
import os
import requests
import pandas as pd




def main() -> None:
    """
    Dummy function to print to a csv file
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response.text)
    curr_dir = os.getcwd()
    print(curr_dir)
    timestamp = datetime.now()
    log_df = pd.read_csv('../data/logs.csv')
    print(log_df)
    print(timestamp)


if __name__ == "__main__":
    main()
