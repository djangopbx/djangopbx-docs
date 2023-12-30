*********
Tenants
*********

The **Tenants** application stores data related to the PBX User, **Domains** and
their associated settings.
There is a one-to-one mapping between the Django User and the PBX User.
The PBX User is represented by the Profile data shown in the **Profiles** section.

The **Tenants** application also stores **Settings** data in the following three
tables:

- **Default settings**:
    System-wide variables; their usage is determined by the setting category.

- **Domain settings**:
    Variables specific to an individual Domain. If any of these variables have the same name as a
    **Default settings** variable then these will take priority.  One Domain setting that you will
    often see is the **Menu**; this controls which menu is shown to anyone logging in to that Domain.

- **Profile settings**:
    Variables specific to an individual Profile. If any of these variables have the same name as a
    **Default settings** variable or **Domain settings** variable then these will take priority.


.. toctree::
  :maxdepth: 2

  domains.rst
  profiles.rst
  default_settings.rst

