import subprocess, socket, os, re, smtplib, \
        logging, pathlib, json, time, shutil

def main():

  # capture wifi data
  with open('network_wifi.txt', 'a') as network_wifi:
    try:
      commands = subprocess.Popen(['ipconfig','ifconfig'], stdout=network_wifi, stderr=network_wifi, shell=True)
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




if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Program Exiting")