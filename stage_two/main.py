"""
This module defines what will happen in stage_2.
"""
import requests
import pandas as pd
from datetime import datetime


def main() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(response.text)

    
    dt = datetime.now()
    df = pd.DataFrame({'time': [dt],
                   'action': ['Run Stage 2']})
    df.to_csv('data/logs.csv', mode='a', index=False, header=False)


if __name__ == "__main__":
    main()
