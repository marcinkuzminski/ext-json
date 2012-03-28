EXTENDED JSON
=============


Simple extended version of JSON encoder for handling serialization of few
other than standard python data types. It works on python json module, and 
fallbacks to simplejson if available


Supports the following objects and types by default:

+-------------------+-----------------+
| Python            | JSON            |
+===================+=================+
| dict, namedtuple  | object          |
+-------------------+-----------------+
| list, tuple       | array           |
+-------------------+-----------------+
| str, unicode      | string          |
+-------------------+-----------------+
| int, long, float  | number          |
+-------------------+-----------------+
| True              | true            |
+-------------------+-----------------+
| False             | false           |
+-------------------+-----------------+
| None              | null            |
+-------------------+-----------------+
| Decimal           | str             |
+-------------------+-----------------+ 
| complex           | array[real,img] |
+-------------------+-----------------+
| datetime.date     | date.isoformat  |
+-------------------+-----------------+


usage::

 from ext_json import json