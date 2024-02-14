#######################################################
# Author: Arnold Vianna  
# https://github.com/arnold-vianna
# https://arnold-vianna.github.io/
#######################################################


import psutil

def find_and_kill_python_script(script_name):
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(process.info['cmdline'])
            if 'python' in process.info['name'] and script_name in cmdline:
                print(f"Found process {process.info['pid']} - {cmdline}")
                process.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    script_name = "copycat.py"  # Update this with your script name
    find_and_kill_python_script(script_name)
