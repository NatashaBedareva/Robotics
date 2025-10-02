import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/natalia/Documents/STUDING/robotix/modul2/ex10/install/text_to_cmd_vel'
