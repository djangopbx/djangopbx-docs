***********
DB Schema
***********

Key
=====
- 🔑 Primary Key
- 🔎 Index
- 🔍 Unique Index
- ⬋ Sort direction descending
- ⬈ Sort direction ascending
- \* Required field


Table public.auth_group
=========================

======= ==== ============
Idx     Name Data Type
======= ==== ============
\* 🔑 ⬋ id   serial
\* 🔍   name varchar(150)
======= ==== ============

**Indexes**

==== ============================= =======
Type Name                          On
==== ============================= =======
🔑   auth_group_pkey               ON id
🔍   auth_group_name_key           ON name
🔎   auth_group_name_a6ea08ec_like ON name
==== ============================= =======


Table public.auth_group_permissions
=====================================

======= ============= =========
Idx     Name          Data Type
======= ============= =========
\* 🔑   id            bigserial
\* 🔍 ⬈ group_id      integer
\* 🔍 ⬈ permission_id integer
======= ============= =========

.. _Indexes-1:

**Indexes**


+-----------------------+-------------------------------------------------------------+----------------------------+
| Type                  | Name                                                        | On                         |
+=======================+=============================================================+============================+
| 🔑                    | auth_group_permissions_pkey                                 | ON id                      |
+-----------------------+-------------------------------------------------------------+----------------------------+
| 🔍                    | auth_group_permissions_group_id_permission_id_0cd325b0_uniq | ON group_id, permission_id |
+-----------------------+-------------------------------------------------------------+----------------------------+
| 🔎                    | auth_group_permissions_group_id_b120cbf9                    | ON group_id                |
+-----------------------+-------------------------------------------------------------+----------------------------+
| 🔎                    | auth_group_permissions_permission_id_84c5c92e               | ON permission_id           |
+-----------------------+-------------------------------------------------------------+----------------------------+

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                    |
+=======================+===========================================================+=======================================================================================+
|                       | auth_group_permissions_group_id_b120cbf9_fk_auth_group_id | ( group_id ) ref `public.auth_group <#table-public-auth-group>`__ (id)                |
+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------+
|                       | auth_group_permissio_permission_id_84c5c92e_fk_auth_perm  | ( permission_id ) ref `public.auth_permission <#table-public-auth-permission>`__ (id) |
+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------+

Table public.auth_permission
============================

======= =============== ============
Idx     Name            Data Type
======= =============== ============
\* 🔑 ⬋ id              serial
\*      name            varchar(255)
\* 🔍 ⬈ content_type_id integer
\* 🔍   codename        varchar(100)
======= =============== ============

.. _Indexes-2:

**Indexes**


+-----------------------+--------------------------------------------------------+------------------------------+
| Type                  | Name                                                   | On                           |
+=======================+========================================================+==============================+
| 🔑                    | auth_permission_pkey                                   | ON id                        |
+-----------------------+--------------------------------------------------------+------------------------------+
| 🔍                    | auth_permission_content_type_id_codename_01ab375a_uniq | ON content_type_id, codename |
+-----------------------+--------------------------------------------------------+------------------------------+
| 🔎                    | auth_permission_content_type_id_2f476e4b               | ON content_type_id           |
+-----------------------+--------------------------------------------------------+------------------------------+

.. _foreign-keys-1:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                                              |
+=======================+=======================================================+=================================================================================================+
|                       | auth_permission_content_type_id_2f476e4b_fk_django_co | ( content_type_id ) ref `public.django_content_type <#table-public-django-content-type>`__ (id) |
+-----------------------+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+

Table public.auth_user
======================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           serial
\*      password     varchar(128)
\       last_login   timestamptz
\*      is_superuser boolean
\* 🔍   username     varchar(150)
\*      first_name   varchar(150)
\*      last_name    varchar(150)
\*      email        varchar(254)
\*      is_staff     boolean
\*      is_active    boolean
\*      date_joined  timestamptz
======= ============ ============

.. _Indexes-3:

**Indexes**


==== ================================ ===========
Type Name                             On
==== ================================ ===========
🔑   auth_user_pkey                   ON id
🔍   auth_user_username_key           ON username
🔎   auth_user_username_6821ab7c_like ON username
==== ================================ ===========

Table public.auth_user_groups
=============================

======= ======== =========
Idx     Name     Data Type
======= ======== =========
\* 🔑   id       bigserial
\* 🔍 ⬈ user_id  integer
\* 🔍 ⬈ group_id integer
======= ======== =========

.. _Indexes-4:

**Indexes**


+-----------------------+-------------------------------------------------+-----------------------+
| Type                  | Name                                            | On                    |
+=======================+=================================================+=======================+
| 🔑                    | auth_user_groups_pkey                           | ON id                 |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔍                    | auth_user_groups_user_id_group_id_94350c0c_uniq | ON user_id, group_id  |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔎                    | auth_user_groups_user_id_6a12ed8b               | ON user_id            |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔎                    | auth_user_groups_group_id_97559544              | ON group_id           |
+-----------------------+-------------------------------------------------+-----------------------+

.. _foreign-keys-2:

**Foreign Keys**


+-----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
| Type                  | Name                                                | On                                                                     |
+=======================+=====================================================+========================================================================+
|                       | auth_user_groups_user_id_6a12ed8b_fk_auth_user_id   | ( user_id ) ref `public.auth_user <#table-public-auth-user>`__ (id     |
+-----------------------+-----------------------------------------------------+------------------------------------------------------------------------+
|                       | auth_user_groups_group_id_97559544_fk_auth_group_id | ( group_id ) ref `public.auth_group <#table-public-auth-group>`__ (id) |
+-----------------------+-----------------------------------------------------+------------------------------------------------------------------------+

Table public.auth_user_user_permissions
=======================================

======= ============= =========
Idx     Name          Data Type
======= ============= =========
\* 🔑   id            bigserial
\* 🔍 ⬈ user_id       integer
\* 🔍 ⬈ permission_id integer
======= ============= =========

.. _Indexes-5:

**Indexes**


+-----------------------+----------------------------------------------------------------+---------------------------+
| Type                  | Name                                                           | On                        |
+=======================+================================================================+===========================+
| 🔑                    | auth_user_user_permissions_pkey                                | ON id                     |
+-----------------------+----------------------------------------------------------------+---------------------------+
| 🔍                    | auth_user_user_permissions_user_id_permission_id_14a6b632_uniq | ON user_id, permission_id |
+-----------------------+----------------------------------------------------------------+---------------------------+
| 🔎                    | auth_user_user_permissions_user_id_a95ead1b                    | ON user_id                |
+-----------------------+----------------------------------------------------------------+---------------------------+
| 🔎                    | auth_user_user_permissions_permission_id_1fbb5f2c              | ON permission_id          |
+-----------------------+----------------------------------------------------------------+---------------------------+

.. _foreign-keys-3:

**Foreign Keys**


+-----------------------+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Type                  | Name                                                        | On                                                                                    |
+=======================+=============================================================+=======================================================================================+
|                       | auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id | ( user_id ) ref `public.auth_user <#table-public-auth-user>`__ (id)                   |
+-----------------------+-------------------------------------------------------------+---------------------------------------------------------------------------------------+
|                       | auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    | ( permission_id ) ref `public.auth_permission <#table-public-auth-permission>`__ (id) |
+-----------------------+-------------------------------------------------------------+---------------------------------------------------------------------------------------+

Table public.authtoken_token
============================

======= ======= ===========
Idx     Name    Data Type
======= ======= ===========
\*      created timestamptz
\* 🔍 ⬈ user_id integer
======= ======= ===========

.. _Indexes-6:

**Indexes**


==== =========================== ==========
Type Name                        On
==== =========================== ==========
🔍   authtoken_token_user_id_key ON user_id
==== =========================== ==========

.. _foreign-keys-4:

**Foreign Keys**


+-----------------------+--------------------------------------------------+---------------------------------------------------------------------+
| Type                  | Name                                             | On                                                                  |
+=======================+==================================================+=====================================================================+
|                       | authtoken_token_user_id_35299eff_fk_auth_user_id | ( user_id ) ref `public.auth_user <#table-public-auth-user>`__ (id) |
+-----------------------+--------------------------------------------------+---------------------------------------------------------------------+

Table public.django_admin_log
=============================

======= =============== ============
Idx     Name            Data Type
======= =============== ============
\* 🔑   id              serial
\*      action_time     timestamptz
\       object_id       text
\*      object_repr     varchar(200)
\*      action_flag     smallint
\*      change_message  text
🔎 ⬈    content_type_id integer
\* 🔎 ⬈ user_id         integer
======= =============== ============

.. _Indexes-7:

**Indexes**


+-----------------------+-------------------------------------------+-----------------------+
| Type                  | Name                                      | On                    |
+=======================+===========================================+=======================+
| 🔑                    | django_admin_log_pkey                     | ON id                 |
+-----------------------+-------------------------------------------+-----------------------+
| 🔎                    | django_admin_log_content_type_id_c4bce8eb | ON content_type_id    |
+-----------------------+-------------------------------------------+-----------------------+
| 🔎                    | django_admin_log_user_id_c564eba6         | ON user_id            |
+-----------------------+-------------------------------------------+-----------------------+

.. _foreign-keys-5:

**Foreign Keys**


+-----------------------+--------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Type                  | Name                                                   | On                                                                                              |
+=======================+========================================================+=================================================================================================+
|                       | django_admin_log_content_type_id_c4bce8eb_fk_django_co | ( content_type_id ) ref `public.django_content_type <#table-public-django-content-type>`__ (id) |
+-----------------------+--------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|                       | django_admin_log_user_id_c564eba6_fk_auth_user_id      | ( user_id ) ref `public.auth_user <#table-public-auth-user>`__ (id)                             |
+-----------------------+--------------------------------------------------------+-------------------------------------------------------------------------------------------------+

**Constraints**


================================== ==================
Name                               Definition
================================== ==================
django_admin_log_action_flag_check (action_flag >= 0)
================================== ==================

Table public.django_content_type
================================

======= ========= ============
Idx     Name      Data Type
======= ========= ============
\* 🔑 ⬋ id        serial
\* 🔍   app_label varchar(100)
\* 🔍   model     varchar(100)
======= ========= ============

.. _Indexes-8:

**Indexes**


+-----------------------+---------------------------------------------------+-----------------------+
| Type                  | Name                                              | On                    |
+=======================+===================================================+=======================+
| 🔑                    | django_content_type_pkey                          | ON id                 |
+-----------------------+---------------------------------------------------+-----------------------+
| 🔍                    | django_content_type_app_label_model_76bd3d3b_uniq | ON app_label, model   |
+-----------------------+---------------------------------------------------+-----------------------+

Table public.django_migrations
==============================

===== ======= ============
Idx   Name    Data Type
===== ======= ============
\* 🔑 id      bigserial
\*    app     varchar(255)
\*    name    varchar(255)
\*    applied timestamptz
===== ======= ============

.. _Indexes-9:

**Indexes**


==== ====================== =====
Type Name                   On
==== ====================== =====
🔑   django_migrations_pkey ON id
==== ====================== =====

Table public.django_session
===========================

===== ============ ===========
Idx   Name         Data Type
===== ============ ===========
\* 🔑 session_key  varchar(40)
\*    session_data text
\* 🔎 expire_date  timestamptz
===== ============ ===========

.. _Indexes-10:

**Indexes**


==== ======================================== ==============
Type Name                                     On
==== ======================================== ==============
🔑   django_session_pkey                      ON session_key
🔎   django_session_session_key_c0390e0f_like ON session_key
🔎   django_session_expire_date_a5c62663      ON expire_date
==== ======================================== ==============

Table public.pbx_access_control_nodes
=====================================

======= ==================== ============
Idx     Name                 Data Type
======= ==================== ============
\* 🔑   id                   uuid
\*      type                 varchar(8)
\       cidr                 varchar(64)
\       domain               varchar(64)
\       description          varchar(254)
\       created              timestamptz
\       updated              timestamptz
\       synchronised         timestamptz
\*      updated_by           varchar(64)
\* 🔎 ⬈ access_control_id_id uuid
======= ==================== ============

.. _Indexes-11:

**Indexes**


+-----------------------+--------------------------------------------------------+-------------------------+
| Type                  | Name                                                   | On                      |
+=======================+========================================================+=========================+
| 🔑                    | pbx_access_control_nodes_pkey                          | ON id                   |
+-----------------------+--------------------------------------------------------+-------------------------+
| 🔎                    | pbx_access_control_nodes_access_control_id_id_d842e92a | ON access_control_id_id |
+-----------------------+--------------------------------------------------------+-------------------------+

.. _foreign-keys-6:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Type                  | Name                                                            | On                                                                                                   |
+=======================+=================================================================+======================================================================================================+
|                       | pbx_access_control_n_access_control_id_id_d842e92a_fk_pbx_acces | ( access_control_id_id ) ref `public.pbx_access_controls <#table-public-pbx-access-controls>`__ (id) |
+-----------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

Table public.pbx_access_controls
================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(64)
\*      default      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ============

.. _Indexes-12:

**Indexes**


==== ======================== =====
Type Name                     On
==== ======================== =====
🔑   pbx_access_controls_pkey ON id
==== ======================== =====

Table public.pbx_auto_report
============================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\       name         varchar(64)
\       title        varchar(128)
\       message      text
\       footer       varchar(256)
\*      recipients   text
\       frequency    varchar(8)
\*      enabled      varchar(8)
\       description  varchar(128)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
🔎 ⬈    domain_uuid  uuid
======= ============ ============

.. _Indexes-13:

**Indexes**


==== ==================================== ==============
Type Name                                 On
==== ==================================== ==============
🔑   pbx_auto_report_pkey                 ON id
🔎   pbx_auto_report_domain_uuid_80816be5 ON domain_uuid
==== ==================================== ==============

.. _foreign-keys-7:

**Foreign Keys**


+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                   | On                                                                          |
+=======================+========================================================+=============================================================================+
|                       | pbx_auto_report_domain_uuid_80816be5_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_auto_report_section
====================================

===== ============== ============
Idx   Name           Data Type
===== ============== ============
\* 🔑 id             uuid
\     title          varchar(128)
\*    sequence       numeric(3)
\*    sql            text
\     message        text
\*    enabled        varchar(8)
\     description    varchar(128)
\     created        timestamptz
\     updated        timestamptz
\     synchronised   timestamptz
\*    updated_by     varchar(64)
🔎 ⬈  auto_report_id uuid
===== ============== ============

.. _Indexes-14:

**Indexes**


+-----------------------+-------------------------------------------------+-----------------------+
| Type                  | Name                                            | On                    |
+=======================+=================================================+=======================+
| 🔑                    | pbx_auto_report_section_pkey                    | ON id                 |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔎                    | pbx_auto_report_section_auto_report_id_ca93bf77 | ON auto_report_id     |
+-----------------------+-------------------------------------------------+-----------------------+

.. _foreign-keys-8:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                                     |
+=======================+============================================================+========================================================================================+
|                       | pbx_auto_report_sect_auto_report_id_ca93bf77_fk_pbx_auto\_ | ( auto_report_id ) ref `public.pbx_auto_report <#table-public-pbx-auto-report>`__ (id) |
+-----------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------+

Table public.pbx_bridges
========================

===== ============ ============
Idx   Name         Data Type
===== ============ ============
\* 🔑 id           uuid
\*    name         varchar(32)
\*    destination  varchar(256)
\*    enabled      varchar(8)
\     description  varchar(64)
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
🔎 ⬈  domain_uuid  uuid
===== ============ ============

.. _Indexes-15:

**Indexes**


==== ================================ ==============
Type Name                             On
==== ================================ ==============
🔑   pbx_bridges_pkey                 ON id
🔎   pbx_bridges_domain_uuid_41623292 ON domain_uuid
==== ================================ ==============

.. _foreign-keys-9:

**Foreign Keys**


+-----------------------+----------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                               | On                                                                          |
+=======================+====================================================+=============================================================================+
|                       | pbx_bridges_domain_uuid_41623292_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+----------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_call_block
===========================

===== ============ ============
Idx   Name         Data Type
===== ============ ============
\* 🔑 id           uuid
\     name         varchar(64)
\     number       varchar(64)
\*    block_count  numeric(6)
\     app          varchar(32)
\     data         varchar(256)
\*    enabled      varchar(8)
\     description  varchar(64)
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
🔎 ⬈  domain_uuid  uuid
===== ============ ============

.. _Indexes-16:

**Indexes**


==== =================================== ==============
Type Name                                On
==== =================================== ==============
🔑   pbx_call_block_pkey                 ON id
🔎   pbx_call_block_domain_uuid_6e47cf15 ON domain_uuid
==== =================================== ==============

.. _foreign-keys-10:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                          |
+=======================+=======================================================+=============================================================================+
|                       | pbx_call_block_domain_uuid_6e47cf15_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_call_centre_agents
===================================

======= ==================== ============
Idx     Name                 Data Type
======= ==================== ============
\* 🔑 ⬋ id                   uuid
\       name                 varchar(64)
\       agent_type           varchar(16)
\*      call_timeout         numeric(3)
🔍      agent_id             varchar(64)
\*      agent_pin            varchar(16)
\       contact              varchar(256)
\       status               varchar(32)
\*      data                 varchar(64)
\*      no_answer_delay_time numeric(3)
\*      max_no_answer        numeric(3)
\*      wrap_up_time         numeric(3)
\*      reject_delay_time    numeric(3)
\*      busy_delay_time      numeric(3)
\       created              timestamptz
\       updated              timestamptz
\       synchronised         timestamptz
\*      updated_by           varchar(64)
🔍 ⬈    domain_uuid          uuid
🔎 ⬈    user_uuid            uuid
======= ==================== ============

.. _Indexes-17:

**Indexes**


+-----------------------+-----------------------------------------------------------+--------------------------+
| Type                  | Name                                                      | On                       |
+=======================+===========================================================+==========================+
| 🔑                    | pbx_call_centre_agents_pkey                               | ON id                    |
+-----------------------+-----------------------------------------------------------+--------------------------+
| 🔍                    | pbx_call_centre_agents_domain_uuid_agent_id_cfab14bd_uniq | ON domain_uuid, agent_id |
+-----------------------+-----------------------------------------------------------+--------------------------+
| 🔎                    | pbx_call_centre_agents_domain_uuid_e3542885               | ON domain_uuid           |
+-----------------------+-----------------------------------------------------------+--------------------------+
| 🔎                    | pbx_call_centre_agents_user_uuid_6eab1ecb                 | ON user_uuid             |
+-----------------------+-----------------------------------------------------------+--------------------------+

.. _foreign-keys-11:

**Foreign Keys**


+-----------------------+---------------------------------------------------------------+------------------------------------------------------------------------------+
| Type                  | Name                                                          | On                                                                           |
+=======================+===============================================================+==============================================================================+
|                       | pbx_call_centre_agents_domain_uuid_e3542885_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id)  |
+-----------------------+---------------------------------------------------------------+------------------------------------------------------------------------------+
|                       | pbx_call_centre_agen_user_uuid_6eab1ecb_fk_pbx_users          | ( user_uuid ) ref `public.pbx_users <#table-public-pbx-users>`__ (user_uuid) |
+-----------------------+---------------------------------------------------------------+------------------------------------------------------------------------------+

