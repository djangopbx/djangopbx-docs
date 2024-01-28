**********************************
Commands to use when Upgrading
**********************************

This is a short list of commands that can be issued by the root user
and the django-pbx user when upgrading your DjangoPBX installation.

In most cases an update can be achieved with a simple git pull.
You **MUST** be logged in as the djangp-pbx user when issuing git commands.
The git pull will bring down any new or modified files.

There will be occasions where a git pull will identify a conflict.
Conflicts happen when you have modified one or more of the files in
or under the ~/pbx directory.  Of course it may not have been you that
physically made the modification, the installer modifies the settings.py file
to change keys and passwords.

Most conflicts will centre around the settings.py file, so it is advisable to
make a backup of this file before issuing a git pull commmand.

There may be some occasions when you may wish to backup your existing DjangoPBX,
clone a whole new copy and then edit the new settings.py file putting the keys
and passwords back in from the saved settings.py file.
::

 mv ~/pbx ~/pbx_20240128
 git clone https://github.com/djangopbx/djangopbx.git pbx


These are the key lines in ~/pbx/pbx/setttings.py that you may need to edit.
Do not run in production with DEBUG set to True.:
::

  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'django-insecure-aaabbbcccdddeeefff9876543210'

  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = True

  ALLOWED_HOSTS = ['*']

  # Database
  # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangopbx',
        'USER': 'djangopbx',
        'PASSWORD': 'postgres-insecure-abcdef9876543210',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    },
    'freeswitch': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'freeswitch',
        'USER': 'freeswitch',
        'PASSWORD': 'postgres-insecure-abcdef9876543210',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
  }

  # Uncomment for production
  # SESSION_COOKIE_AGE = 3600
  # SESSION_EXPIRE_AT_BROWSER_CLOSE = True


The Upgrade
-------------

Most of the time a simple git pull will suffice:
::

 cd ~/pbx
 git pull


If you do encounter a conflict, it can be resolved by using git stash.
Use git stash to save your local changes and then execute the git pull.
Then use git stash pop to get your stashed changes back.:
::

 cd ~/pbx
 git stash
 git pull
 git stash pop


The git commands update the DjangoPBX source code, but depending on what has changed,
there may be some additional steps to take, but they are very simple to do.

If changes have been made to the database schema, you will need to apply those changes
using the migrate tool:
::

 cd ~/pbx
 python3 manage.py migrate


If any static files for the webserver have been changed or added, for example a stylesheet
or a new javascript library, you will need to ensure these get moved to the web server using
the collectstatic tool:
::

 cd ~/pbx
 python3 manage.py collectstatic


Other DjangoPBX command line operations are detailed here:
:doc:`./django_management_commands`


Finally
---------
Logged in as the root user, issue the follow commands:
::

 uwsgi --reload /var/run/uwsgi/app/fs_config/pid
 uwsgi --reload /var/run/uwsgi/app/djangopbx/pid


