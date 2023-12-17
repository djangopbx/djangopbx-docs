Architecture
**************

**DjangoPBX** is written in `Python <https://www.python.org/>`_ using
the `Django Framework <https://www.djangoproject.com/>`_.

The main component is of course `FreeSWITCH <https://www.freeswitch.org/>`_ which
is a very powerful and highly scalable multi-platform voice and video switch.

`uWSGI <https://en.wikipedia.org/wiki/UWSGI/>`_ serves the DjangoPBX output to
both FreeSWITCH and an NGINX web server.

`PostgreSQL <https://www.postgresql.org/>`_ provides the database back end.

**All services** are protected by `nftables <https://nftables.org//>`_ which provides a
firewall that can be dynamically configured from within the DjangoPBX application.


.. toctree::
  :maxdepth: 3
  :glob:

  high_level_view.rst