Table public.pbx_call_centre_queues
===================================

======= ===================== ============
Idx     Name                  Data Type
======= ===================== ============
\* 🔑 ⬋ id                    uuid
\       name                  varchar(64)
\*      extension             varchar(32)
\       greeting              varchar(256)
\       strategy              varchar(32)
\       moh_sound             varchar(256)
\       record_template       varchar(256)
\       time_base_score       varchar(16)
\*      max_wait_time         numeric(3)
\*      max_wait_time_na      numeric(3)
\*      max_wait_time_natr    numeric(3)
\       timeout_action        varchar(256)
\*      tier_rules_apply      varchar(8)
\*      tier_rule_wait_sec    numeric(3)
\*      tier_rule_wm_level    varchar(8)
\*      tier_rule_nanw        varchar(8)
\*      discard_abndnd_after  numeric(4)
\*      abndnd_resume_allowed varchar(8)
\       cid_name_prefix       varchar(32)
\       announce_sound        varchar(256)
\       announce_frequency    numeric(3)
\       cc_exit_keys          varchar(8)
\*      enabled               varchar(8)
\       description           varchar(64)
\       dialplan_id           uuid
\       created               timestamptz
\       updated               timestamptz
\       synchronised          timestamptz
\*      updated_by            varchar(64)
🔎 ⬈    domain_uuid           uuid
\*      wb_aban_crit_level    numeric(3)
\*      wb_aban_warn_level    numeric(3)
\*      wb_agents_per_row     numeric(3)
\*      wb_show_agents        varchar(8)
\*      wb_wait_crit_level    numeric(3)
\*      wb_wait_warn_level    numeric(3)
======= ===================== ============

.. _Indexes-18:

**Indexes**


+-----------------------+---------------------------------------------+-----------------------+
| Type                  | Name                                        | On                    |
+=======================+=============================================+=======================+
| 🔑                    | pbx_call_centre_queues_pkey                 | ON id                 |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_call_centre_queues_domain_uuid_496e4188 | ON domain_uuid        |
+-----------------------+---------------------------------------------+-----------------------+

.. _foreign-keys-12:

**Foreign Keys**


+-----------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                          | On                                                                          |
+=======================+===============================================================+=============================================================================+
|                       | pbx_call_centre_queues_domain_uuid_496e4188_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_call_centre_tiers
==================================

======= ============= ===========
Idx     Name          Data Type
======= ============= ===========
\* 🔑   id            uuid
\*      tier_level    numeric(4)
\*      tier_position numeric(4)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ agent_id_id   uuid
\* 🔎 ⬈ queue_id_id   uuid
======= ============= ===========

.. _Indexes-19:

**Indexes**


+-----------------------+--------------------------------------------+-----------------------+
| Type                  | Name                                       | On                    |
+=======================+============================================+=======================+
| 🔑                    | pbx_call_centre_tiers_pkey                 | ON id                 |
+-----------------------+--------------------------------------------+-----------------------+
| 🔎                    | pbx_call_centre_tiers_agent_id_id_bbc2132e | ON agent_id_id        |
+-----------------------+--------------------------------------------+-----------------------+
| 🔎                    | pbx_call_centre_tiers_queue_id_id_24aa23a1 | ON queue_id_id        |
+-----------------------+--------------------------------------------+-----------------------+

.. _foreign-keys-13:

**Foreign Keys**


+-----------------------+---------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Type                  | Name                                                    | On                                                                                                |
+=======================+=========================================================+===================================================================================================+
|                       | pbx_call_centre_tier_agent_id_id_bbc2132e_fk_pbx_call\_ | ( agent_id_id ) ref `public.pbx_call_centre_agents <#table-public-pbx-call-centre-agents>`__ (id) |
+-----------------------+---------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|                       | pbx_call_centre_tier_queue_id_id_24aa23a1_fk_pbx_call\_ | ( queue_id_id ) ref `public.pbx_call_centre_queues <#table-public-pbx-call-centre-queues>`__ (id) |
+-----------------------+---------------------------------------------------------+---------------------------------------------------------------------------------------------------+

Table public.pbx_call_flows
===========================

===== =============== ============
Idx   Name            Data Type
===== =============== ============
\* 🔑 id              uuid
\     name            varchar(64)
\*    extension       varchar(32)
\*    feature_code    varchar(8)
\*    status          varchar(8)
\     pin_number      varchar(16)
\     label           varchar(32)
\     sound           varchar(254)
\     app             varchar(32)
\     data            varchar(256)
\     alternate_label varchar(32)
\     alternate_sound varchar(254)
\     alternate_app   varchar(32)
\     alternate_data  varchar(256)
🔎    context         varchar(128)
\     description     varchar(64)
\     dialplan_id     uuid
\     created         timestamptz
\     updated         timestamptz
\     synchronised    timestamptz
\*    updated_by      varchar(64)
🔎 ⬈  domain_uuid     uuid
===== =============== ============

.. _Indexes-20:

**Indexes**


==== ==================================== ==============
Type Name                                 On
==== ==================================== ==============
🔑   pbx_call_flows_pkey                  ON id
🔎   pbx_call_flows_context_1e7d42c9      ON context
🔎   pbx_call_flows_context_1e7d42c9_like ON context
🔎   pbx_call_flows_domain_uuid_436e3fcb  ON domain_uuid
==== ==================================== ==============

.. _foreign-keys-14:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                          |
+=======================+=======================================================+=============================================================================+
|                       | pbx_call_flows_domain_uuid_436e3fcb_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_cc_agent_status_log
====================================

======= ============ ===========
Idx     Name         Data Type
======= ============ ===========
\* 🔑   id           uuid
\       status       varchar(32)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ agent_id_id  uuid
======= ============ ===========

.. _Indexes-21:

**Indexes**


+-----------------------+----------------------------------------------+-----------------------+
| Type                  | Name                                         | On                    |
+=======================+==============================================+=======================+
| 🔑                    | pbx_cc_agent_status_log_pkey                 | ON id                 |
+-----------------------+----------------------------------------------+-----------------------+
| 🔎                    | pbx_cc_agent_status_log_agent_id_id_2fe7e484 | ON agent_id_id        |
+-----------------------+----------------------------------------------+-----------------------+

.. _foreign-keys-15:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                                |
+=======================+===========================================================+===================================================================================================+
|                       | pbx_cc_agent_status\_\ *agent_id_id_2fe7e484_fk_pbx_call* | ( agent_id_id ) ref `public.pbx_call_centre_agents <#table-public-pbx-call-centre-agents>`__ (id) |
+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+

Table public.pbx_conference_centres
===================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\       name         varchar(64)
\*      extension    varchar(32)
\       greeting     varchar(254)
\*      enabled      varchar(8)
\       description  varchar(64)
\       dialplan_id  uuid
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
🔎 ⬈    domain_uuid  uuid
======= ============ ============

.. _Indexes-22:

**Indexes**


+-----------------------+---------------------------------------------+-----------------------+
| Type                  | Name                                        | On                    |
+=======================+=============================================+=======================+
| 🔑                    | pbx_conference_centres_pkey                 | ON id                 |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_conference_centres_domain_uuid_734e0ffb | ON domain_uuid        |
+-----------------------+---------------------------------------------+-----------------------+

.. _foreign-keys-16:

**Foreign Keys**


+-----------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                          | On                                                                          |
+=======================+===============================================================+=============================================================================+
|                       | pbx_conference_centres_domain_uuid_734e0ffb_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+---------------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_conference_control_details
===========================================

======= =============== ============
Idx     Name            Data Type
======= =============== ============
\* 🔑   id              uuid
\*      digits          varchar(8)
\*      action          varchar(64)
\       data            varchar(254)
\*      enabled         varchar(8)
\       created         timestamptz
\       updated         timestamptz
\       synchronised    timestamptz
\*      updated_by      varchar(64)
\* 🔎 ⬈ conf_ctrl_id_id uuid
======= =============== ============

