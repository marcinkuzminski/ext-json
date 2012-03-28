EXTENDED JSON
=============


Simple extended version of JSON encoder for handling serialization of few
other than standard python data types. It works on python json module, and 
fallbacks to simplejson if available


Supports the following objects and types by default:

+-----------------------------+-----------------------------+
| Python                      | JSON                        |
+=============================+=============================+
| dict, namedtuple            | object                      |
+-----------------------------+-----------------------------+
| list, tuple, set            | array                  |
+-----------------------------+-----------------------------+
| str, unicode                | string                      |
+-----------------------------+-----------------------------+
| int, long, float            | number                      |
+-----------------------------+-----------------------------+
| True                        | true                        |
+-----------------------------+-----------------------------+
| False                       | false                       |
+-----------------------------+-----------------------------+
| None                        | null                        |
+-----------------------------+-----------------------------+
| Decimal                     | str                         |
+-----------------------------+-----------------------------+
| complex                     | array[real,img]             |
+-----------------------------+-----------------------------+
| datetime.date               | date.isoformat  ECMA-262    |
+-----------------------------+-----------------------------+
| datetime.datetime           | datetime.isoformat ECMA-262 |
+-----------------------------+-----------------------------+
| decimal.Decimal             | string of decimal           |
+-----------------------------+-----------------------------+
| datetime.time               | datetime.tim.isoformat      |
+-----------------------------+-----------------------------+


usage::

 from ext_json import json
 
imported json have already extended encoder as default so no special calls
are needed to execute `json.dump` or `json.dumps`