# Display & cronJob

This part of the SchoolPICluster runs in a cronJob to set the Display Data and manage everything with the Display...

> Please read the [pip.txt](pip.txt) file to know what packages you need.
> And also have python 13 installed on your system.

###### cronJob for every minute `* * * * *`
```bash

crontab -e

# Paste this in the crontab file
# * * * * * python3 /root/display/main.py

```