.. _Indexes-23:

**Indexes**


+-----------------------+---------------------------------------------------------+-----------------------+
| Type                  | Name                                                    | On                    |
+=======================+=========================================================+=======================+
| 🔑                    | pbx_conference_control_details_pkey                     | ON id                 |
+-----------------------+---------------------------------------------------------+-----------------------+
| 🔎                    | pbx_conference_control_details_conf_ctrl_id_id_487dc607 | ON conf_ctrl_id_id    |
+-----------------------+---------------------------------------------------------+-----------------------+

.. _foreign-keys-17:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                                                      |
+=======================+============================================================+=========================================================================================================+
|                       | pbx_conference_contr_conf_ctrl_id_id_487dc607_fk_pbx_confe | ( conf_ctrl_id_id ) ref `public.pbx_conference_controls <#table-public-pbx-conference-controls>`__ (id) |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

Table public.pbx_conference_controls
====================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(32)
\*      enabled      varchar(8)
\       description  varchar(256)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ============

.. _Indexes-24:

**Indexes**


==== ============================ =====
Type Name                         On
==== ============================ =====
🔑   pbx_conference_controls_pkey ON id
==== ============================ =====

Table public.pbx_conference_profile_params
==========================================

======= ================== ============
Idx     Name               Data Type
======= ================== ============
\* 🔑   id                 uuid
\*      name               varchar(64)
\       value              varchar(254)
\*      enabled            varchar(8)
\       description        varchar(254)
\       created            timestamptz
\       updated            timestamptz
\       synchronised       timestamptz
\*      updated_by         varchar(64)
\* 🔎 ⬈ conf_profile_id_id uuid
======= ================== ============

.. _Indexes-25:

**Indexes**


+-----------------------+-----------------------------------------------------------+-----------------------+
| Type                  | Name                                                      | On                    |
+=======================+===========================================================+=======================+
| 🔑                    | pbx_conference_profile_params_pkey                        | ON id                 |
+-----------------------+-----------------------------------------------------------+-----------------------+
| 🔎                    | pbx_conference_profile_params_conf_profile_id_id_4829dcec | ON conf_profile_id_id |
+-----------------------+-----------------------------------------------------------+-----------------------+

.. _foreign-keys-18:

**Foreign Keys**


+-----------------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Type                  | Name                                                          | On                                                                                                         |
+=======================+===============================================================+============================================================================================================+
|                       | pbx_conference_profi_conf_profile_id_id_4829dcec_fk_pbx_confe | ( conf_profile_id_id ) ref `public.pbx_conference_profiles <#table-public-pbx-conference-profiles>`__ (id) |
+-----------------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Table public.pbx_conference_profiles
====================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(32)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ============

.. _Indexes-26:

**Indexes**


==== ============================ =====
Type Name                         On
==== ============================ =====
🔑   pbx_conference_profiles_pkey ON id
==== ============================ =====

Table public.pbx_conference_room_users
======================================

======= ============ ===========
Idx     Name         Data Type
======= ============ ===========
\* 🔑   id           uuid
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ c_room_id_id uuid
🔎 ⬈    user_uuid    uuid
======= ============ ===========

.. _Indexes-27:

**Indexes**


+-----------------------+-------------------------------------------------+-----------------------+
| Type                  | Name                                            | On                    |
+=======================+=================================================+=======================+
| 🔑                    | pbx_conference_room_users_pkey                  | ON id                 |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔎                    | pbx_conference_room_users_c_room_id_id_b06cc2c1 | ON c_room_id_id       |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔎                    | pbx_conference_room_users_user_uuid_f8ec5578    | ON user_uuid          |
+-----------------------+-------------------------------------------------+-----------------------+

.. _foreign-keys-19:

**Foreign Keys**


+-----------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Type                  | Name                                                     | On                                                                                             |
+=======================+==========================================================+================================================================================================+
|                       | pbx_conference_room\__c_room_id_id_b06cc2c1_fk_pbx_confe | ( c_room_id_id ) ref `public.pbx_conference_rooms <#table-public-pbx-conference-rooms>`__ (id) |
+-----------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------+
|                       | pbx_conference_room\__user_uuid_f8ec5578_fk_pbx_users    | ( user_uuid ) ref `public.pbx_users <#table-public-pbx-users>`__ (user_uuid)                   |
+-----------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------+

Table public.pbx_conference_rooms
=================================

======= =============== ===========
Idx     Name            Data Type
======= =============== ===========
\* 🔑 ⬋ id              uuid
\       name            varchar(64)
\* 🔍   moderator_pin   varchar(16)
\* 🔍   participant_pin varchar(16)
\*      max_members     numeric(3)
\       start_time      timestamptz
\       stop_time       timestamptz
\*      record          varchar(8)
\*      wait_mod        varchar(8)
\*      announce        varchar(8)
\*      sounds          varchar(8)
\*      mute            varchar(8)
\*      enabled         varchar(8)
\       description     varchar(64)
\       created         timestamptz
\       updated         timestamptz
\       synchronised    timestamptz
\*      updated_by      varchar(64)
\* 🔍 ⬈ c_centre_id_id  uuid
\* 🔎 ⬈ c_profile_id_id uuid
======= =============== ===========

.. _Indexes-28:

**Indexes**


+-----------------------+-----------------------------------------------------------------+------------------------------------+
| Type                  | Name                                                            | On                                 |
+=======================+=================================================================+====================================+
| 🔑                    | pbx_conference_rooms_pkey                                       | ON id                              |
+-----------------------+-----------------------------------------------------------------+------------------------------------+
| 🔍                    | pbx_conference_rooms_c_centre_id_id_moderator_pin_b138db4e_uniq | ON c_centre_id_id, moderator_pin   |
+-----------------------+-----------------------------------------------------------------+------------------------------------+
| 🔍                    | pbx_conference_rooms_c_centre_id_id_participa_c8fb4ea1_uniq     | ON c_centre_id_id, participant_pin |
+-----------------------+-----------------------------------------------------------------+------------------------------------+
| 🔎                    | pbx_conference_rooms_c_centre_id_id_b917996a                    | ON c_centre_id_id                  |
+-----------------------+-----------------------------------------------------------------+------------------------------------+
| 🔎                    | pbx_conference_rooms_c_profile_id_id_14ed4f86                   | ON c_profile_id_id                 |
+-----------------------+-----------------------------------------------------------------+------------------------------------+

.. _foreign-keys-20:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                                                      |
+=======================+============================================================+=========================================================================================================+
|                       | pbx_conference_rooms_c_centre_id_id_b917996a_fk_pbx_confe  | ( c_centre_id_id ) ref `public.pbx_conference_centres <#table-public-pbx-conference-centres>`__ (id)    |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|                       | pbx_conference_rooms_c_profile_id_id_14ed4f86_fk_pbx_confe | ( c_profile_id_id ) ref `public.pbx_conference_profiles <#table-public-pbx-conference-profiles>`__ (id) |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

Table public.pbx_conference_sessions
====================================

======= ================ ============
Idx     Name             Data Type
======= ================ ============
\* 🔑   id               uuid
\       caller_id_name   varchar(128)
\       caller_id_number varchar(64)
\       profile          varchar(32)
\*      live             varchar(8)
\       recording        varchar(256)
\       start            timestamptz
\       end              timestamptz
\       created          timestamptz
\       updated          timestamptz
\       synchronised     timestamptz
\*      updated_by       varchar(64)
\* 🔎 ⬈ c_room_id_id     uuid
======= ================ ============

.. _Indexes-29:

**Indexes**


+-----------------------+-----------------------------------------------+-----------------------+
| Type                  | Name                                          | On                    |
+=======================+===============================================+=======================+
| 🔑                    | pbx_conference_sessions_pkey                  | ON id                 |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_conference_sessions_c_room_id_id_f5c1cfb4 | ON c_room_id_id       |
+-----------------------+-----------------------------------------------+-----------------------+

.. _foreign-keys-21:

**Foreign Keys**


+-----------------------+---------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Type                  | Name                                                    | On                                                                                             |
+=======================+=========================================================+================================================================================================+
|                       | pbx_conference_sessi_c_room_id_id_f5c1cfb4_fk_pbx_confe | ( c_room_id_id ) ref `public.pbx_conference_rooms <#table-public-pbx-conference-rooms>`__ (id) |
+-----------------------+---------------------------------------------------------+------------------------------------------------------------------------------------------------+

Table public.pbx_contacts
=========================

======= ================ ============
Idx     Name             Data Type
======= ================ ============
\* 🔑 ⬋ id               uuid
\*      fn               varchar(254)
\*      family_name      varchar(64)
\       given_name       varchar(64)
\       additional_name  varchar(64)
\       honorific_prefix varchar(32)
\       honorific_suffix varchar(32)
\       nickname         varchar(64)
\       timezone         varchar(128)
\       notes            text
\*      enabled          varchar(8)
\       created          timestamptz
\       updated          timestamptz
\       synchronised     timestamptz
\*      updated_by       varchar(64)
🔎 ⬈    domain_id_id     uuid
🔎 ⬈    user_id_id       bigint
======= ================ ============

.. _Indexes-30:

**Indexes**


==== ================================== ===============
Type Name                               On
==== ================================== ===============
🔑   pbx_contacts_pkey                  ON id
🔎   pbx_contacts_domain_id_id_5e67d2a4 ON domain_id_id
🔎   pbx_contacts_user_id_id_0ad8c3a4   ON user_id_id
==== ================================== ===============

.. _foreign-keys-22:

**Foreign Keys**


+-----------------------+------------------------------------------------------+------------------------------------------------------------------------------+
| Type                  | Name                                                 | On                                                                           |
+=======================+======================================================+==============================================================================+
|                       | pbx_contacts_domain_id_id_5e67d2a4_fk_pbx_domains_id | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+------------------------------------------------------+------------------------------------------------------------------------------+
|                       | pbx_contacts_user_id_id_0ad8c3a4_fk_pbx_users_id     | ( user_id_id ) ref `public.pbx_users <#table-public-pbx-users>`__ (id)       |
+-----------------------+------------------------------------------------------+------------------------------------------------------------------------------+

Table public.pbx_contacts_address
=================================

======= ================ ============
Idx     Name             Data Type
======= ================ ============
\* 🔑   id               uuid
\*      post_office_box  varchar(64)
\*      extended_address varchar(128)
\*      street_address   varchar(128)
\*      locality         varchar(128)
\*      region           varchar(128)
\*      postal_code      varchar(16)
\*      country_name     varchar(128)
\*      addr_type        varchar(16)
\       created          timestamptz
\       updated          timestamptz
\       synchronised     timestamptz
\*      updated_by       varchar(64)
\* 🔎 ⬈ contact_id_id    uuid
======= ================ ============

.. _Indexes-31:

**Indexes**


+-----------------------+---------------------------------------------+-----------------------+
| Type                  | Name                                        | On                    |
+=======================+=============================================+=======================+
| 🔑                    | pbx_contacts_address_pkey                   | ON id                 |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_address_contact_id_id_efcbd0bb | ON contact_id_id      |
+-----------------------+---------------------------------------------+-----------------------+

.. _foreign-keys-23:

**Foreign Keys**


+-----------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                           | On                                                                              |
+=======================+================================================================+=================================================================================+
|                       | pbx_contacts_address_contact_id_id_efcbd0bb_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_category
==================================

======= ============= ===========
Idx     Name          Data Type
======= ============= ===========
\* 🔑   id            uuid
\*      category      varchar(64)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ contact_id_id uuid
======= ============= ===========

.. _Indexes-32:

**Indexes**


+-----------------------+----------------------------------------------+-----------------------+
| Type                  | Name                                         | On                    |
+=======================+==============================================+=======================+
| 🔑                    | pbx_contacts_category_pkey                   | ON id                 |
+-----------------------+----------------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_category_contact_id_id_490708cf | ON contact_id_id      |
+-----------------------+----------------------------------------------+-----------------------+

.. _foreign-keys-24:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                            | On                                                                              |
+=======================+=================================================================+=================================================================================+
|                       | pbx_contacts_category_contact_id_id_490708cf_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_dates
===============================

======= ============= ===========
Idx     Name          Data Type
======= ============= ===========
\* 🔑   id            uuid
\       sig_date      date
\*      label         varchar(64)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ contact_id_id uuid
======= ============= ===========

.. _Indexes-33:

**Indexes**


+-----------------------+-------------------------------------------+-----------------------+
| Type                  | Name                                      | On                    |
+=======================+===========================================+=======================+
| 🔑                    | pbx_contacts_dates_pkey                   | ON id                 |
+-----------------------+-------------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_dates_contact_id_id_954dc217 | ON contact_id_id      |
+-----------------------+-------------------------------------------+-----------------------+

.. _foreign-keys-25:

**Foreign Keys**


+-----------------------+--------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                         | On                                                                              |
+=======================+==============================================================+=================================================================================+
|                       | pbx_contacts_dates_contact_id_id_954dc217_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+--------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_email
===============================

======= ============= =============
Idx     Name          Data Type
======= ============= =============
\* 🔑   id            uuid
\*      email_type    varchar(16)
\*      email         varchar(1024)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ contact_id_id uuid
======= ============= =============

.. _Indexes-34:

**Indexes**


+-----------------------+-------------------------------------------+-----------------------+
| Type                  | Name                                      | On                    |
+=======================+===========================================+=======================+
| 🔑                    | pbx_contacts_email_pkey                   | ON id                 |
+-----------------------+-------------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_email_contact_id_id_a3fd5069 | ON contact_id_id      |
+-----------------------+-------------------------------------------+-----------------------+

