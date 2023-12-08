from cx_Freeze import setup, Executable

script_name = "pars.py"

exe_name = "Pars_Per"

executables = [Executable(script=script_name, base="Console")]

setup(
    name="YourApp",
    version="1.0",
    description="Your description",
    executables=executables
)
