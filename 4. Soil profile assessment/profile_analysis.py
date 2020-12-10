import requests
import json
import base64

# ----------------------------------------------------------------------------
# 1. FUNCTION TO CREATE IMAGE (ONLY DEFINE ONCE IN YOUR PROJECT)
# ----------------------------------------------------------------------------

def create_image(filename,image_png,image_pdf):
    image_bytes = image_png.replace("'", '""').encode('utf8')
    with open(filename+".png", "wb") as fh:
        fh.write(base64.decodebytes(image_bytes))
    image_bytes = image_pdf.replace("'", '""').encode('utf8')
    with open(filename+".pdf", "wb") as fh:
        fh.write(base64.decodebytes(image_bytes))
    return()

# ----------------------------------------------------------------------------
# 2. FUNCTION TO CREATE LOGFILE (ONLY DEFINE ONCE IN YOUR PROJECT)
# ----------------------------------------------------------------------------

def create_logfile(filename,log_string):
    with open(filename+".txt", "w") as fh:
        fh.write(log_string)
    return()

# ----------------------------------------------------------------------------
# 3. LOGIN (ONLY REQUIRED ONCE IN YOUR PROJECT)
# ----------------------------------------------------------------------------

# 3.1 Define login requirement
url = "https://be-mole.herokuapp.com/"
username = 'FILL IN USERNAME HERE'
password = 'FILL IN PASSWORD HERE'

# 3.2 Login
login = requests.post(url+"login",json={"username":username,"password":password})
print(login.json()["message"]) # Can always be requested to check the API response

# 3.3 Validate access token
validate = requests.get(url+"validate",headers={"Authorization":"Bearer "+str(login.json()['access_token'])})
print(validate.json()["message"]) # Can always be requested to check the API response

# ----------------------------------------------------------------------------
# 4. PROFILE ANALYSIS
# ----------------------------------------------------------------------------

# 4.1 Data import
cpt_data = json.load(open('./input.json', 'r'))

# 4.2 Validate and analyse data
analysis = requests.post(url+"profile_analysis",json=cpt_data,headers={"Authorization":"Bearer "+str(login.json()['access_token'])})

# 4.3 Convert string to bytes value and save
create_image("output",analysis.json()["image_output_png"],analysis.json()["image_output_pdf"])
create_logfile("./logfile",analysis.json()["log_string"])
