EXTENDED JSON
=============


Simple extended version of JSON encoder for handling serialization of few
other than standard python data types. It tries to use simplejson lib if found
then fallback to stdlib json module. Raises an exception if no json module
can be loaded.


Supports the following objects and types by default:

+-----------------------------+-----------------------------+
| Python                      | JSON                        |
+=============================+=============================+
| dict, namedtuple            | object                      |
+-----------------------------+-----------------------------+
| list, tuple, set            | array                       |
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


In addition if object have **__json__** attribute or method encoder will use 
that for serialization 


usage::

 from ext_json import json
 
imported json have already extended encoder as default so no special calls
are needed to execute `json.dump` or `json.dumps`

if you prefer to import specific encoder you can do::
 
 from ext_json import simplejson # for simplejson <-- can be None
 from ext_json import stdjson # for json from stdlib
 