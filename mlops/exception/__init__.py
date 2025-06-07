import sys

class MLOpsException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys, stage: str = "Unknown Stage"):
        self.stage = stage
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
        super().__init__(f"[Stage: {self.stage}] {self.error_message}")

    @staticmethod
    def get_detailed_error_message(error: Exception, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        line_number = exc_tb.tb_lineno if exc_tb else -1
        return f"Error occurred in file [{file_name}] at line [{line_number}]: {str(error)}"

    def __str__(self):
        return self.error_message
