# Minecraft Server Scanner
A non-harmful IP scanner intended for use in locating the Liveoverflow server.

# How did I find these IPs?
While I won't share exactly how I located these IPs, I will tell you a bit about getting them. My first task at hand was finding a range of IPs I could scan. I did this using a linux distribution known as Debian and the library masscan a super quick and reliable source to directly target a certain range. I won't share how I found the ranges, but if you are trying to keep in mind factors like his accent, any mentions of his whereabouts, etc. The 50 IPs provided are actual data as well and could help you locate the range.

# How does this program work?
The program initiates a connection with a free-to-use website that allows me to check the public statistics of a minecraft server. I ask which file of IPs it wants to check and establish an output method, then the program gets to work. The Liveoverflow server has some specifications for it and we can take those to create a scoring system as you may see. This allows has to better organize what to check first. The higher the score the more credientials it meets to matching the server we are looking for.

# Example Program Execution
```
Output files to external document?: "y"
Outputting all information to 'output.json'
Name of file to read IP addresses from... "sample.txt"
```
_Quotations represent information input by the user..._<br>
This would take all the IPs from the sample.txt file and will output the information into the 'output.json'. All these example files can be found here on the github.
