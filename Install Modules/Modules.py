import importlib
import subprocess
def install_module(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"{module_name} is not installed. Installing...")
        try:
            subprocess.call(['pip', 'install', module_name])
            print(f"{module_name} has been successfully installed.")
        except Exception as e:
            print(f"Error installing {module_name}: {e}")
required_modules = [
    'sympy', '--upgrade setuptools', 'tk', 'numpy', 'googletrans==4.0.0-rc1', 'pymysql', 'pycryptodome',
    'mysql-connector-python', '--update futures', 'matplotlib', 'pygame', '--upgrade --force-reinstall --no-cache-dir PyDictionary',
    'gTTS', 'pyjokes', 'subprocess', 'speech_recognition', 'pyttsx3', 'wikipedia', 'webbrowser', 'smtplib']

for module in required_modules:
    install_module(module)
