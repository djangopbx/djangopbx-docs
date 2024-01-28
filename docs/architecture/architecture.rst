##############
Architecture
##############

**DjangoPBX** is written in `Python <https://www.python.org/>`_ using
the `Django Framework <https://www.djangoproject.com/>`_.

The main component is of course `FreeSWITCH <https://www.freeswitch.org/>`_ which
is a very powerful and highly scalable multi-platform voice and video switch.

`uWSGI <https://en.wikipedia.org/wiki/UWSGI>`_ serves the DjangoPBX output to
both FreeSWITCH and a NGINX web server.

`PostgreSQL <https://www.postgresql.org/>`_ provides the database back end.

`RabbitMQ <https://www.rabbitmq.com/>`_ is used as a message broker for more advanced clustering operations.

**All services** are protected by `nftables <https://nftables.org/projects/nftables/index.html>`_ which provides a
firewall that can be dynamically configured from within the DjangoPBX application.


.. toctree::
  :maxdepth: 1

  high_level_view.rst
  db_schema.rst
  db_entity_relationship_diagram.rst
  firewall.rst
