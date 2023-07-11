import tkinter as tk
import boto3
import os
import sys
from tempfile import gettempdir
from contextlib import closing
root=tk.Tk()
root.geometry("400x240")
root.title("T2S-Con Amazon Polly")
textExample=tk.Text(root,height=10)
textExample.pack()
def getText():
 # aws_mag_con=boto3.session.Session(profile_name='demo_user')
  '''client=aws_mag_con.client(service_name='polly',aws_access_key_id='AKIA3LK5XFYTSIUXFND6',secret_key='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', region_name='us-east-1')'''

  client = boto3.client('polly', aws_access_key_id='AKIA3LK5XFYTSIUXFND6', aws_secret_access_key='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', region_name='us-east-1')

  result=textExample.get("1.0","end")
  print(result)
  response= client.synthesize_speech(VoiceId='Joanna', OutputFormat='mp3',Text=result, Engine='neural')
  print(response)
  if "AudioStream" in response:
    with closing(response['AudioStream']) as stream:
      output=os.path.join(gettempdir(),"speech.mp3")
      try:
        with open(output,"wb") as file:
          file.write(stream.read())
      except IOError as error:
        print(error)
        sys.exit(-1)
  else:
      print("cloud not find the stream!")
      sys.exit(-1)
  if sys.platform=='win32':
      os.startfile(output)

btnRead=tk.Button(root,height=1,width=10,text="read",command=getText)
btnRead.pack()
root.mainloop()

