"""
pip3 install kerberos
pip3 install impala
pip3 install impyla
"""

from impala.dbapi import connect

# for parameters, see https://github.com/cloudera/impyla/blob/master/impala/dbapi.py
conn = connect(host='c191-node2.labs.support.hortonworks.com',
  port=10000,
  database='default',
  auth_mechanism='GSSAPI',
  #use_ssl='true',
  #ca_cert='/opt/impyla/mr3-ssl.pem',
  kerberos_service_name='hive')

cursor = conn.cursor()
cursor.execute("SHOW TABLES")
print(cursor.description)  # prints the result set's schema
results = cursor.fetchall()
cursor.close()
conn.close()