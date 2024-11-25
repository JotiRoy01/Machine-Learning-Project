import os
import datetime
#ROOT_DIR = os.getcwd() # To get current working directory
#ROOT_DIR = os.getcwd(".")
#ROOT_DIR = os.chdir("d:\\Develops\\ML_PROJECT\\Machine-Learning-Project")
ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, CONFIG_FILE_NAME)
CURRENT_TIME_STAMP = f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"