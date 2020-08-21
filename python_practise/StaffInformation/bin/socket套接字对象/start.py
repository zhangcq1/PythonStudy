import os
import sys
project_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_path)
from core import main
if __name__ == '__main__':
    main.fun()