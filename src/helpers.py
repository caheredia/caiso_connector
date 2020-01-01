DATABASE_LOCATION = "src/lmp.db"
ZIP_DIRECTORY = 'src/temp_data'


BASE_URL = "http://oasis.caiso.com/oasisapi/SingleZip"
query_name = "?queryname=PRC_LMP"
time_range = "&startdatetime=20190201T00:00-0000&enddatetime=20190206T00:00-0000"
query_params = "&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
# build full caiso url
target_url = BASE_URL + query_name + time_range + query_params
