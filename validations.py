# from constants import ValidationResponse
from constants import ValidationResponse

def SerialTop_Validation(SerialNum):
    ResponseTopSerial = ValidationResponse['RESP_TOP_SERIAL']
    if SerialNum != None:
        ResponseTopSerial['value'] = SerialNum
        ResponseTopSerial['status'] = True
        return ResponseTopSerial
    else:
        return ValidationResponse['RESP_TOP_SERIAL']

def SerialBottom_Validation(SerialNum):
    ResponseBottomSerial = ValidationResponse['RESP_BOTTOM_SERIAL']
    if SerialNum != None:
        ResponseBottomSerial['value'] = SerialNum
        ResponseBottomSerial['status'] = True
        return ResponseBottomSerial
    else:
        return ValidationResponse['RESP_BOTTOM_SERIAL']

def PrintYear_Validation(PrintYear):
    ResponsePrintYear = ValidationResponse['RESP_PRINT_YEAR']
    if PrintYear != None:
        ResponsePrintYear['value'] = PrintYear
        ResponsePrintYear['status'] = True
        return ResponsePrintYear
    else:
        return ValidationResponse['RESP_PRINT_YEAR']

def Denomination_Validation(Denomination):
    ResponseDenomination = ValidationResponse['RESP_DENOMINATION']
    if Denomination != None:
        ResponseDenomination['value'] = Denomination
        ResponseDenomination['status'] = True
        return ResponseDenomination
    else:
        return ValidationResponse['RESP_DENOMINATION']

def Governor_Validation(Governor):
    ResponseGovernor = ValidationResponse['RESP_GOVERNOR']
    if Governor != None and Governor != 'No signatures found.':
        ResponseGovernor['value'] = Governor
        ResponseGovernor['status'] = True
        return ResponseGovernor
    else:
        return ValidationResponse['RESP_GOVERNOR']