.. _foreign-keys-26:

**Foreign Keys**


+-----------------------+--------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                         | On                                                                              |
+=======================+==============================================================+=================================================================================+
|                       | pbx_contacts_email_contact_id_id_a3fd5069_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+--------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_geo
=============================

======= ============= =============
Idx     Name          Data Type
======= ============= =============
\* 🔑   id            uuid
\*      geo_uri       varchar(1024)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ contact_id_id uuid
======= ============= =============

.. _Indexes-35:

**Indexes**


+-----------------------+-----------------------------------------+-----------------------+
| Type                  | Name                                    | On                    |
+=======================+=========================================+=======================+
| 🔑                    | pbx_contacts_geo_pkey                   | ON id                 |
+-----------------------+-----------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_geo_contact_id_id_cbb59f6e | ON contact_id_id      |
+-----------------------+-----------------------------------------+-----------------------+

.. _foreign-keys-27:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                              |
+=======================+============================================================+=================================================================================+
|                       | pbx_contacts_geo_contact_id_id_cbb59f6e_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_groups
================================

======= ============= ===========
Idx     Name          Data Type
======= ============= ===========
\* 🔑   id            uuid
\       name          varchar(64)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ contact_id_id uuid
\* 🔎 ⬈ group_id      integer
======= ============= ===========

.. _Indexes-36:

**Indexes**


+-----------------------+--------------------------------------------+-----------------------+
| Type                  | Name                                       | On                    |
+=======================+============================================+=======================+
| 🔑                    | pbx_contacts_groups_pkey                   | ON id                 |
+-----------------------+--------------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_groups_contact_id_id_83fcf911 | ON contact_id_id      |
+-----------------------+--------------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_groups_group_id_dc0329a4      | ON group_id           |
+-----------------------+--------------------------------------------+-----------------------+

.. _foreign-keys-28:

**Foreign Keys**


+-----------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                          | On                                                                              |
+=======================+===============================================================+=================================================================================+
|                       | pbx_contacts_groups_contact_id_id_83fcf911_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------+
|                       | pbx_contacts_groups_group_id_dc0329a4_fk_auth_group_id        | ( group_id ) ref `public.auth_group <#table-public-auth-group>`__ (id)          |
+-----------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_org
=============================

======= ================= ============
Idx     Name              Data Type
======= ================= ============
\* 🔑   id                uuid
\*      organisation_name varchar(128)
\*      organisation_unit varchar(128)
\       created           timestamptz
\       updated           timestamptz
\       synchronised      timestamptz
\*      updated_by        varchar(64)
\* 🔎 ⬈ contact_id_id     uuid
======= ================= ============

.. _Indexes-37:

**Indexes**


+-----------------------+-----------------------------------------+-----------------------+
| Type                  | Name                                    | On                    |
+=======================+=========================================+=======================+
| 🔑                    | pbx_contacts_org_pkey                   | ON id                 |
+-----------------------+-----------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_org_contact_id_id_d5127702 | ON contact_id_id      |
+-----------------------+-----------------------------------------+-----------------------+

.. _foreign-keys-29:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                              |
+=======================+============================================================+=================================================================================+
|                       | pbx_contacts_org_contact_id_id_d5127702_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_tel
=============================

======= ============= ============
Idx     Name          Data Type
======= ============= ============
\* 🔑   id            uuid
\*      tel_type      varchar(32)
\*      number        varchar(128)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ contact_id_id uuid
\       speed_dial    varchar(16)
======= ============= ============

.. _Indexes-38:

**Indexes**


+-----------------------+-----------------------------------------+-----------------------+
| Type                  | Name                                    | On                    |
+=======================+=========================================+=======================+
| 🔑                    | pbx_contacts_tel_pkey                   | ON id                 |
+-----------------------+-----------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_tel_contact_id_id_3ac83646 | ON contact_id_id      |
+-----------------------+-----------------------------------------+-----------------------+

.. _foreign-keys-30:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                              |
+=======================+============================================================+=================================================================================+
|                       | pbx_contacts_tel_contact_id_id_3ac83646_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_contacts_url
=============================

======= ============= =============
Idx     Name          Data Type
======= ============= =============
\* 🔑   id            uuid
\*      url_uri       varchar(1024)
\       created       timestamptz
\       updated       timestamptz
\       synchronised  timestamptz
\*      updated_by    varchar(64)
\* 🔎 ⬈ contact_id_id uuid
======= ============= =============

.. _Indexes-39:

**Indexes**


+-----------------------+-----------------------------------------+-----------------------+
| Type                  | Name                                    | On                    |
+=======================+=========================================+=======================+
| 🔑                    | pbx_contacts_url_pkey                   | ON id                 |
+-----------------------+-----------------------------------------+-----------------------+
| 🔎                    | pbx_contacts_url_contact_id_id_3a99de63 | ON contact_id_id      |
+-----------------------+-----------------------------------------+-----------------------+

.. _foreign-keys-31:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                              |
+=======================+============================================================+=================================================================================+
|                       | pbx_contacts_url_contact_id_id_3a99de63_fk_pbx_contacts_id | ( contact_id_id ) ref `public.pbx_contacts <#table-public-pbx-contacts>`__ (id) |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_default_settings
=================================

===== ============ ============
Idx   Name         Data Type
===== ============ ============
\* 🔑 id           uuid
\     app_uuid     uuid
\* 🔎 category     varchar(32)
\* 🔎 subcategory  varchar(64)
\* 🔎 value_type   varchar(32)
\     value        varchar(254)
\*    sequence     numeric(11)
\*    enabled      varchar(8)
\     description  varchar(128)
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
===== ============ ============

.. _Indexes-40:

**Indexes**


+-----------------------+------------------------------------------------+-----------------------+
| Type                  | Name                                           | On                    |
+=======================+================================================+=======================+
| 🔑                    | pbx_default_settings_pkey                      | ON id                 |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_default_settings_category_0b9f954d         | ON category           |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_default_settings_category_0b9f954d_like    | ON category           |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_default_settings_value_type_0fa61d41       | ON value_type         |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_default_settings_value_type_0fa61d41_like  | ON value_type         |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_default_settings_subcategory_5e12c14d      | ON subcategory        |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_default_settings_subcategory_5e12c14d_like | ON subcategory        |
+-----------------------+------------------------------------------------+-----------------------+

Table public.pbx_device_keys
============================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\*      category     varchar(16)
\*      key_id       numeric(11)
\*      key_type     varchar(64)
\*      line         numeric(3)
\       value        varchar(254)
\       extension    varchar(64)
\*      protected    varchar(8)
\       label        varchar(64)
\       icon         varchar(64)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ device_id    uuid
======= ============ ============

.. _Indexes-41:

**Indexes**


==== ================================== ============
Type Name                               On
==== ================================== ============
🔑   pbx_device_keys_pkey               ON id
🔎   pbx_device_keys_device_id_3e0c21ec ON device_id
==== ================================== ============

.. _foreign-keys-32:

**Foreign Keys**


+-----------------------+------------------------------------------------------+---------------------------------------------------------------------------+
| Type                  | Name                                                 | On                                                                        |
+=======================+======================================================+===========================================================================+
|                       | pbx_device_keys_device_id_3e0c21ec_fk_pbx_devices_id | ( device_id ) ref `public.pbx_devices <#table-public-pbx-devices>`__ (id) |
+-----------------------+------------------------------------------------------+---------------------------------------------------------------------------+

Table public.pbx_device_lines
=============================

======= ======================== ============
Idx     Name                     Data Type
======= ======================== ============
\* 🔑   id                       uuid
\*      line_number              numeric(3)
\       server_address           varchar(254)
\       server_address_primary   varchar(254)
\       server_address_secondary varchar(254)
\       outbound_proxy_primary   varchar(254)
\       outbound_proxy_secondary varchar(254)
\       display_name             varchar(254)
\       user_id                  varchar(254)
\       auth_id                  varchar(254)
\       password                 varchar(254)
\       sip_port                 numeric(5)
\       sip_transport            varchar(254)
\       register_expires         numeric(5)
\       shared_line              varchar(128)
\*      enabled                  varchar(8)
\       created                  timestamptz
\       updated                  timestamptz
\       synchronised             timestamptz
\*      updated_by               varchar(64)
\* 🔎 ⬈ device_id                uuid
======= ======================== ============

.. _Indexes-42:

**Indexes**


==== =================================== ============
Type Name                                On
==== =================================== ============
🔑   pbx_device_lines_pkey               ON id
🔎   pbx_device_lines_device_id_b3ca7db8 ON device_id
==== =================================== ============

.. _foreign-keys-33:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+---------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                        |
+=======================+=======================================================+===========================================================================+
|                       | pbx_device_lines_device_id_b3ca7db8_fk_pbx_devices_id | ( device_id ) ref `public.pbx_devices <#table-public-pbx-devices>`__ (id) |
+-----------------------+-------------------------------------------------------+---------------------------------------------------------------------------+

Table public.pbx_device_profile_keys
====================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\*      category     varchar(16)
\*      key_id       numeric(11)
\*      key_type     varchar(64)
\*      line         numeric(3)
\       value        varchar(254)
\       extension    varchar(64)
\*      protected    varchar(8)
\       label        varchar(64)
\       icon         varchar(64)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ profile_id   uuid
======= ============ ============

.. _Indexes-43:

**Indexes**


+-----------------------+---------------------------------------------+-----------------------+
| Type                  | Name                                        | On                    |
+=======================+=============================================+=======================+
| 🔑                    | pbx_device_profile_keys_pkey                | ON id                 |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_device_profile_keys_profile_id_5c98872a | ON profile_id         |
+-----------------------+---------------------------------------------+-----------------------+

.. _foreign-keys-34:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                                         |
+=======================+=======================================================+============================================================================================+
|                       | pbx_device_profile_k_profile_id_5c98872a_fk_pbx_devic | ( profile_id ) ref `public.pbx_device_profiles <#table-public-pbx-device-profiles>`__ (id) |
+-----------------------+-------------------------------------------------------+--------------------------------------------------------------------------------------------+

Table public.pbx_device_profile_settings
========================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\*      name         varchar(64)
\       value        varchar(254)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ profile_id   uuid
======= ============ ============

.. _Indexes-44:

**Indexes**


+-----------------------+-------------------------------------------------+-----------------------+
| Type                  | Name                                            | On                    |
+=======================+=================================================+=======================+
| 🔑                    | pbx_device_profile_settings_pkey                | ON id                 |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔎                    | pbx_device_profile_settings_profile_id_241770f9 | ON profile_id         |
+-----------------------+-------------------------------------------------+-----------------------+

.. _foreign-keys-35:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                                         |
+=======================+=======================================================+============================================================================================+
|                       | pbx_device_profile_s_profile_id_241770f9_fk_pbx_devic | ( profile_id ) ref `public.pbx_device_profiles <#table-public-pbx-device-profiles>`__ (id) |
+-----------------------+-------------------------------------------------------+--------------------------------------------------------------------------------------------+

Table public.pbx_device_profiles
================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(64)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
🔎 ⬈    domain_id_id uuid
🔎 ⬈    vendor_id    uuid
======= ============ ============

.. _Indexes-45:

**Indexes**


+-----------------------+-------------------------------------------+-----------------------+
| Type                  | Name                                      | On                    |
+=======================+===========================================+=======================+
| 🔑                    | pbx_device_profiles_pkey                  | ON id                 |
+-----------------------+-------------------------------------------+-----------------------+
| 🔎                    | pbx_device_profiles_domain_id_id_4067cb40 | ON domain_id_id       |
+-----------------------+-------------------------------------------+-----------------------+
| 🔎                    | pbx_device_profiles_vendor_id_95ae1fd9    | ON vendor_id          |
+-----------------------+-------------------------------------------+-----------------------+

.. _foreign-keys-36:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Type                  | Name                                                            | On                                                                                      |
+=======================+=================================================================+=========================================================================================+
|                       | pbx_device_profiles_domain_id_id_4067cb40_fk_pbx_domains_id     | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id)            |
+-----------------------+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
|                       | pbx_device_profiles_vendor_id_95ae1fd9_fk_pbx_device_vendors_id | ( vendor_id ) ref `public.pbx_device_vendors <#table-public-pbx-device-vendors>`__ (id) |
+-----------------------+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------+

Table public.pbx_device_settings
================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\*      name         varchar(64)
\       value        varchar(254)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ device_id    uuid
======= ============ ============

.. _Indexes-46:

**Indexes**


==== ====================================== ============
Type Name                                   On
==== ====================================== ============
🔑   pbx_device_settings_pkey               ON id
🔎   pbx_device_settings_device_id_12903bad ON device_id
==== ====================================== ============

.. _foreign-keys-37:

**Foreign Keys**


+-----------------------+----------------------------------------------------------+---------------------------------------------------------------------------+
| Type                  | Name                                                     | On                                                                        |
+=======================+==========================================================+===========================================================================+
|                       | pbx_device_settings_device_id_12903bad_fk_pbx_devices_id | ( device_id ) ref `public.pbx_devices <#table-public-pbx-devices>`__ (id) |
+-----------------------+----------------------------------------------------------+---------------------------------------------------------------------------+

Table public.pbx_device_vendor_function_groups
==============================================

======= ============ ===========
Idx     Name         Data Type
======= ============ ===========
\* 🔑   id           uuid
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ function_id  uuid
\* 🔎 ⬈ group_id     integer
======= ============ ===========

.. _Indexes-47:

**Indexes**


