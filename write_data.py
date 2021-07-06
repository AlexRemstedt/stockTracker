"""Writes data to excel file."""
from typing import Any, List
import pandas as pd
from datetime import datetime

from get_data import Share

today = datetime.now().strftime('%d/%m/%Y')


def get_request_data(code: str, request_data: List[str]) -> Any:
    """Get data from iex-cloud.

    :param code: Code name of company
    :param request_data: list with datapoints which are needed
    :return: Requested data
    """
    share = Share(code)
    all_data = share.get_data()
    specific_data = [all_data[i] for i in request_data]
    return specific_data


def write_data(xls_path: str, code: str, data: List[str]) -> None:
    """Write data to excel file.

    :param xls_path: path to excel file
    :param code: Code name of company
    :param data: data that needs to be added to excel
    """
    original = pd.read_excel(xls_path, code)
    if today not in original.columns:
        original[today] = data
        original.to_excel(xls_path, code, index=False)
        return f"data added to {code}"
    return "already got data today"


with pd.ExcelFile('shares.xlsx') as xlsx:
    shares = xlsx.sheet_names
    for share in shares:
        vars = pd.read_excel('shares.xlsx',
                             sheet_name=share)['dates'].tolist()
        new_data = get_request_data(share, vars)
        check = write_data('shares.xlsx', share, new_data)
        print(check)
