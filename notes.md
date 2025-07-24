## Notes

- **Creating virtual environmet**

    ```
    conda create -p venv python==3.12
    ```
    -p venv means: Create the environment in a folder named `venv` in the current directory.

    ```
    conda create -n myenv python=3.12
    ```
    `-n` creates the virtual environment in Conda's default environment directory. 

    ```
    pip install -r requirements.txt
    ```

- The `setup.py` file is responsible for defining the configuration and metadata needed to package and distribute a Python project.

    Put simply, the `setup.py` file contains the instructions to build, package, and distribute a Python project. 

