# Previously, install flask and pywhatkit
# Install them with pip3

import pywhatkit
from datetime import datetime
import time

seconds  = time.time() + 40
date     = datetime.fromtimestamp(seconds) 
pywhatkit.sendwhatmsg("+34xxxxxxxxx", "Hola _______, te estoy escribiendo desde un bot que he programado en python",
                       date.hour, date.minute)


