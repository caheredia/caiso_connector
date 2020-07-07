import os


def generate_url(start_time: str, end_time: str) -> str:
    """Generates a CAISO OASIS url based on start and time.

    Parameters
    ----------
    start_time : str
        start timestamp
    end_time : str
        end timestamp

    Returns
    -------
    target_url: str
        OASIS url for download
    """

    base_url = "http://oasis.caiso.com/oasisapi/SingleZip"
    query = "?queryname=PRC_LMP"
    time_range = f"&startdatetime={start_time}-0000&enddatetime={end_time}-0000"
    version = "&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"

    target_url = base_url + query + time_range + version
    return target_url

