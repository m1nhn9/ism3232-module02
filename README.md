# Module 2: Shell Navigation and File Operations

This module contains the Week 2 navigation exercise and the command reference
used through Weeks 2–4.

## Week 2 Commands

| Command | Description |
| --- | --- |
| `pwd` | Print the current working directory. |
| `ls` | List visible files and folders. |
| `ls -la` | List files, including hidden files and details. |
| `cd ..` | Move to the parent directory. |
| `cd ~/ism3232` | Move to the course directory. |
| `tree -L 2` | Display the directory tree to two levels. |
| `touch FILE` | Create an empty file or update its timestamp. |
| `cat FILE` | Print a file's contents. |
| `cp SOURCE DEST` | Copy a file. |
| `mv SOURCE DEST` | Move or rename a file. |
| `python3 FILE` | Run a Python script. |
| `rm FILE` | Delete a file after checking its location and contents. |

## Week 3 Environment Commands

| Command or alias | Description |
| --- | --- |
| `python3 -m venv .venv` | Create a project virtual environment. |
| `source .venv/bin/activate` | Activate the environment. |
| `which python3` | Show the active Python interpreter. |
| `pip install pytest ruff` | Install the lab tools. |
| `pip freeze > requirements.txt` | Record installed package versions. |
| `deactivate` | Leave the active environment. |
| `ll` | Run `ls -la`. |
| `c` | Clear the terminal. |
| `py` | Run `python3`. |
| `gs` | Run `git status`. |
| `ga` | Run `git add .`. |
| `gcmsg MESSAGE` | Run `git commit -m MESSAGE`. |
| `gp` | Run `git push`. |
| `gl` | Run `git log --oneline`. |
| `tree2` | Run `tree -L 2`. |
| `mkcd NAME` | Create a directory and enter it. |

Run `python3 week2_lab/week2_script.py` from this repository root.
The Week 4 verification tests are in `tests/`.

## Run the Week 4 Checks

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ruff format . && ruff check . && pytest -v
```

## Import History

This is the standalone `module02_zsh` repository for Weeks 2–4.
It is private because Week 4 specifies a private GitHub repository.
Relevant commits were extracted from the combined coursework repository;
their messages and authors are preserved, but commit IDs changed.
AI assisted with the separation and earlier documented edits.
