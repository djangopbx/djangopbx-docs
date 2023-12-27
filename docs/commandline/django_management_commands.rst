DjangoPBX Management Commands
===============================

**django-admin** is Django’s command-line utility for administrative tasks.
Whilst django-admin is on the system path and can be used in most circumstances,
the preferred command method for DjangoPBX is to use **manage.py**.
**manage.py** is located in the DjangoPBX project directory. **manage.py** does the
same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable
so that it points to the DjangoPBX project’s settings.py file.

**Usage:**
::

 cd ~/pbx
 python3 manage.py <command> [options]


changepassword
----------------
Allows changing a user’s password.
It prompts you to enter a new password twice for the given user.
::

 changepassword <username>

 django-pbx:~/pbx$ python3 manage.py changepassword 201@test1.djangopbx.com


createsuperuser
----------------
Creates a superuser account (a user who has all permissions).
This is useful if you need to create an initial superuser account
or if you need to add more superuser accounts.
::

 django-pbx:~/pbx$ python3 manage.py createsuperuser


createpbxdomain
----------------
Creates a tenant domain and optionally assigns a user to it.
The created domain will automatically have the default menu assigned,
and a default set of dialplans created.
::

 createpbxdomain --domain <domain name> [--user <user numeric Id>]

 django-pbx:~/pbx$ python3 manage.py createpbxdomain --domain test1.djangopbx.com --user 23


createpbxuser
----------------
Creates a user and assigns it to a domain.
::

 createpbxuser --domain <domain name>
               --username <username>
               --password <pass>
               --firstname <given name>
               --lastname <family name>
               --email <email address>

 django-pbx:~/pbx$ python3 manage.py createpbxuser --domain test1.djangopbx.com \
               --username 201@test1.djangopbx.com \
               --password verystrongpass \
               --firstname Adrian \
               --lastname Fretwell \
               --email adrian@djangopbx.com


collectstatic
---------------
Collects the static files (.css, icons etc.) from the various DjangoPBX applications
into the :file:`/var/www/static` directory.
::

 django-pbx:~/pbx$ python3 manage.py collectstatic


dialplandefaults
------------------
Installs or rebuilds the dial plans for the domain specified.

**Add or update dialplans**
::

 django-pbx:~/pbx$ python3 dialplandefaults --domain test1.djangopbx.com

**Add dialplans removing existing first**
::

 django-pbx:~/pbx$ python3 dialplandefaults --remove --domain test1.djangopbx.com


dumpdata
----------
Extracts data from application tables.
The dumpdata command can be used to generate input for loaddata_.
::

 django-pbx:~/pbx$ python3 manage.py dumpdata <app_name>.<table> --indent 4 > <destination file>

**Below are some examples of using dumpdata:**

Dump Default Settings to the /tmp directory
::

 django-pbx:~/pbx$ python3 manage.py tenants.defaultsetting --indent 4 > /tmp/default_settings.json


Create fixtrue data files for Menu Items
::

 django-pbx:~/pbx$ python3 manage.py portal.menuitem --indent 4 > portal/fixtures/memuitem.json
 django-pbx:~/pbx$ python3 manage.py portal.menuitemgroup --indent 4 > portal/fixtures/memuitemgroup.json


.. _loaddata:

loaddata
----------
The following will load the modules' fixture data for the switch application:
::

 django-pbx:~/pbx$ python3 manage.py loaddata --app switch modules.json


menudefaults
--------------
Run this command after installing a new application to your DjangoPBX.
Adds in menu items to the default menu if they do not exist.
If used with the --remove option the existing default menu will be removed
before new items are added.
::

 django-pbx:~/pbx$ python3 manage.py menudefaults [--remove <true>]


migrate
---------
Run this command after upgrading your DjangoPBX source for performing a git pull.
Synchronises the database schema and state with the current set of models and migrations.
::

 django-pbx:~/pbx$ python3 manage.py migrate


reinstatefwsipcustomerlist
----------------------------
Run this command after a reboot or after reloading the firewall.
This command reads all the IP addresses in the Switch IP Register.  All addresses
With a status of **current** are added to the firewall SIP customer list.
::

 django-pbx:~/pbx$ python3 manage.py reinstatefwsipcustomerlist


sipprofiledefaults
--------------------
Loads default SIP Profiles.
If used with the --remove option the existing default SIP Profiles will be removed
before new items are added.
::

 django-pbx:~/pbx$ python3 manage.py sipprofiledefaults [--remove <true>]


vardefaults
--------------------
Loads default Switch variables.
If used with the --remove option the existing switch variables will be removed
before new items are added.
::

 django-pbx:~/pbx$ python3 manage.py vardefaults [--remove <true>]


