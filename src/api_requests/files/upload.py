import requests
from pathlib import Path

path = str(Path.cwd().parent)

"""
  function to upload a file to gcloud storage
"""
# url is provided with upload_input_file function


def upload_file(url, file_path):
    # change the name of your input file if you want to try with another file
    files = {'file': open(file_path, 'rb')}

    headers = {
        "Content-Type": "multipart/form-data",
    }
    response = requests.put(url, files=files, headers=headers)

    return response.text
