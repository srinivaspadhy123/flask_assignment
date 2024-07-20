import json
class RecordNotFoundException(Exception):

    def __init__(self,status,error,message):
        self.status = status
        self.error = error
        self.message = message

    def __str__(self) -> str:

        return json.dumps({
            'status':self.status,
            'error':self.error,
            'message':self.message
        })

    def to_dict(self):

        return{
            'status':self.status,
            'error':self.error,
            'message':self.message
        }
    
def build_exception_response(error):
    return ({
        "status":500,
        "error":"Internal Server Error",
        "message": error
    })
