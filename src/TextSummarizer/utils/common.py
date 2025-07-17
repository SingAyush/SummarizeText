import os
import yaml
from TextSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any, List, Union

def read_yaml(path_to_yaml: Union[str, Path]) -> ConfigBox:
    """
    Read yaml file and return ConfigBox object
    
    Args:
        path_to_yaml (Union[str, Path]): Path to the yaml file
        
    Returns:
        ConfigBox: ConfigBox object containing yaml content
    """
    try:
        path_to_yaml = Path(path_to_yaml)  # Convert to Path object if string
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"YAML file not found: {path_to_yaml}")
        raise FileNotFoundError(f"YAML file not found: {path_to_yaml}")
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        raise yaml.YAMLError(f"Error parsing YAML file: {e}")
    except Exception as e:
        logger.error(f"Unexpected error reading yaml file: {e}")
        raise e

def create_directories(path_to_directories: List[str]) -> None:
    """
    Create list of directories
    
    Args:
        path_to_directories (List[str]): List of directory paths to create
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            logger.info(f"Created directory at: {path}")
    except OSError as e:
        logger.error(f"Error creating directories: {e}")
        raise OSError(f"Error creating directories: {e}")
    except Exception as e:
        logger.error(f"Unexpected error creating directories: {e}")
        raise e

def get_size(path: Union[str, Path]) -> str:
    """
    Get size of file in KB
    
    Args:
        path (Union[str, Path]): Path to the file
        
    Returns:
        str: Size of file in KB
    """
    try:
        path = Path(path)  # Convert to Path object if string
        if not path.exists():
            logger.error(f"File not found: {path}")
            raise FileNotFoundError(f"File not found: {path}")
        
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~ {size_in_kb} KB"
    except OSError as e:
        logger.error(f"Error getting file size: {e}")
        raise OSError(f"Error getting file size: {e}")
    except Exception as e:
        logger.error(f"Unexpected error getting file size: {e}")
        raise e