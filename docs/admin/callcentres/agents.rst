Agents
========

**Agents** are the members or people who will take calls distributed to then by the
Call Centre Queues.

.. image:: ../../_static/images/admin/callcentres/agents_list.jpg
        :scale: 85%


The Edit Screen
~~~~~~~~~~~~~~~~~

The **Agent** edit screen show the setting for an Agent.
Agents have Status and States. The Status is the general state of the agent
set by Logging In or Out, whilst States are dynamic and are updated by the system
based on the progress of a agent in a call.

.. image:: ../../_static/images/admin/callcentres/agent_edit.jpg
        :scale: 85%



Agent Options
~~~~~~~~~~~~~~~~

Agent Name
""""""""""""

Name of the agent. When adding agents to a Queue, this is what describes the agent


User
""""""

Associates a system user with the call centre agent


Type
""""""
Two types are supported, **Callback** and **UUID Standby**. Callback will try to reach the agent via the contact
fields value. UUID Standby will try to directly bridge the call using the agent UUID.


Call Timeout
""""""""""""""

Time to ring the agent before deeming them unavailable.


Agent Id
""""""""""

An ID that can be used to log the agent in and out of the Call Centre.


Agent PIN
"""""""""""
PIN to log the agent into the call center. Not required if agent_authorized=true is set in the dialplan for \*22.


Contact
"""""""""

A List/Edit to select which extension should be used to contact the Agent.


Status
""""""""

Sets the default status for the agent in the Call Centre


No Answer Delay Time
""""""""""""""""""""""

The time the system will wait to attempt a call to the agent again if they did not answer within the **Call Timeout** time.


Max No Answer
"""""""""""""""

Max attempts to call the agent. For example, when set to 1, if the agent does not answer within the first Call Timeout,
they will not get another chance to answer the call. If set to 2, the agent will have two attempts to answer the call.


Wrap Up Time
""""""""""""""

The amount of time after a ending call before the agent will be rung again.


Reject Delay Time
"""""""""""""""""""

If an agent rejects a call manually then this is the time to wait before a call is offered again.


Busy Delay Time
"""""""""""""""""

If the agent is on **Do Not Disturb**, the time to wait before trying them again.