+-----------------------+--------------------------------------------------------+-----------------------+
| Type                  | Name                                                   | On                    |
+=======================+========================================================+=======================+
| 🔑                    | pbx_device_vendor_function_groups_pkey                 | ON id                 |
+-----------------------+--------------------------------------------------------+-----------------------+
| 🔎                    | pbx_device_vendor_function_groups_function_id_ea1e5a9b | ON function_id        |
+-----------------------+--------------------------------------------------------+-----------------------+
| 🔎                    | pbx_device_vendor_function_groups_group_id_67a203de    | ON group_id           |
+-----------------------+--------------------------------------------------------+-----------------------+

.. _foreign-keys-38:

**Foreign Keys**


+-----------------------+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Type                  | Name                                                   | On                                                                                                          |
+=======================+========================================================+=============================================================================================================+
|                       | pbx_device_vendor_fu_function_id_ea1e5a9b_fk_pbx_devic | ( function_id ) ref `public.pbx_device_vendor_functions <#table-public-pbx-device-vendor-functions>`__ (id) |
+-----------------------+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
|                       | pbx_device_vendor_fu_group_id_67a203de_fk_auth_grou    | ( group_id ) ref `public.auth_group <#auth_group>`__ (id)                                                   |
+-----------------------+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

Table public.pbx_device_vendor_functions
========================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(64)
\       value        varchar(254)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ vendor_id    uuid
======= ============ ============

.. _Indexes-48:

**Indexes**


+-----------------------+------------------------------------------------+-----------------------+
| Type                  | Name                                           | On                    |
+=======================+================================================+=======================+
| 🔑                    | pbx_device_vendor_functions_pkey               | ON id                 |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_device_vendor_functions_vendor_id_949d5c05 | ON vendor_id          |
+-----------------------+------------------------------------------------+-----------------------+

.. _foreign-keys-39:

**Foreign Keys**


+-----------------------+------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Type                  | Name                                                 | On                                                                                      |
+=======================+======================================================+=========================================================================================+
|                       | pbx_device_vendor_fu_vendor_id_949d5c05_fk_pbx_devic | ( vendor_id ) ref `public.pbx_device_vendors <#table-public-pbx-device-vendors>`__ (id) |
+-----------------------+------------------------------------------------------+-----------------------------------------------------------------------------------------+

Table public.pbx_device_vendors
===============================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(64)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ============

.. _Indexes-49:

**Indexes**


==== ======================= =====
Type Name                    On
==== ======================= =====
🔑   pbx_device_vendors_pkey ON id
==== ======================= =====

Table public.pbx_devices
========================

======= ================== ============
Idx     Name               Data Type
======= ================== ============
\* 🔑 ⬋ id                 uuid
\*      mac_address        varchar(24)
\       label              varchar(64)
\       model              varchar(64)
\       firmware_version   varchar(64)
\       template           varchar(254)
\       username           varchar(32)
\       password           varchar(32)
\       provisioned_date   timestamptz
\       provisioned_method varchar(16)
\*      enabled            varchar(8)
\       description        varchar(254)
🔍      provisioned_ip     inet
\       created            timestamptz
\       updated            timestamptz
\       synchronised       timestamptz
\*      updated_by         varchar(64)
🔎 ⬈    domain_id_id       uuid
🔎 ⬈    profile_id_id      uuid
🔎 ⬈    user_id_id         bigint
🔎 ⬈    vendor_id          uuid
======= ================== ============

.. _Indexes-50:

**Indexes**


==== ================================== =================
Type Name                               On
==== ================================== =================
🔑   pbx_devices_pkey                   ON id
🔎   pbx_devices_domain_id_id_10d0954a  ON domain_id_id
🔎   pbx_devices_profile_id_id_d05f3c63 ON profile_id_id
🔎   pbx_devices_user_id_id_bd7443ea    ON user_id_id
🔎   pbx_devices_vendor_id_63e85b1c     ON vendor_id
==== ================================== =================

.. _foreign-keys-40:

**Foreign Keys**


+-----------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Type                  | Name                                                         | On                                                                                            |
+=======================+==============================================================+===============================================================================================+
|                       | pbx_devices_vendor_id_63e85b1c_fk_pbx_device_vendors_id      | ( vendor_id ) ref `public.pbx_device_vendors <#table-public-pbx-device-vendors>`__ (id)       |
+-----------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                       | pbx_devices_domain_id_id_10d0954a_fk_pbx_domains_id          | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id)                  |
+-----------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                       | pbx_devices_profile_id_id_d05f3c63_fk_pbx_device_profiles_id | ( profile_id_id ) ref `public.pbx_device_profiles <#table-public-pbx-device-profiles>`__ (id) |
+-----------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                       | pbx_devices_user_id_id_bd7443ea_fk_pbx_users_id              | ( user_id_id ) ref `public.pbx_users <#table-public-pbx-users>`__ (id)                        |
+-----------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

Table public.pbx_dialplan_details
=================================

======= ============== ============
Idx     Name           Data Type
======= ============== ============
\* 🔑   id             uuid
\*      tag            varchar(32)
\       type           varchar(128)
\       data           varchar(512)
\       dp_break       varchar(8)
\       inline         varchar(8)
\*      group          numeric(11)
\*      sequence       numeric(11)
\       created        timestamptz
\       updated        timestamptz
\       synchronised   timestamptz
\*      updated_by     varchar(64)
\* 🔎 ⬈ dialplan_id_id uuid
======= ============== ============

.. _Indexes-51:

**Indexes**


+-----------------------+----------------------------------------------+-----------------------+
| Type                  | Name                                         | On                    |
+=======================+==============================================+=======================+
| 🔑                    | pbx_dialplan_details_pkey                    | ON id                 |
+-----------------------+----------------------------------------------+-----------------------+
| 🔎                    | pbx_dialplan_details_dialplan_id_id_eb4dbc17 | ON dialplan_id_id     |
+-----------------------+----------------------------------------------+-----------------------+

.. _foreign-keys-41:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                 |
+=======================+===========================================================+====================================================================================+
|                       | pbx_dialplan_details_dialplan_id_id_eb4dbc17_fk_pbx_dialp | ( dialplan_id_id ) ref `public.pbx_dialplans <#table-public-pbx-dialplans>`__ (id) |
+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+

Table public.pbx_dialplans
==========================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\       app_id       uuid
🔎      hostname     varchar(128)
🔎      context      varchar(128)
🔎      category     varchar(32)
\       name         varchar(64)
\       number       varchar(32)
\* 🔎   destination  varchar(8)
\*      dp_continue  varchar(8)
\       xml          text
\*      sequence     numeric(3)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
🔎 ⬈    domain_id_id uuid
======= ============ ============

.. _Indexes-52:

**Indexes**


==== ======================================= ===============
Type Name                                    On
==== ======================================= ===============
🔑   pbx_dialplans_pkey                      ON id
🔎   pbx_dialplans_domain_id_id_581e14be     ON domain_id_id
🔎   pbx_dialplans_category_62ff80d9         ON category
🔎   pbx_dialplans_category_62ff80d9_like    ON category
🔎   pbx_dialplans_context_9f65b37d          ON context
🔎   pbx_dialplans_context_9f65b37d_like     ON context
🔎   pbx_dialplans_destination_bb1c9803      ON destination
🔎   pbx_dialplans_destination_bb1c9803_like ON destination
🔎   pbx_dialplans_hostname_0e8300e2         ON hostname
🔎   pbx_dialplans_hostname_0e8300e2_like    ON hostname
==== ======================================= ===============

.. _foreign-keys-42:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                           |
+=======================+=======================================================+==============================================================================+
|                       | pbx_dialplans_domain_id_id_581e14be_fk_pbx_domains_id | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------------+

Table public.pbx_domain_settings
================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\       app_uuid     uuid
\* 🔎   category     varchar(32)
\* 🔎   subcategory  varchar(64)
\* 🔎   value_type   varchar(32)
\       value        varchar(254)
\*      sequence     numeric(11)
\*      enabled      varchar(8)
\       description  varchar(128)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ domain_id_id uuid
======= ============ ============

.. _Indexes-53:

**Indexes**


+-----------------------+-----------------------------------------------+-----------------------+
| Type                  | Name                                          | On                    |
+=======================+===============================================+=======================+
| 🔑                    | pbx_domain_settings_pkey                      | ON id                 |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_domain_settings_domain_id_id_c7461c47     | ON domain_id_id       |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_domain_settings_category_b8b72e31         | ON category           |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_domain_settings_category_b8b72e31_like    | ON category           |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_domain_settings_value_type_41f42703       | ON value_type         |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_domain_settings_value_type_41f42703_like  | ON value_type         |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_domain_settings_subcategory_db5affbb      | ON subcategory        |
+-----------------------+-----------------------------------------------+-----------------------+
| 🔎                    | pbx_domain_settings_subcategory_db5affbb_like | ON subcategory        |
+-----------------------+-----------------------------------------------+-----------------------+

.. _foreign-keys-43:

**Foreign Keys**


+-----------------------+-------------------------------------------------------------+------------------------------------------------------------------------------+
| Type                  | Name                                                        | On                                                                           |
+=======================+=============================================================+==============================================================================+
|                       | pbx_domain_settings_domain_id_id_c7461c47_fk_pbx_domains_id | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-------------------------------------------------------------+------------------------------------------------------------------------------+

Table public.pbx_domains
========================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\* 🔍   name         varchar(128)
\*      enabled      varchar(8)
\       description  varchar(128)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ============

.. _Indexes-54:

**Indexes**


==== ============================== =======
Type Name                           On
==== ============================== =======
🔑   pbx_domains_pkey               ON id
🔍   pbx_domains_name_key           ON name
🔎   pbx_domains_name_ce0c9e76_like ON name
==== ============================== =======

Table public.pbx_email_templates
================================

===== ============ ============
Idx   Name         Data Type
===== ============ ============
\* 🔑 id           uuid
\*    language     varchar(8)
\*    category     varchar(32)
\*    subcategory  varchar(32)
\     subject      varchar(128)
\*    type         varchar(8)
\     body         text
\*    enabled      varchar(8)
\     description  varchar(254)
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
🔎 ⬈  domain_id_id uuid
===== ============ ============

.. _Indexes-55:

**Indexes**


+-----------------------+-------------------------------------------+-----------------------+
| Type                  | Name                                      | On                    |
+=======================+===========================================+=======================+
| 🔑                    | pbx_email_templates_pkey                  | ON id                 |
+-----------------------+-------------------------------------------+-----------------------+
| 🔎                    | pbx_email_templates_domain_id_id_592ee910 | ON domain_id_id       |
+-----------------------+-------------------------------------------+-----------------------+

.. _foreign-keys-44:

**Foreign Keys**


+-----------------------+-------------------------------------------------------------+------------------------------------------------------------------------------+
| Type                  | Name                                                        | On                                                                           |
+=======================+=============================================================+==============================================================================+
|                       | pbx_email_templates_domain_id_id_592ee910_fk_pbx_domains_id | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-------------------------------------------------------------+------------------------------------------------------------------------------+

Table public.pbx_extension_users
================================

.. _pbx_extension_users:

===== ============== ===========
Idx   Name           Data Type
===== ============== ===========
\* 🔑 id             uuid
\     created        timestamptz
\     updated        timestamptz
\     synchronised   timestamptz
\*    updated_by     varchar(64)
🔎 ⬈  extension_uuid uuid
🔎 ⬈  user_uuid      uuid
\*    default_user   varchar(8)
===== ============== ===========

.. _Indexes-56:

**Indexes**


+-----------------------+---------------------------------------------+-----------------------+
| Type                  | Name                                        | On                    |
+=======================+=============================================+=======================+
| 🔑                    | pbx_extension_users_pkey                    | ON id                 |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_extension_users_extension_uuid_68cf4da0 | ON extension_uuid     |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_extension_users_user_uuid_c416d33e      | ON user_uuid          |
+-----------------------+---------------------------------------------+-----------------------+

.. _foreign-keys-45:

**Foreign Keys**


+-----------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Type                  | Name                                                          | On                                                                                   |
+=======================+===============================================================+======================================================================================+
|                       | pbx_extension_users_extension_uuid_68cf4da0_fk_pbx_exten      | ( extension_uuid ) ref `public.pbx_extensions <#table-public-pbx-extensions>`__ (id) |
+-----------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------+
|                       | pbx_extension_users_user_uuid_c416d33e_fk_pbx_users_user_uuid | ( user_uuid ) ref `public.pbx_users <#table-public-pbx-users>`__ (user_uuid)         |
+-----------------------+---------------------------------------------------------------+--------------------------------------------------------------------------------------+

Table public.pbx_extensions
===========================

.. _pbx_extensions:

