Changelog
=========

37.0 (Unpublished)
------------------

* Support for Python 3.4 and 3.5.
  [hynekcer]

* Update to use version 37.0 of the Salesforce.com partner WSDL by default.
  [hynekcer]

* Automatic tests for all Python versions by 'tox'.
  [hynekcer]

* Support for easy sandbox login.
  [hynekcer]

* Fixed deprecation warning due to deprecated failUnless test method.
  [hynekcer]

32.1 (2014-12-04)
-----------------

* Fix bug in convertLead when passed a single object instead of a list.
  [davisagli]

32.0 (2014-12-01)
-----------------

* Add support for the convertLead call.
  [davisagli]

* Update to use version 32.0 of the Salesforce.com partner WSDL by default.
  [davisagli]

* Don't use _out internal method from XMLGenerator.
  [smcmahon]

20.0 (2010-11-30)
-----------------

* Add 'encryptedstring' to the list of types marshalled as strings.  Thanks
  sobyone.
  [davisagli]

* Update to use version 20.0 of the Salesforce.com partner WSDL by default.
  [davisagli]

19.0 (2010-08-23)
-----------------

* Update marshalling of describeGlobal and describeSObjects responses to
  include new properties now returned by the API.  For backwards
  compatibility, we set the types property of the describeGlobal response
  to a list of the names of all types (which Salesforce now returns in
  separate DescribeGlobalSObjectResult objects).
  [davisagli]

* Update to use version 19.0 of the Salesforce.com partner WSDL by default.
  Also, use the new login.salesforce.com login endpoint by default.
  [davisagli]

16.1 (2010-03-11)
-----------------

* Catch and retry on exceptions from the socket library, in addition to ones
  from httplib.  This fixes a regression introduced in version 16.0.
  [davisagli]


16.0 (2009-11-12)
-----------------

* Don't strip newlines when marshalling the values of textarea fields.
  [davisagli]

* Make sure to add a field to fieldsToNull if its Python value is None.
  [rhettg, davisagli]

* Fix issue where numbers of type long weren't converted to a string.
  [spleeman, davisagli]

* Only catch HTTP exceptions when retrying a connection.
  [spleeman, davisagli]


16.0b1 (2009-09-08)
-------------------

* Log beatbox calls at the debug level.
  [davisagli]

* Fixed a string exception for compatibility with Python 2.6.
  [davisagli]

* Added support for SOSL searches via the search method.  Thanks to Alex Tokar
  of Web Collective.
  [davisagli]

* Added an optional cache for the sObject type descriptions needed for
  marshalling query results into Python objects. This can avoid an extra
  describeSObjects API call for each query, but means that the information
  could become stale if the type metadata is modified in Salesforce.com.
  The cache is off by default. Turn it on by passing
  cacheTypeDescriptions=True when instantiating a Python client. The cache may
  be reset by calling the flushTypeDescriptionsCache method of the Python
  client.
  [davisagli]

* Support a full SOQL statement as a parameter to the query method of the
  Python client.  The old 3-part method signature (fields, sObjectType,
  conditionalExpression) should continue to work.
  [davisagli]

* In the Python client, support relationship queries and other queries that may
  return multiple types of objects.  Object type descriptions (required for
  marshalling field values into the correct Python type) are cached for the
  duration of the query after the first time they are used.  Thanks to
  Melnychuk Taras of Quintagroup.
  [davisagli]

* In the Python client, queries now return a list-like QueryRecordSet holding
  a sequence of dict-like QueryRecord objects, instead of a dict containing a
  list of dicts.  This allows for more Pythonic access such as results[0].Id
  instead of results['results'][0]['Id'].  The old syntax should still work.
  Thanks to Melnychuk Taras of Quintagroup.
  [davisagli]

* Update to use version 16.0 of the Salesforce.com partner WSDL.
  [davisagli]


0.12 (2009-05-13)
-----------------

* Use the default serverUrl value if the passed value evaluates to boolean
  False.
  [davisagli]

0.11 (2009-05-13)
-----------------

* Access 'created' instead of 'isCreated' in the upsert result. This closes
  http://code.google.com/p/salesforce-beatbox/issues/detail?id=4
  [davisagli]

0.10 (2009-05-06)
-----------------

* Added optional serverUrl parameter when creating a Client.
  [davisagli]

pre 0.9.1.1
-----------

* ancient history
