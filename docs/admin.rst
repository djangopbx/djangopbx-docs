Admin Interface
=================

One of the most powerful parts of Django is the **Admin** interface.
DjangoPBX utilises the Admin interface to provide access to all the
data models.  Each model represents a table in the database.

The Admin interface easily accommodates most of the DjangoPBX requirements
However a very few operations require a more process-centric interface
that abstracts away the implementation details of database tables and fields.
These actions are provided via the user portal interface.


.. toctree::
  :maxdepth: 3
  :glob:

  admin/overview.rst
  admin/accounts/bridges.rst
  admin/accounts/extensions.rst
  admin/accounts/gateways.rst
  admin/administration/log_entries.rst
