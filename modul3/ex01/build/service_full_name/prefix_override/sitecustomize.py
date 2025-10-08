import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/natalia/Documents/STUDING/robotix/modul3/ex01/install/service_full_name'