======= ======================================= ============
Idx     Name                                    Data Type
======= ======================================= ============
\* 🔑 ⬋ id                                      uuid
\* 🔍   extension                               varchar(32)
🔍      number_alias                            varchar(16)
\*      password                                varchar(32)
\       accountcode                             varchar(32)
\       effective_caller_id_name                varchar(32)
\       effective_caller_id_number              varchar(16)
\       outbound_caller_id_name                 varchar(32)
\       outbound_caller_id_number               varchar(16)
\       emergency_caller_id_name                varchar(32)
\       emergency_caller_id_number              varchar(16)
\       directory_first_name                    varchar(32)
\       directory_last_name                     varchar(32)
\*      directory_visible                       varchar(8)
\*      directory_exten_visible                 varchar(8)
\       limit_max                               numeric(11)
\       limit_destination                       varchar(32)
\       missed_call_app                         varchar(32)
\       missed_call_data                        varchar(256)
\       user_context                            varchar(128)
\       toll_allow                              varchar(32)
\       call_timeout                            numeric(11)
\       call_group                              varchar(32)
\*      call_screen_enabled                     varchar(8)
\       user_record                             varchar(8)
\       hold_music                              varchar(64)
\       auth_acl                                varchar(16)
\       cidr                                    varchar(128)
\       sip_force_contact                       varchar(64)
\       nibble_account                          numeric(1)
\       sip_force_expires                       numeric(11)
\       mwi_account                             varchar(256)
\       sip_bypass_media                        varchar(32)
\       unique_id                               numeric(1)
\       dial_string                             text
\       dial_user                               varchar(32)
\       dial_domain                             varchar(128)
\*      do_not_disturb                          varchar(8)
\       forward_all_destination                 varchar(16)
\*      forward_all_enabled                     varchar(8)
\       forward_busy_destination                varchar(16)
\*      forward_busy_enabled                    varchar(8)
\       forward_no_answer_destination           varchar(16)
\*      forward_no_answer_enabled               varchar(8)
\       forward_user_not_registered_destination varchar(16)
\*      forward_user_not_registered_enabled     varchar(8)
\       follow_me_uuid                          uuid
\       forward_caller_id                       varchar(16)
\*      follow_me_enabled                       varchar(8)
\       follow_me_destinations                  text
\*      enabled                                 varchar(8)
\       description                             varchar(64)
\       absolute_codec_string                   varchar(64)
\*      force_ping                              varchar(8)
\       created                                 timestamptz
\       updated                                 timestamptz
\       synchronised                            timestamptz
\*      updated_by                              varchar(64)
🔍 ⬈    domain_uuid                             uuid
======= ======================================= ============

.. _Indexes-57:

**Indexes**


+-----------------------+-------------------------------------------------------+------------------------------+
| Type                  | Name                                                  | On                           |
+=======================+=======================================================+==============================+
| 🔑                    | pbx_extensions_pkey                                   | ON id                        |
+-----------------------+-------------------------------------------------------+------------------------------+
| 🔍                    | pbx_extensions_domain_uuid_extension_8ef2eb2b_uniq    | ON domain_uuid, extension    |
+-----------------------+-------------------------------------------------------+------------------------------+
| 🔍                    | pbx_extensions_domain_uuid_number_alias_64dbcbb9_uniq | ON domain_uuid, number_alias |
+-----------------------+-------------------------------------------------------+------------------------------+
| 🔎                    | pbx_extensions_domain_uuid_246c1b36                   | ON domain_uuid               |
+-----------------------+-------------------------------------------------------+------------------------------+
| 🔎                    | pbx_extensions_extension_8d76e869                     | ON extension                 |
+-----------------------+-------------------------------------------------------+------------------------------+
| 🔎                    | pbx_extensions_extension_8d76e869_like                | ON extension                 |
+-----------------------+-------------------------------------------------------+------------------------------+
| 🔎                    | pbx_extensions_number_alias_9f983a90                  | ON number_alias              |
+-----------------------+-------------------------------------------------------+------------------------------+
| 🔎                    | pbx_extensions_number_alias_9f983a90_like             | ON number_alias              |
+-----------------------+-------------------------------------------------------+------------------------------+

.. _foreign-keys-46:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                          |
+=======================+=======================================================+=============================================================================+
|                       | pbx_extensions_domain_uuid_246c1b36_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_failed_logins
==============================

===== ============ ============
Idx   Name         Data Type
===== ============ ============
\* 🔑 id           uuid
\* 🔍 address      inet
\     username     varchar(254)
\*    attempts     numeric(4)
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
===== ============ ============

.. _Indexes-58:

**Indexes**


==== ============================= ==========
Type Name                          On
==== ============================= ==========
🔑   pbx_failed_logins_pkey        ON id
🔍   pbx_failed_logins_address_key ON address
==== ============================= ==========

Table public.pbx_follow_me_destinations
=======================================

===== ============== ===========
Idx   Name           Data Type
===== ============== ===========
\* 🔑 id             uuid
\*    destination    varchar(32)
\*    delay          numeric(3)
\*    timeout        numeric(3)
\     prompt         varchar(8)
\     sequence       numeric(11)
\     created        timestamptz
\     updated        timestamptz
\     synchronised   timestamptz
\*    updated_by     varchar(64)
🔎 ⬈  extension_uuid uuid
===== ============== ===========

.. _Indexes-59:

**Indexes**


+-----------------------+----------------------------------------------------+-----------------------+
| Type                  | Name                                               | On                    |
+=======================+====================================================+=======================+
| 🔑                    | pbx_follow_me_destinations_pkey                    | ON id                 |
+-----------------------+----------------------------------------------------+-----------------------+
| 🔎                    | pbx_follow_me_destinations_extension_uuid_7a65cb1a | ON extension_uuid     |
+-----------------------+----------------------------------------------------+-----------------------+

.. _foreign-keys-47:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                   |
+=======================+===========================================================+======================================================================================+
|                       | pbx_follow_me_destin_extension_uuid_7a65cb1a_fk_pbx_exten | ( extension_uuid ) ref `public.pbx_extensions <#table-public-pbx-extensions>`__ (id) |
+-----------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------+

Table public.pbx_gateways
=========================

===== ==================== ============
Idx   Name                 Data Type
===== ==================== ============
\* 🔑 id                   uuid
\*    gateway              varchar(32)
\     username             varchar(32)
\     password             varchar(32)
\     distinct_to          varchar(8)
\     auth_username        varchar(32)
\     realm                varchar(128)
\     from_user            varchar(32)
\     from_domain          varchar(128)
\*    proxy                varchar(128)
\     register_proxy       varchar(128)
\     outbound_proxy       varchar(128)
\*    expire_seconds       numeric(5)
\*    register             varchar(8)
\     register_transport   varchar(8)
\*    retry_seconds        numeric(4)
\     extension            varchar(32)
\     ping                 varchar(8)
\     caller_id_in_from    varchar(8)
\     supress_cng          varchar(8)
\     sip_cid_type         varchar(8)
\     codec_prefs          varchar(34)
\*    channels             numeric(4)
\     extension_in_contact varchar(8)
\*    context              varchar(128)
\*    profile              varchar(64)
\     hostname             varchar(128)
\*    enabled              varchar(8)
\     description          varchar(64)
\     created              timestamptz
\     updated              timestamptz
\     synchronised         timestamptz
\*    updated_by           varchar(64)
🔎 ⬈  domain_uuid          uuid
===== ==================== ============

.. _Indexes-60:

**Indexes**


==== ================================= ==============
Type Name                              On
==== ================================= ==============
🔑   pbx_gateways_pkey                 ON id
🔎   pbx_gateways_domain_uuid_08cbf6c7 ON domain_uuid
==== ================================= ==============

.. _foreign-keys-48:

**Foreign Keys**


+-----------------------+-----------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                | On                                                                          |
+=======================+=====================================================+=============================================================================+
|                       | pbx_gateways_domain_uuid_08cbf6c7_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-----------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_httapi_session
===============================

===== ======= ===========
Idx   Name    Data Type
===== ======= ===========
\* 🔑 id      uuid
\*    name    varchar(32)
\     xml     text
\     json    jsonb
\     created timestamptz
===== ======= ===========

.. _Indexes-61:

**Indexes**


==== ======================= =====
Type Name                    On
==== ======================= =====
🔑   pbx_httapi_session_pkey ON id
==== ======================= =====

Table public.pbx_ip_register
============================

===== ============ ===========
Idx   Name         Data Type
===== ============ ===========
\* 🔑 id           uuid
\* 🔍 address      inet
\*    status       numeric(2)
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
===== ============ ===========

.. _Indexes-62:

**Indexes**


==== =========================== ==========
Type Name                        On
==== =========================== ==========
🔑   pbx_ip_register_pkey        ON id
🔍   pbx_ip_register_address_key ON address
==== =========================== ==========

Table public.pbx_ivr_menu_options
=================================

======= ============== ============
Idx     Name           Data Type
======= ============== ============
\* 🔑   id             uuid
\       option_digits  varchar(8)
\       option_action  varchar(64)
\*      option_param   varchar(128)
\*      sequence       numeric(3)
\       description    varchar(64)
\       created        timestamptz
\       updated        timestamptz
\       synchronised   timestamptz
\*      updated_by     varchar(64)
\* 🔎 ⬈ ivr_menu_id_id uuid
======= ============== ============

.. _Indexes-63:

**Indexes**


+-----------------------+----------------------------------------------+-----------------------+
| Type                  | Name                                         | On                    |
+=======================+==============================================+=======================+
| 🔑                    | pbx_ivr_menu_options_pkey                    | ON id                 |
+-----------------------+----------------------------------------------+-----------------------+
| 🔎                    | pbx_ivr_menu_options_ivr_menu_id_id_596a92af | ON ivr_menu_id_id     |
+-----------------------+----------------------------------------------+-----------------------+

.. _foreign-keys-49:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                 |
+=======================+===========================================================+====================================================================================+
|                       | pbx_ivr_menu_options_ivr_menu_id_id_596a92af_fk_pbx_ivr_m | ( ivr_menu_id_id ) ref `public.pbx_ivr_menus <#table-public-pbx-ivr-menus>`__ (id) |
+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+

Table public.pbx_ivr_menus
==========================

======= =================== ============
Idx     Name                Data Type
======= =================== ============
\* 🔑 ⬋ id                  uuid
\       dialplan_id         uuid
\       name                varchar(64)
\*      extension           varchar(32)
\       language            varchar(32)
\       greet_long          varchar(254)
\       greet_short         varchar(254)
\       invalid_sound       varchar(254)
\       exit_sound          varchar(254)
\       confirm_macro       varchar(254)
\       confirm_key         varchar(8)
\       tts_engine          varchar(64)
\       tts_voice           varchar(254)
\*      confirm_attempts    numeric(2)
\*      timeout             numeric(5)
\       exit_app            varchar(32)
\       exit_data           varchar(256)
\*      inter_digit_timeout numeric(5)
\*      max_failiures       numeric(2)
\*      max_timeouts        numeric(2)
\*      digit_len           numeric(2)
\*      direct_dial         varchar(8)
\       ringback            varchar(128)
\       cid_prefix          varchar(32)
🔎      context             varchar(128)
\*      enabled             varchar(8)
\       description         varchar(64)
\       created             timestamptz
\       updated             timestamptz
\       synchronised        timestamptz
\*      updated_by          varchar(64)
🔎 ⬈    domain_uuid         uuid
======= =================== ============

.. _Indexes-64:

**Indexes**


==== =================================== ==============
Type Name                                On
==== =================================== ==============
🔑   pbx_ivr_menus_pkey                  ON id
🔎   pbx_ivr_menus_context_23574173      ON context
🔎   pbx_ivr_menus_context_23574173_like ON context
🔎   pbx_ivr_menus_domain_uuid_82c2bc95  ON domain_uuid
==== =================================== ==============

.. _foreign-keys-50:

**Foreign Keys**


+-----------------------+------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                 | On                                                                          |
+=======================+======================================================+=============================================================================+
|                       | pbx_ivr_menus_domain_uuid_82c2bc95_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_menu_item_groups
=================================

======= ============ ===========
Idx     Name         Data Type
======= ============ ===========
\* 🔑   id           uuid
\       name         varchar(64)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ group_id     integer
\* 🔎 ⬈ menu_item_id uuid
======= ============ ===========

.. _Indexes-65:

**Indexes**


+-----------------------+--------------------------------------------+-----------------------+
| Type                  | Name                                       | On                    |
+=======================+============================================+=======================+
| 🔑                    | pbx_menu_item_groups_pkey                  | ON id                 |
+-----------------------+--------------------------------------------+-----------------------+
| 🔎                    | pbx_menu_item_groups_group_id_727cd142     | ON group_id           |
+-----------------------+--------------------------------------------+-----------------------+
| 🔎                    | pbx_menu_item_groups_menu_item_id_c543d3d6 | ON menu_item_id       |
+-----------------------+--------------------------------------------+-----------------------+

.. _foreign-keys-51:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| Type                  | Name                                                            | On                                                                                 |
+=======================+=================================================================+====================================================================================+
|                       | pbx_menu_item_groups_group_id_727cd142_fk_auth_group_id         | ( group_id ) ref `public.auth_group <#table-public-auth-group>`__ (id)             |
+-----------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
|                       | pbx_menu_item_groups_menu_item_id_c543d3d6_fk_pbx_menu_items_id | ( menu_item_id ) ref `public.pbx_menu_items <#table-public-pbx-menu_items>`__ (id) |
+-----------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------+

Table public.pbx_menu_items
===========================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      title        varchar(64)
\       link         varchar(128)
\       icon         varchar(32)
\*      category     varchar(16)
\*      protected    varchar(8)
\*      sequence     numeric(11)
\*      description  varchar(128)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ menu_id      uuid
🔎 ⬈    parent_id    uuid
======= ============ ============

.. _Indexes-66:

**Indexes**


==== ================================= ============
Type Name                              On
==== ================================= ============
🔑   pbx_menu_items_pkey               ON id
🔎   pbx_menu_items_menu_id_a8e4817b   ON menu_id
🔎   pbx_menu_items_parent_id_c68849bb ON parent_id
==== ================================= ============

.. _foreign-keys-52:

**Foreign Keys**


