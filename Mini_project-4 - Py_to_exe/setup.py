from cx_Freeze import setup, Executable

setup(name = 'Calculator',
      version =  '0.1',
      description = 'Basic Calculator Functions',
      executables = [Executable("Py_calc.py")])