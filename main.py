import os
import sys
import subprocess

if __name__ == '__main__':
    # Launch Streamlit app in frontend/app.py
    cmd = f'streamlit run "{os.path.join(os.path.dirname(__file__), "frontend", "app.py")}"'
    print("Launching Streamlit GUI...")
    # Use os.exec to replace process, or subprocess to keep control
    subprocess.run(cmd, shell=True, check=True)
