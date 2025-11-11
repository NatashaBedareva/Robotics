import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/natalia/Documents/STUDING/robotix/modul4/ex02b/mycarrot/install/mycarrot'
