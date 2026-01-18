# # below code is to check the logging config
# # from src.logger import logging

# # logging.debug("This is a debug message.")
# # logging.info("This is an info message.")
# # logging.warning("This is a warning message.")
# # logging.error("This is an error message.")
# # logging.critical("This is a critical message.")

# # --------------------------------------------------------------------------------

# # # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

# # --------------------------------------------------------------------------------

# from src.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()


# Using requests in Python after publishing sheet as CSV
import requests
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-.../pub?gid=0&single=true&output=csv'
response = requests.get(CSV_URL)
print(response.text)

