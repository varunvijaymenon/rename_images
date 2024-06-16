import re
from PIL import Image 
from pytesseract import pytesseract 
import os
import shutil
from os import listdir
from os.path import isfile, join

dest_dir = '/Users/varunvijay/dummy/renamed_files/{}.png'
src_dir = '/Users/varunvijay/dummy/Pride month SCIP SIGNATURES/SCIP PRIDE MONTH SIGNATURES/{}'
def find_emails(img_name, text):
    # List of email patterns to look for
    patterns = [r"\S+@\S+"]
     
    for pattern in patterns:
        # Compile the pattern
        email_regex = re.compile(pattern)
         
        # Find all instances of the pattern in the text
        emails = email_regex.findall(text)
        filename = emails[0].split("@")[0]

        shutil.copy(src_dir.format(img_name), dest_dir.format(filename))

def img_to_text(img_name):
    image_path = "/Users/varunvijay/dummy/Pride month SCIP SIGNATURES/SCIP PRIDE MONTH SIGNATURES/{}"
  
    #   Opening the image & storing it in an image object 
    img = Image.open(image_path.format(img_name))
    text = pytesseract.image_to_string(img) 
    find_emails(img_name, text[:-1])


onlyfiles = [f for f in listdir('/Users/varunvijay/dummy/Pride month SCIP SIGNATURES/SCIP PRIDE MONTH SIGNATURES') if f.lower().endswith(('.png'))]
for img_name in onlyfiles:
    img_to_text(img_name)

print('done')
# print(onlyfiles)
# print(len(onlyfiles))
# img_to_text('WhatsApp Image 2024-06-07 at 20.07.21.jpeg')