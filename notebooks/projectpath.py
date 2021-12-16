import sys 
import os 

module_path = os.path.abspath(os.path.join(os.pardir, os.pardir))+r'/MATH-446-MEV/src'
if module_path not in sys.path: 
    sys.path.append(module_path)