+-----------------------+--------------------------------------------------------+---------------------------------------------------------------------------------+
| Type                  | Name                                                   | On                                                                              |
+=======================+========================================================+=================================================================================+
|                       | pbx_menu_items_menu_id_a8e4817b_fk_pbx_menus_id        | ( menu_id ) ref `public.pbx_menus <#table-public-pbx-menus>`__ (id)             |
+-----------------------+--------------------------------------------------------+---------------------------------------------------------------------------------+
|                       | pbx_menu_items_parent_id_c68849bb_fk_pbx_menu_items_id | ( parent_id ) ref `public.pbx_menu_items <#table-public-pbx-menu-items>`__ (id) |
+-----------------------+--------------------------------------------------------+---------------------------------------------------------------------------------+

Table public.pbx_menus
======================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(64)
\*      description  varchar(128)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ============

.. _Indexes-67:

**Indexes**


==== ============== =====
Type Name           On
==== ============== =====
🔑   pbx_menus_pkey ON id
==== ============== =====

Table public.pbx_modules
========================

===== =============== ============
Idx   Name            Data Type
===== =============== ============
\* 🔑 id              uuid
\*    label           varchar(64)
\*    name            varchar(64)
\*    category        varchar(64)
\*    sequence        numeric(11)
\*    enabled         varchar(8)
\*    default_enabled varchar(8)
\     description     varchar(254)
\     created         timestamptz
\     updated         timestamptz
\     synchronised    timestamptz
\*    updated_by      varchar(64)
===== =============== ============

.. _Indexes-68:

**Indexes**


==== ================ =====
Type Name             On
==== ================ =====
🔑   pbx_modules_pkey ON id
==== ================ =====

Table public.pbx_music_on_hold
==============================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(32)
\*      path         varchar(256)
\*      rate         numeric(11)
\*      shuffle      varchar(8)
\       channels     numeric(11)
\       interval     numeric(11)
\*      timer_name   varchar(32)
\       chime_list   varchar(64)
\       chime_freq   numeric(11)
\       chime_max    numeric(11)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
🔎 ⬈    domain_uuid  uuid
======= ============ ============

.. _Indexes-69:

**Indexes**


==== ====================================== ==============
Type Name                                   On
==== ====================================== ==============
🔑   pbx_music_on_hold_pkey                 ON id
🔎   pbx_music_on_hold_domain_uuid_f5d415b6 ON domain_uuid
==== ====================================== ==============

.. _foreign-keys-53:

**Foreign Keys**


+-----------------------+----------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                     | On                                                                          |
+=======================+==========================================================+=============================================================================+
|                       | pbx_music_on_hold_domain_uuid_f5d415b6_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+----------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_music_on_hold_files
====================================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\*      filename     text
\*      file_name    varchar(256)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ moh_id_id    uuid
======= ============ ============

.. _Indexes-70:

**Indexes**


+-----------------------+--------------------------------------------+-----------------------+
| Type                  | Name                                       | On                    |
+=======================+============================================+=======================+
| 🔑                    | pbx_music_on_hold_files_pkey               | ON id                 |
+-----------------------+--------------------------------------------+-----------------------+
| 🔎                    | pbx_music_on_hold_files_moh_id_id_2ed7958f | ON moh_id_id          |
+-----------------------+--------------------------------------------+-----------------------+

.. _foreign-keys-54:

**Foreign Keys**


+-----------------------+------------------------------------------------------+---------------------------------------------------------------------------------------+
| Type                  | Name                                                 | On                                                                                    |
+=======================+======================================================+=======================================================================================+
|                       | pbx_music_on_hold_fi_moh_id_id_2ed7958f_fk_pbx_music | ( moh_id_id ) ref `public.pbx_music_on_hold <#table-public-pbx-music-on-hold>`__ (id) |
+-----------------------+------------------------------------------------------+---------------------------------------------------------------------------------------+

Table public.pbx_number_translation_details
===========================================

======= ======================== ============
Idx     Name                     Data Type
======= ======================== ============
\* 🔑   id                       uuid
\       td_regex                 varchar(128)
\       td_replace               varchar(128)
\*      td_order                 numeric(3)
\       created                  timestamptz
\       updated                  timestamptz
\       synchronised             timestamptz
\*      updated_by               varchar(64)
\* 🔎 ⬈ number_translation_id_id uuid
======= ======================== ============

.. _Indexes-71:

**Indexes**


+-----------------------+--------------------------------------------------------------+-----------------------------+
| Type                  | Name                                                         | On                          |
+=======================+==============================================================+=============================+
| 🔑                    | pbx_number_translation_details_pkey                          | ON id                       |
+-----------------------+--------------------------------------------------------------+-----------------------------+
| 🔎                    | pbx_number_translation_det_number_translation_id_id_c92ec084 | ON number_translation_id_id |
+-----------------------+--------------------------------------------------------------+-----------------------------+

.. _foreign-keys-55:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Type                  | Name                                                            | On                                                                                                               |
+=======================+=================================================================+==================================================================================================================+
|                       | pbx_number_translati_number_translation_i_c92ec084_fk_pbx_numbe | ( number_translation_id_id ) ref `public.pbx_number_translations <#table-public-pbx-number-translations>`__ (id) |
+-----------------------+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

Table public.pbx_number_translations
====================================

======= ============ ===========
Idx     Name         Data Type
======= ============ ===========
\* 🔑 ⬋ id           uuid
\       name         varchar(64)
\*      enabled      varchar(8)
\       description  varchar(64)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ===========

.. _Indexes-72:

**Indexes**


==== ============================ =====
Type Name                         On
==== ============================ =====
🔑   pbx_number_translations_pkey ON id
==== ============================ =====

Table public.pbx_phrase_details
===============================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\*      pfunction    varchar(16)
\       data         varchar(254)
\*      sequence     numeric(11)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ phrase_id_id uuid
======= ============ ============

.. _Indexes-73:

**Indexes**


+-----------------------+------------------------------------------+-----------------------+
| Type                  | Name                                     | On                    |
+=======================+==========================================+=======================+
| 🔑                    | pbx_phrase_details_pkey                  | ON id                 |
+-----------------------+------------------------------------------+-----------------------+
| 🔎                    | pbx_phrase_details_phrase_id_id_b0a5c23d | ON phrase_id_id       |
+-----------------------+------------------------------------------+-----------------------+

.. _foreign-keys-56:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                           |
+=======================+============================================================+==============================================================================+
|                       | pbx_phrase_details_phrase_id_id_b0a5c23d_fk_pbx_phrases_id | ( phrase_id_id ) ref `public.pbx_phrases <#table-public-pbx-phrases>`__ (id) |
+-----------------------+------------------------------------------------------------+------------------------------------------------------------------------------+

Table public.pbx_phrases
========================

======= ============ ===========
Idx     Name         Data Type
======= ============ ===========
\* 🔑 ⬋ id           uuid
\       name         varchar(64)
\*      language     varchar(8)
\*      enabled      varchar(8)
\       description  varchar(64)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
🔎 ⬈    domain_uuid  uuid
======= ============ ===========

.. _Indexes-74:

**Indexes**


==== ================================ ==============
Type Name                             On
==== ================================ ==============
🔑   pbx_phrases_pkey                 ON id
🔎   pbx_phrases_domain_uuid_3e4927b6 ON domain_uuid
==== ================================ ==============

.. _foreign-keys-57:

**Foreign Keys**


+-----------------------+----------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                               | On                                                                          |
+=======================+====================================================+=============================================================================+
|                       | pbx_phrases_domain_uuid_3e4927b6_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+----------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_recordings
===========================

===== ============ ============
Idx   Name         Data Type
===== ============ ============
\* 🔑 id           uuid
\*    filename     text
\*    name         varchar(64)
\     description  varchar(128)
\     base64       text
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
🔎 ⬈  domain_uuid  uuid
===== ============ ============

.. _Indexes-75:

**Indexes**


==== =================================== ==============
Type Name                                On
==== =================================== ==============
🔑   pbx_recordings_pkey                 ON id
🔎   pbx_recordings_domain_uuid_e92a4731 ON domain_uuid
==== =================================== ==============

.. _foreign-keys-58:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                          |
+=======================+=======================================================+=============================================================================+
|                       | pbx_recordings_domain_uuid_e92a4731_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+-------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_ring_group_destinations
========================================

======= ================== ============
Idx     Name               Data Type
======= ================== ============
\* 🔑   id                 uuid
\*      number             varchar(128)
\*      delay              numeric(3)
\*      timeout            numeric(3)
\*      destination_prompt numeric(3)
\       created            timestamptz
\       updated            timestamptz
\       synchronised       timestamptz
\*      updated_by         varchar(64)
\* 🔎 ⬈ ring_group_id_id   uuid
======= ================== ============

.. _Indexes-76:

**Indexes**


+-----------------------+-------------------------------------------------------+-----------------------+
| Type                  | Name                                                  | On                    |
+=======================+=======================================================+=======================+
| 🔑                    | pbx_ring_group_destinations_pkey                      | ON id                 |
+-----------------------+-------------------------------------------------------+-----------------------+
| 🔎                    | pbx_ring_group_destinations_ring_group_id_id_b1dd9e79 | ON ring_group_id_id   |
+-----------------------+-------------------------------------------------------+-----------------------+

.. _foreign-keys-59:

**Foreign Keys**


+-----------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Type                  | Name                                                         | On                                                                                       |
+=======================+==============================================================+==========================================================================================+
|                       | pbx_ring_group_desti_ring_group_id_id_b1dd9e79_fk_pbx_ring\_ | ( ring_group_id_id ) ref `public.pbx_ring_groups <#table-public-pbx-ring-groups>`__ (id) |
+-----------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------------+

Table public.pbx_ring_group_users
=================================

======= ================ ===========
Idx     Name             Data Type
======= ================ ===========
\* 🔑   id               uuid
\       created          timestamptz
\       updated          timestamptz
\       synchronised     timestamptz
\*      updated_by       varchar(64)
\* 🔎 ⬈ ring_group_id_id uuid
🔎 ⬈    user_uuid        uuid
======= ================ ===========

.. _Indexes-77:

**Indexes**


+-----------------------+------------------------------------------------+-----------------------+
| Type                  | Name                                           | On                    |
+=======================+================================================+=======================+
| 🔑                    | pbx_ring_group_users_pkey                      | ON id                 |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_ring_group_users_ring_group_id_id_f248dec4 | ON ring_group_id_id   |
+-----------------------+------------------------------------------------+-----------------------+
| 🔎                    | pbx_ring_group_users_user_uuid_78082a94        | ON user_uuid          |
+-----------------------+------------------------------------------------+-----------------------+

.. _foreign-keys-60:

**Foreign Keys**


+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Type                  | Name                                                           | On                                                                                       |
+=======================+================================================================+==========================================================================================+
|                       | pbx_ring_group_users_ring_group_id_id_f248dec4_fk_pbx_ring\_   | ( ring_group_id_id ) ref `public.pbx_ring_groups <#table-public-pbx-ring-groups>`__ (id) |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------+
|                       | pbx_ring_group_users_user_uuid_78082a94_fk_pbx_users_user_uuid | ( user_uuid ) ref `public.pbx_users <#table-public-pbx-users>`__ (user_uuid)             |
+-----------------------+----------------------------------------------------------------+------------------------------------------------------------------------------------------+

Table public.pbx_ring_groups
============================

======= =================== ============
Idx     Name                Data Type
======= =================== ============
\* 🔑 ⬋ id                  uuid
\       name                varchar(64)
\*      extension           varchar(32)
\       greeting            varchar(254)
\       strategy            varchar(16)
\       timeout_app         varchar(32)
\       timeout_data        varchar(256)
\*      call_timeout        numeric(3)
\       caller_id_name      varchar(32)
\       caller_id_number    varchar(16)
\       cid_name_prefix     varchar(32)
\       cid_number_prefix   varchar(16)
\       distinctive_ring    varchar(32)
\       ring_group_ringback varchar(128)
\*      follow_me_enabled   varchar(8)
\       missed_call_app     varchar(32)
\       missed_call_data    varchar(256)
\*      forward_enabled     varchar(8)
\       forward_destination varchar(128)
\       forward_toll_allow  varchar(32)
🔎      context             varchar(128)
\*      enabled             varchar(8)
\       description         varchar(64)
\       dialplan_id         uuid
\       created             timestamptz
\       updated             timestamptz
\       synchronised        timestamptz
\*      updated_by          varchar(64)
🔎 ⬈    domain_uuid         uuid
======= =================== ============

.. _Indexes-78:

**Indexes**


==== ===================================== ==============
Type Name                                  On
==== ===================================== ==============
🔑   pbx_ring_groups_pkey                  ON id
🔎   pbx_ring_groups_context_378e5e39      ON context
🔎   pbx_ring_groups_context_378e5e39_like ON context
🔎   pbx_ring_groups_domain_uuid_8ee40c93  ON domain_uuid
==== ===================================== ==============

.. _foreign-keys-61:

**Foreign Keys**


