Auto Report Crontab Entries
=============================

Auto Reports rely on the crontab for the django-pbx user.
Typical additions made to the crontab file for Auto Reports are shown below:

::

 15 6 1 * * cd /home/django-pbx/pbx; python3 manage.py timedreport --frequency month > /dev/null 2>&1
 30 6 * * 1 cd /home/django-pbx/pbx; python3 manage.py timedreport --frequency week > /dev/null 2>&1
 45 6 * * * cd /home/django-pbx/pbx; python3 manage.py timedreport --frequency day > /dev/null 2>&1
 # Uncomment below if hourly reports are really needed.
 #0 9-17 * * * cd /home/django-pbx/pbx; python3 manage.py timedreport --frequency hour > /dev/null 2>&1



The file is called **crontab** and is located in the django-pbx home directory: :file:`/home/django-pbx/crontab`
Any changes made to this file will not take effect until the following Operating System command is issued:

::

 django-pbx@myserver:~$ crontab crontab
