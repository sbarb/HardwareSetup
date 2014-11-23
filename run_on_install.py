import os

GOOGLE_CHROME_PACKAGE_NAME = "google-chrome-stable_current_amd64.deb"
GOOGLE_CHROME_PACKAGE_PATH = "~/$GOOGLE_CHROME_PACKAGE_NAME"
SCHOOL_STREAMER_URL = "http://socialdrizzle.com/univeristy-of-alabama-at-birmingham/s/jumbotron"
STARTUP_SCRIPT_PATH = "~/Desktop/Start-Drizzle.sh"

#installs/removes
# install chromium
os.system("sudo apt-get install chromium-browser")
# Install Chrome dependencies
os.system("sudo apt-get install libxss1 libappindicator1 libindicator7")
# download chrome's debian package
os.system("wget -O $GOOGLE_CHROME_PACKAGE_PATH "https://dl.google.com/linux/direct/$GOOGLE_CHROME_PACKAGE_NAME"")
# install the chrome package
os.system("sudo dpkg -i $GOOGLE_CHROME_PACKAGE_NAME")
# remove the google deb package that was downloaded and installed already
os.system("sudo rm -rf $GOOGLE_CHROME_PACKAGE_PATH")

# writes Start-Drizzle.sh to Desktop to open on boot
os.system("echo "#!/bin/bash \n
chromium-browser --kiosk ‘$SCHOOL_STREAMER_URL’" > $STARTUP_SCRIPT_PATH")

# change permissions on the startup script
os.system("chmod 755 $STARTUP_SCRIPT_PATH")

# autorun the startup script once the desktop is ready
os.system("mkdir -p ~/.config/autostart/directory/
echo "[Desktop Entry]
Type=Application
Exec=$STARTUP_SCRIPT_PATH" > ~/.config/autostart/directory/drizzle.desktop")