+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------+
| Type                  | Name                                                   | On                                                                          |
+=======================+========================================================+=============================================================================+
|                       | pbx_ring_groups_domain_uuid_8ee40c93_fk_pbx_domains_id | ( domain_uuid ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+--------------------------------------------------------+-----------------------------------------------------------------------------+

Table public.pbx_sip_profile_domains
====================================

======= ============== ============
Idx     Name           Data Type
======= ============== ============
\* 🔑   id             uuid
\*      name           varchar(128)
\*      alias          varchar(8)
\*      parse          varchar(8)
\       created        timestamptz
\       updated        timestamptz
\       synchronised   timestamptz
\*      updated_by     varchar(64)
\* 🔎 ⬈ sip_profile_id uuid
======= ============== ============

.. _Indexes-79:

**Indexes**


+-----------------------+-------------------------------------------------+-----------------------+
| Type                  | Name                                            | On                    |
+=======================+=================================================+=======================+
| 🔑                    | pbx_sip_profile_domains_pkey                    | ON id                 |
+-----------------------+-------------------------------------------------+-----------------------+
| 🔎                    | pbx_sip_profile_domains_sip_profile_id_6a5cdae5 | ON sip_profile_id     |
+-----------------------+-------------------------------------------------+-----------------------+

.. _foreign-keys-62:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                       |
+=======================+===========================================================+==========================================================================================+
|                       | pbx_sip_profile_doma_sip_profile_id_6a5cdae5_fk_pbx_sip_p | ( sip_profile_id ) ref `public.pbx_sip_profiles <#table-public-pbx-sip-profiles>`__ (id) |
+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------------+

Table public.pbx_sip_profile_settings
=====================================

======= ============== ============
Idx     Name           Data Type
======= ============== ============
\* 🔑   id             uuid
\*      name           varchar(64)
\       value          varchar(254)
\*      enabled        varchar(8)
\       description    varchar(254)
\       created        timestamptz
\       updated        timestamptz
\       synchronised   timestamptz
\*      updated_by     varchar(64)
\* 🔎 ⬈ sip_profile_id uuid
======= ============== ============

.. _Indexes-80:

**Indexes**


+-----------------------+--------------------------------------------------+-----------------------+
| Type                  | Name                                             | On                    |
+=======================+==================================================+=======================+
| 🔑                    | pbx_sip_profile_settings_pkey                    | ON id                 |
+-----------------------+--------------------------------------------------+-----------------------+
| 🔎                    | pbx_sip_profile_settings_sip_profile_id_3d874090 | ON sip_profile_id     |
+-----------------------+--------------------------------------------------+-----------------------+

.. _foreign-keys-63:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                       |
+=======================+===========================================================+==========================================================================================+
|                       | pbx_sip_profile_sett_sip_profile_id_3d874090_fk_pbx_sip_p | ( sip_profile_id ) ref `public.pbx_sip_profiles <#table-public-pbx-sip-profiles>`__ (id) |
+-----------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------------+

Table public.pbx_sip_profiles
=============================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           uuid
\*      name         varchar(64)
\       hostname     varchar(128)
\*      enabled      varchar(8)
\       description  varchar(254)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
======= ============ ============

.. _Indexes-81:

**Indexes**


==== ===================== =====
Type Name                  On
==== ===================== =====
🔑   pbx_sip_profiles_pkey ON id
==== ===================== =====

Table public.pbx_user_settings
==============================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑   id           uuid
\* 🔎   category     varchar(32)
\* 🔎   subcategory  varchar(64)
\* 🔎   value_type   varchar(32)
\       value        varchar(254)
\*      sequence     numeric(11)
\*      enabled      varchar(8)
\       description  varchar(128)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
\* 🔎 ⬈ user_id_id   bigint
======= ============ ============

.. _Indexes-82:

**Indexes**


+-----------------------+---------------------------------------------+-----------------------+
| Type                  | Name                                        | On                    |
+=======================+=============================================+=======================+
| 🔑                    | pbx_user_settings_pkey                      | ON id                 |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_user_settings_user_id_id_f9155e23       | ON user_id_id         |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_user_settings_category_abdd8fa8         | ON category           |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_user_settings_category_abdd8fa8_like    | ON category           |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_user_settings_value_type_2a2d5624       | ON value_type         |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_user_settings_value_type_2a2d5624_like  | ON value_type         |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_user_settings_subcategory_681bdf20      | ON subcategory        |
+-----------------------+---------------------------------------------+-----------------------+
| 🔎                    | pbx_user_settings_subcategory_681bdf20_like | ON subcategory        |
+-----------------------+---------------------------------------------+-----------------------+

.. _foreign-keys-64:

**Foreign Keys**


+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------+
| Type                  | Name                                                  | On                                                                     |
+=======================+=======================================================+========================================================================+
|                       | pbx_user_settings_user_id_id_f9155e23_fk_pbx_users_id | ( user_id_id ) ref `public.pbx_users <#table-public-pbx-users>`__ (id) |
+-----------------------+-------------------------------------------------------+------------------------------------------------------------------------+

Table public.pbx_users
======================

======= ============ ============
Idx     Name         Data Type
======= ============ ============
\* 🔑 ⬋ id           bigserial
\* 🔍 ⬋ user_uuid    uuid
\* 🔍   username     varchar(150)
\       email        varchar(254)
\*      status       varchar(32)
\       api_key      varchar(254)
\*      enabled      varchar(8)
\       created      timestamptz
\       updated      timestamptz
\       synchronised timestamptz
\*      updated_by   varchar(64)
🔎 ⬈    domain_id_id uuid
\* 🔍 ⬈ user_id      integer
======= ============ ============

.. _Indexes-83:

**Indexes**


==== ================================ ===============
Type Name                             On
==== ================================ ===============
🔑   pbx_users_pkey                   ON id
🔍   pbx_users_user_uuid_key          ON user_uuid
🔍   pbx_users_username_key           ON username
🔍   pbx_users_user_id_key            ON user_id
🔎   pbx_users_username_bda12c52_like ON username
🔎   pbx_users_domain_id_id_cfe07cc2  ON domain_id_id
==== ================================ ===============

.. _foreign-keys-65:

**Foreign Keys**


+-----------------------+---------------------------------------------------+------------------------------------------------------------------------------+
| Type                  | Name                                              | On                                                                           |
+=======================+===================================================+==============================================================================+
|                       | pbx_users_domain_id_id_cfe07cc2_fk_pbx_domains_id | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id) |
+-----------------------+---------------------------------------------------+------------------------------------------------------------------------------+
|                       | pbx_users_user_id_4712cf8b_fk_auth_user_id        | ( user_id ) ref `public.auth_user <#table-public-auth-user>`__ (id)          |
+-----------------------+---------------------------------------------------+------------------------------------------------------------------------------+

Table public.pbx_vars
=====================

===== ============ ============
Idx   Name         Data Type
===== ============ ============
\* 🔑 id           uuid
\*    category     varchar(64)
\*    name         varchar(64)
\     value        varchar(254)
\     command      varchar(16)
\     hostname     varchar(128)
\*    enabled      varchar(8)
\*    sequence     numeric(11)
\     description  text
\     created      timestamptz
\     updated      timestamptz
\     synchronised timestamptz
\*    updated_by   varchar(64)
===== ============ ============

.. _Indexes-84:

**Indexes**


==== ============= =====
Type Name          On
==== ============= =====
🔑   pbx_vars_pkey ON id
==== ============= =====

Table public.pbx_voicemail_greetings
====================================

===== =============== ============
Idx   Name            Data Type
===== =============== ============
\* 🔑 id              uuid
\*    filename        text
\*    name            varchar(64)
\     description     varchar(128)
\     created         timestamptz
\     updated         timestamptz
\     synchronised    timestamptz
\*    updated_by      varchar(64)
🔎 ⬈  voicemail_id_id uuid
===== =============== ============

.. _Indexes-85:

**Indexes**


+-----------------------+--------------------------------------------------+-----------------------+
| Type                  | Name                                             | On                    |
+=======================+==================================================+=======================+
| 🔑                    | pbx_voicemail_greetings_pkey                     | ON id                 |
+-----------------------+--------------------------------------------------+-----------------------+
| 🔎                    | pbx_voicemail_greetings_voicemail_id_id_ee67c381 | ON voicemail_id_id    |
+-----------------------+--------------------------------------------------+-----------------------+

.. _foreign-keys-66:

**Foreign Keys**


+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Type                  | Name                                                       | On                                                                                    |
+=======================+============================================================+=======================================================================================+
|                       | pbx_voicemail_greeti_voicemail_id_id_ee67c381_fk_pbx_voice | ( voicemail_id_id ) ref `public.pbx_voicemails <#table-public-pbx-voicemails>`__ (id) |
+-----------------------+------------------------------------------------------------+---------------------------------------------------------------------------------------+

Table public.pbx_voicemails
===========================

======= ===================== ============
Idx     Name                  Data Type
======= ===================== ============
\* 🔑 ⬋ id                    uuid
\       password              varchar(16)
\       greeting_id           numeric(2)
\       alternate_greeting_id numeric(2)
\       mail_to               varchar(256)
\       sms_to                varchar(32)
\       cc                    varchar(64)
\*      attach_file           varchar(8)
\*      local_after_email     varchar(8)
\*      enabled               varchar(8)
\       description           varchar(256)
\       created               timestamptz
\       updated               timestamptz
\       synchronised          timestamptz
\*      updated_by            varchar(64)
🔎 ⬈    extension_id_id       uuid
======= ===================== ============

.. _Indexes-86:

**Indexes**


+-----------------------+-----------------------------------------+-----------------------+
| Type                  | Name                                    | On                    |
+=======================+=========================================+=======================+
| 🔑                    | pbx_voicemails_pkey                     | ON id                 |
+-----------------------+-----------------------------------------+-----------------------+
| 🔎                    | pbx_voicemails_extension_id_id_f5c8e5c1 | ON extension_id_id    |
+-----------------------+-----------------------------------------+-----------------------+

.. _foreign-keys-67:

**Foreign Keys**


+-----------------------+--------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Type                  | Name                                                         | On                                                                                    |
+=======================+==============================================================+=======================================================================================+
|                       | pbx_voicemails_extension_id_id_f5c8e5c1_fk_pbx_extensions_id | ( extension_id_id ) ref `public.pbx_extensions <#table-public-pbx-extensions>`__ (id) |
+-----------------------+--------------------------------------------------------------+---------------------------------------------------------------------------------------+

Table public.pbx_xml_cdr
========================

===== ========================= ============
Idx   Name                      Data Type
===== ========================= ============
\* 🔑 id                        uuid
\     domain_name               varchar(128)
\     accountcode               varchar(32)
\     direction                 varchar(16)
\     context                   varchar(128)
\     caller_id_name            varchar(32)
\     caller_id_number          varchar(32)
\     caller_destination        varchar(32)
\     source_number             varchar(32)
\     destination_number        varchar(32)
\     start_epoch               numeric(32)
\     start_stamp               timestamptz
\     answer_epoch              numeric(32)
\     answer_stamp              timestamptz
\     end_epoch                 numeric(32)
\     end_stamp                 timestamptz
\     duration                  numeric(32)
\     mduration                 numeric(32)
\     billsec                   numeric(32)
\     billmsec                  numeric(32)
\     bridge_uuid               uuid
\     read_codec                varchar(16)
\     read_rate                 varchar(16)
\     write_codec               varchar(16)
\     write_rate                varchar(16)
\     remote_media_ip           varchar(128)
\     network_addr              varchar(128)
\     record_path               varchar(256)
\     record_name               varchar(64)
\     leg                       varchar(8)
\     pdd_ms                    numeric(32)
\     rtp_audio_in_mos          numeric(4,2)
\     last_app                  varchar(32)
\     last_arg                  text
\     missed_call               boolean
\     cc_side                   varchar(16)
\     cc_member_uuid            uuid
\     cc_queue_joined_epoch     numeric(32)
\     cc_queue                  uuid
\     cc_member_session_uuid    uuid
\     cc_agent_uuid             uuid
\     cc_agent                  uuid
\     cc_agent_type             varchar(32)
\     cc_agent_bridged          varchar(8)
\     cc_queue_answered_epoch   numeric(32)
\     cc_queue_terminated_epoch numeric(32)
\     cc_queue_canceled_epoch   numeric(32)
\     cc_cancel_reason          varchar(32)
\     cc_cause                  varchar(32)
\     waitsec                   numeric(32)
\     conference_name           varchar(256)
\     conference_uuid           uuid
\     conference_member_id      varchar(8)
\     digits_dialed             varchar(64)
\     pin_number                varchar(16)
\     hangup_cause              varchar(32)
\     hangup_cause_q850         numeric(4)
\     sip_hangup_disposition    varchar(32)
\     xml                       text
\     json                      jsonb
\     created                   timestamptz
\     updated                   timestamptz
\     synchronised              timestamptz
\*    updated_by                varchar(64)
🔎 ⬈  domain_id_id              uuid
🔎 ⬈  extension_id_id           uuid
===== ========================= ============

.. _Indexes-87:

**Indexes**


+-----------------------+--------------------------------------+-----------------------+
| Type                  | Name                                 | On                    |
+=======================+======================================+=======================+
| 🔑                    | pbx_xml_cdr_pkey                     | ON id                 |
+-----------------------+--------------------------------------+-----------------------+
| 🔎                    | pbx_xml_cdr_domain_id_id_ccce6e81    | ON domain_id_id       |
+-----------------------+--------------------------------------+-----------------------+
| 🔎                    | pbx_xml_cdr_extension_id_id_f5f7d64e | ON extension_id_id    |
+-----------------------+--------------------------------------+-----------------------+

.. _foreign-keys-68:

**Foreign Keys**


+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------+
| Type                  | Name                                                      | On                                                                                    |
+=======================+===========================================================+=======================================================================================+
|                       | pbx_xml_cdr_domain_id_id_ccce6e81_fk_pbx_domains_id       | ( domain_id_id ) ref `public.pbx_domains <#table-public-pbx-domains>`__ (id)          |
+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------+
|                       | pbx_xml_cdr_extension_id_id_f5f7d64e_fk_pbx_extensions_id | ( extension_id_id ) ref `public.pbx_extensions <#table-public-pbx-extensions>`__ (id) |
+-----------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------+
