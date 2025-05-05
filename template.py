import os
from pathlib import Path
import logging

'''
This script creates a project structure for a machine learning project. It creates directories and files as specified in the list_of_files variable. 
If a directory already exists, it skips creating it. If a file already exists and is not empty, it skips creating it. Otherwise, it creates an empty file. 
'''

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

Project_name = "cellSegmentation"

list_of_files = [".github/workflows/.gitkeep",
                    "data/.gitkeep",
                    f"{Project_name}/__init__.py",
                    f"{Project_name}/components/__init__.py",
                    f"{Project_name}/components/data_ingestion.py",
                    f"{Project_name}/components/data_validation.py",
                    f"{Project_name}/components/model_trainer.py",
                    f"{Project_name}/constant/__init__.py",
                    f"{Project_name}/constant/training_pipeline/__init__.py",
                    f"{Project_name}/constant/application.py",
                    f"{Project_name}/entity/config_entity.py",
                    f"{Project_name}/entity/artifacts_entity.py",
                    f"{Project_name}/exception/__init__.py",
                    f"{Project_name}/logger/__init__.py",
                    f"{Project_name}/pipeline/__init__.py",
                    f"{Project_name}/pipeline/training_pipeline.py",
                    f"{Project_name}/utils/__init__.py",
                    f"{Project_name}/utils/main_utils.py",
                    "research/trials.ipynb",
                    "templates/index.html",
                    "app.py",
                    "Dockerfile",
                    "requirements.txt",
                    "setup.py",
                    ]

for filepath in list_of_files:
    file_path = Path(filepath)

    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created")

