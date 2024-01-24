**A task list website for FRC 1294, Pack of Parts**

Using GitHub Rest API and Flask to give display an updated list of pending issues during meetings. 

To run create a `.env` file in your root directory. Copy the contents of `.env.example`
Then create an access token from [here](https://github.com/settings/tokens) (be sure to include all repository permissions in the perms scope).

Paste that access token in your `.env` file.

Activate the virtual environment. If on windows run `venv\Scripts\activate` in the cmd when in the root directory.
Then run `pip install -r requirements.txt` in that virtual environment.

Then in the virtual environment run `python main.py` to run the application.
