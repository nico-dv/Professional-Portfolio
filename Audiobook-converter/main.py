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


