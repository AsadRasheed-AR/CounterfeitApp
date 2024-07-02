from flask import Flask, request

import numpy as np

from constants import NUM_PATCHES, SINGNATURE_TEMPLATES, SIGNATURE_DICT
from utils import split_and_plot_image, extract_serial, extract_print_year, extract_denomination, extract_signature
# from constants import PASS,FAIL
from validations import SerialTop_Validation, SerialBottom_Validation, Denomination_Validation, PrintYear_Validation, Governor_Validation

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Test Route
@app.route("/test")
def test_route():
    return "API working!"

@app.route("/verify", methods=['POST'])
def verify():
    image = request.files.get("img")

    # Example usage:
    img_parts = split_and_plot_image(image, NUM_PATCHES, show_images=False)

    """Extract and Show Features"""

    Serial_top = extract_serial(np.hstack((img_parts[4], img_parts[5])))
    Serial_Bottom = extract_serial(np.hstack((img_parts[12], img_parts[13])))
    print_year = extract_print_year(img_parts[11])
    denomination = extract_denomination(np.hstack((img_parts[16], img_parts[17])))
    Governor_name = extract_signature(np.hstack((img_parts[7], img_parts[8])), SINGNATURE_TEMPLATES, SIGNATURE_DICT, show_image= False)
    # Serial_top, Serial_Bottom, print_year, denomination, Governor_name

    print(f"Top Serial Number = {Serial_top.upper()}")
    print(f"Bottom Serial Number = {Serial_Bottom.upper()}")
    print(f"Printing Year = {print_year}")
    print(f"Denomination = {denomination}")
    print(f"Governor SBP = {Governor_name}")

    if Serial_top.lower() == None or Serial_Bottom.lower() == None or (Serial_top.lower() != Serial_Bottom.lower()):
        return {
            "response" : "Please provide a clear picture of the bank note."
        }
    else:
        # Features = [
        #         [PASS['RESP_TOP_SERIAL'] if Serial_top.lower() != None else FAIL['RESP_TOP_SERIAL']],
        #         [PASS['RESP_BOTTOM_SERIAL'] if Serial_Bottom.lower() != None else FAIL['RESP_BOTTOM_SERIAL']],
        #         [PASS['RESP_PRINT_YEAR'] if print_year != None else FAIL['RESP_PRINT_YEAR']],
        #         [PASS['RESP_DENOMINATION'] if denomination != None else FAIL['RESP_DENOMINATION']],
        #         [PASS['RESP_GOVERNOR'] if (Governor_name != None and Governor_name != 'No signatures found.') else FAIL['RESP_GOVERNOR']],
        #     ]
        count = 0
        Features = [
                SerialTop_Validation(Serial_top.upper()),
                SerialBottom_Validation(Serial_Bottom.upper()),
                PrintYear_Validation(print_year),
                Denomination_Validation(denomination),
                Governor_Validation(Governor_name)
            ]
        return {
            "Features": Features,
            "Score_Total" : len(Features),
            "Score": sum(1 for feature in Features if feature['value'] is not None)
        }
        # return {
        #     "Top Serial" : Serial_top.upper(),
        #     "Bottom Serial": Serial_Bottom.upper(),
        #     "Print Year": print_year,
        #     "Denomination": denomination,
        #     "Governor Name": Governor_name
        # }

if __name__ == '__main__':   
    app.run(debug=True)