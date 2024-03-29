import sys


def error_massage_details(error, error_details:sys):
   
   _, _, exc_tb=error_details.exc_info()

   file_name=exc_tb.tb_frame.f_code.co_filename

   error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

class SensorException(Exception):
    def __init__(self, error_massage,error_details:sys) :
        """
         "param error_massage: error massage in string format
        """
        super().__init__(error_massage)

        self.error_massage=error_massage_details(error_massage,error_details=error_details)
        
    def __str__(self):
       return self.error_massage    
