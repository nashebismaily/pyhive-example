"""
yum install cyrus-sasl-devel
pip install sasl
pip install thrift
pip install thrift-sasl
pip install PyHive
"""

#!/usr/bin/env python

import time
from pyhive import hive

conn = hive.connect(host='c191-node2.labs.support.hortonworks.com', # Change to your HiveServe2 Hostname
                            port=10000,
                            database='default', # Change to the Hive DB you want to connect to
                            username='nasheb',  # Change to your user
                            auth='KERBEROS',
                            kerberos_service_name='hive')

def test():
    start_time = time.time()
    cursor = conn.cursor()
    cursor.execute("show tables")
    for result in cursor.fetchall():
      print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
    cursor.close()

test()

conn.close()