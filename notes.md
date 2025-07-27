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

    Put simply, the `setup.py` file contains the instructions to build, package and distribute a Python project. 

- The file `__init__.py` tells Python that the folder (for example, `src`) it resides in should be treated as a package. We mean that the `src` folder is now a Python package, meaning:
    - We can import from it
    - Python will recognize its submodules and subpackages

 - `-e .` triggers `setup.py` or `pyproject.toml` to install our package in editable mode, making it easier to develop and test changes without reinstalling the package.
 - The `Sample_Project.egg-info` folder is **metadata** about our Python package. It is created when we install our project using:
    ```
    pip install -e .
    ```
    
    `Sample_Project.egg-info` is an internal **metadata folder** created by `setuptools` when installing the local package. It helps tools understand and manage the package.

    **Why is it called "egg-info"?**
    - It comes from the old Python packaging format called "Eggs", which has now largely been replaced by Wheels (`.whl`).

    - Even though Eggs aren't commonly used anymore, the `.egg-info` structure is still used by `setuptools` to store metadata.

- What `-e .` does?
    
    - `-e` stands for editable install.
    - The `.` refers to the current directory (your project folder).
    - So `-e .` tells pip to install the current project in editable mode using `pyproject.toml` or `setup.py`. 

### **ML Project Lifecycle**
- **Data ingestion** means reading the data from databases. For reading the data, we need a data path and a database configuration. **Data ingestion configuration** will have the information about the data path and the database configuration.

    After having read the data, we split the data into:
    - Train set
    - Test set
    - Validation set 
    
    The output of data ingestion configuration will be a **data ingestion artifact**. 

- **Data validation**: To validate the data, we require schema of the data along with train set, test set and validation set. All four pieces of information become part of the **data validation configuration**. 

    The output of data validation pipeline is train and test sets. This forms the **data validation artifact**.

- The output of data validation pipeline becomes the input of **data transformation** pipeline, which gets further connected to the **model trainer pipleline**. 