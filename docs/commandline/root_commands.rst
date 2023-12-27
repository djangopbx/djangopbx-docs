Commands Issued by the root user
==================================

This is a short list of commends that can be issued by the root user
to control parts of DjangoPBX.

uwsgi
------
If you have made changes to a DjangoPBX application or have upgraded
via git pull or otherwise then you will need to reload the **uwsgi** daemon.
Changes on the Python code will not take effect until you do this.

By default, there are two instances of uwsgi running.  One serves configuration data
to FreeSWITCH (fs_config) and the other serves the NGINX web server (djangopbx).

FreeSWITCH falls back to a port on the web server if the fs_config instance is unavailable
so reloading these one at a time will not affect the running of the switch.

If the update does not include changes to the XML handler ot the HTTAPI handler then
only the (djangopbx) instance will need to be reloaded.
::

 uwsgi <command> <PID>

 root@djangopbx.com:~# uwsgi --reload /var/run/uwsgi/app/fs_config/pid
 root@djangopbx.com:~# uwsgi --reload /var/run/uwsgi/app/djangopbx/pid


systemctl start freeswitch
----------------------------
Starts the FreeSWITCH daemon.
::

 root@djangopbx.com:~# systemctl start freeswitch


systemctl stop freeswitch
----------------------------
Stops the FreeSWITCH daemon.
::

 root@djangopbx.com:~# systemctl stop freeswitch
