
class commandValidationExceptions(Exception):
    pass

class commandValidation:
    def validateCommand(self,cmd,maxCmd):
        errors=[]
        if type(cmd)!=int:
            try:
                cmd=int(cmd)
                if cmd<0 or cmd>maxCmd:
                    errors.append("The command doesn't exist!")
        
            except ValueError:
                errors.append("The command can't be string!")
        if cmd=="":
            errors.append("The command can't be empty!")
            
        if len(errors):
            raise commandValidationExceptions(errors)
        
    