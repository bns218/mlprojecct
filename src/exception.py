import sys
<<<<<<< HEAD

def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in python script [{0}}] line number [{1}] error message [{2}]'.format(
    file_name,exc_tb.tb_lineno,str(error)
    return error_message

    )

class CustomExxception(Exception):
    def __init__(self,error_message,error_details:sys):
        super.__init(error_message)
        self.error_message=error_message_details(error_message,error_details=error_details)
    
    def __str__(self):
        return self.error_message
=======
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in python script [{0}}] line number [{1}] error message [{2}]'.format(
    file_name,exc_tb.tb_lineno,str(error))
    return error_message



class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    


  
    
>>>>>>> a9b94a26ee951cb1ba00f8e77dc00e1f4d64f3f4
