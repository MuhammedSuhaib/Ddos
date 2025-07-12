https://youtu.be/-nsALpaFZ8U?si=Yw-WIv0zx6wy1BnJ    

https://youtu.be/ilhGh9CEIwM?si=wf1f1pzqZFWSIMaR    


`uv init`   

Activate it with `source .venv/bin/activate`On Linux/Mac Or Activate it with `.venv/Scripts/activate` on Windows    

`uv add pyinstaller`

`uvx pyinstaller -v` should return installed `pyinstaller` version      

`uvx pyinstaller --onefile --nowindow --clean --name <app_name> <your_script.py>` should get the job done with a single bundled executable

`--nowindow`: Hides console window (used for GUI or silent apps)

`--clean`: Clears old build cache

`--name <app_name>`: Sets custom name for the .exe file

All are optional, for cleaner/specific builds.

