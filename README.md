# rpi_hc12

**University of Maine BioSensors**
*Samuel Swope*

Description:
This project is used to record data received by the HC-12-USB
and store it on the RaspberryPi. The code for this separates the
incoming data from the different transmitters and puts each in 
their own file. For example, having two transmitters with the 
IDs of 3W and 1C, their respective data files are 3W.txt and
1C.txt. Each reading will also be time stamped, following the
format of: Year-Month-Day,Hour:Min:Sec.

Specifications:
This program is tested in Python 2.7, so their may be errors with 
newer versions. The serial port is reading with default settings
and a baud rate of 9600bps. The program has been tested on a
RaspberryPi 3B+. 

Instructions: 
Ensure that SQLite3 is installed. To do this run *sudo apt-get
install sqlite3*

Notes:
If there are any problems with the code, email me at
samuel.swope@maine.edu.
