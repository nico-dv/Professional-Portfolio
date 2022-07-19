from sqlite3 import converters
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import sys
import os
from pdf import pdf_converter
from tempfile import gettempdir
import subprocess

session = Session(profile_name="default")
polly = session.client("polly")


try:
    response = polly.synthesize_speech(Text=pdf_converter(), OutputFormat="mp3", VoiceId="Carmen")

except (BotoCoreError, ClientError) as error:
    print(error)
    sys.exit(-1)


if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
           output = os.path.join(gettempdir(), "speech.mp3")

           try:
                with open(output, "wb") as file:
                   file.write(stream.read())
           except IOError as error:
              print(error)
              sys.exit(-1)
else:
   
    print("Could not stream audio")
    sys.exit(-1)


if sys.platform == "win32":
    os.startfile(output)
else:
    
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output])