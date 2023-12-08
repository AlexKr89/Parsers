from cx_Freeze import setup, Executable

script_name = "pars.py"

# Замените "YourExecutableName" на желаемое имя .exe файла
exe_name = "Pars_Per"

executables = [Executable(script=script_name, targetName=exe_name)]

setup(
    name="YourApp",
    version="1.0",
    description="Your description",
    executables=executables
)
