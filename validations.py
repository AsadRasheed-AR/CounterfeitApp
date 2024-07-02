from constants import PASS,FAIL

def SerialTop_Validation(SerialNum):
    if SerialNum != None:
        ResponseTopSerial = PASS['RESP_TOP_SERIAL']
        ResponseTopSerial['value'] = SerialNum
        return ResponseTopSerial
    else:
        return FAIL['RESP_TOP_SERIAL']

def SerialBottom_Validation(SerialNum):
    if SerialNum != None:
        ResponseBottomSerial = PASS['RESP_BOTTOM_SERIAL']
        ResponseBottomSerial['value'] = SerialNum
        return ResponseBottomSerial
    else:
        return FAIL['RESP_BOTTOM_SERIAL']

def PrintYear_Validation(PrintYear):
    if PrintYear != None:
        ResponsePrintYear = PASS['RESP_PRINT_YEAR']
        ResponsePrintYear['value'] = PrintYear
        return ResponsePrintYear
    else:
        return FAIL['RESP_PRINT_YEAR']

def Denomination_Validation(Denomination):
    if Denomination != None:
        ResponseDenomination = PASS['RESP_DENOMINATION']
        ResponseDenomination['value'] = Denomination
        return ResponseDenomination
    else:
        return FAIL['RESP_DENOMINATION']

def Governor_Validation(Governor):
    if Governor != None and Governor != 'No signatures found.':
        ResponseGovernor = PASS['RESP_GOVERNOR']
        ResponseGovernor['value'] = Governor
        return ResponseGovernor
    else:
        return FAIL['RESP_GOVERNOR']

