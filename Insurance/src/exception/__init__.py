import sys
import logging


def get_error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file '{file_name}' at line {line_number}: {str(error)}"
    logging.error(error_message)
    return error_message


class MyException(Exception):
    def __init__(self, error_message, error_detail):
        detailed_message = get_error_message_detail(error_message, error_detail)
        super().__init__(detailed_message)
        self.error_message = detailed_message

    def __str__(self):
        return self.error_message
