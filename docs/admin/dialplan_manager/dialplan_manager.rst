******************
Dialplan Manager
******************

The **Dialplan Manager** is the place to create, edit and delete dialplans.

The XML dialplan is the default dialplan used by FreeSwitch. XML is easily edited
by hand without requiring any special tools, and the dialplan edit screen provides a
simple XML editor you to use.

The dialplan as a whole is created from small individual **Dialplans** that work together to
provide a very flexible way of routing calls.

When a new domain (tenant) is created, a default set of dialplans are also created for that domain.
These can be edited or removed to suit the specific requirements of that domain.

Dialplans are separated into **contexts** that closely follow the name of the tenant or domain.
There are also **public** and **global** contexts.
Technically there is not a **global** context but rather a subset of dialplans that specify the 
**${domain_name}** channel variable as their context.  We will discuss this in a later section.

The creation of dialplans for **Inbound Routes**, **Outbound Routes** and **Time Conditions** are managed
from the :doc:`/portal/call_routing/call_routing` menu in the :doc:`/portal/portal`.


.. toctree::
  :maxdepth: 2

  dialplan_list.rst
  dialplan_edit.rst
  milliwatt_dialplan.rst
  dialplan_categories.rst
