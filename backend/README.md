# Backend Setup
You have to write the commands with backend as root folder!!!
## Requirements
- Python 3.12 or newer

## Setup
1. Prepare virtual environment writing on terminal:<br>
`python -m venv .venv`
2. Enter into virtual environment writing on terminal:<br>
`.\.venv\Scripts\activate` (if you are not on windows system, try to use / instead of \\)
3. Install the modules writing on terminal: <br>
`pip install -r requirements.txt`
4. Run server writing on terminal:<br>
`c`

## Extra
- If you are getting an execution policy error on Windows when trying to enter into virtual environment, then open Powershell with the "Run as Administrator" option. Paste on Powershell: `set-executionpolicy remotesigned` <br>
- In order to VSCode recognize the virtual environment modules, write on the VSCode topbar "> Python: Select Interpreter" and enter the virtual environment path.
- To open the swagger (API docs and routes testing) enter to localhost:3000/docs