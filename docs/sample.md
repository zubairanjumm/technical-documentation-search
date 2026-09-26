# Python Virtual Environments

Python virtual environments allow you to create isolated environments
for different projects.

## Creating a Virtual Environment

You can create a virtual environment using:

python -m venv .venv

## Activating on Windows

On Windows PowerShell, activate the environment with:

.venv\Scripts\Activate.ps1

## Installing Packages

After activating the environment, packages can be installed using pip:

pip install package-name

## Deactivating

To leave the virtual environment, run:

deactivate