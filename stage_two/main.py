"""
This module defines what will happen in stage_2.
"""
from datetime import datetime
import requests
import pandas as pd
import os



def main() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response.text)
    CURR_DIR = os.getcwd()
    print(CURR_DIR)
    timestamp = datetime.now()
    log_df = pd.DataFrame({'time': [timestamp],
                   'action': ['Run Stage 2']})
    log_df.to_csv('data/logs.csv', mode='a', index=False, header=False)


if __name__ == "__main__":
    main()
