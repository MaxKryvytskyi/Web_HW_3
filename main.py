
import concurrent.futures
import logging
import shutil
import os
import re
import random
import sys

from time import time
from rich.console import Console
from rich.table import Table
from args import category_dict, normalize, get_cpu_count

directory = 'E:\Git_Files\__Python_GOIT__\__Web_2_0__\sort\main'
processes = get_cpu_count()
console = Console()

def create_folder(category_dict):
    for name in category_dict:
        try:
            os.makedirs(os.path.join(directory, name))
            logging.info(f"INFO: Create folder {name}")
        except FileExistsError:
            logging.info(f"WARNING: Error FileExistsError {name}")

def remove_empty_directories(directory):
    for dirpath, dirnames, _ in os.walk(directory, topdown=False):
        for dirname in dirnames:
            folder_path = os.path.join(dirpath, dirname)
            if not os.listdir(folder_path):  
                os.rmdir(folder_path)
                parts = re.split(re.compile(r'[\\/]'), folder_path)
                logging.info(f"INFO: Remove folder {normalize(parts[-1])}")

def get_category(files: str):
    for cat, extension in category_dict.items():
        if files.split('.')[-1] in extension:
            logging.info(f"INFO: Category {cat}")
            return cat
    logging.info(f"INFO: Category Others")
    return "Others"

def move_file(file, root, cat):
    new_name = normalize(file)
    source_path = os.path.join(root, file)
    destination_path = os.path.join(root, new_name)
    new_path = os.path.join(directory, cat, new_name)

    os.replace(source_path, destination_path)
    try:
        shutil.move(destination_path, new_path)
        logging.info(f"INFO: file {new_name} move {cat}")
    except FileExistsError:
        logging.info(f"WARNING: Error FileExistsError, move {destination_path} > {new_path}")


def main(directory):
    fil = []
    roots = []
    categ = []

    list_table = []
    max_len = 0
    style = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        
    for root, _, files in os.walk(directory):
        for file in files:
            if max_len < len(file):
                max_len = len(file)
            cat = get_category(file)
            fil.append(file)
            roots.append(root)
            categ.append(cat)
            
    create_folder(category_dict)
    with concurrent.futures.ThreadPoolExecutor(max_workers=processes) as executor:
        executor.map(move_file, fil, roots, categ)
    remove_empty_directories(directory)

    for root, _, files in os.walk(directory):
        if not files:
            continue
        parts = re.split(re.compile(r'[\\/]'), root)
        table = Table(title="")
        text = f"{parts[-1]}" + " " * (max_len + 3 -len(parts[-1]))
        table.add_column(text, justify="full", style=random.choice(style), no_wrap=False)
        for file in files:
            table.add_row(file)
        list_table.append(table)
    return list_table
    

if __name__ == "__main__":
    start_time = time()
    logging.basicConfig(level=logging.INFO, handlers=[
    logging.FileHandler("sort_log.txt"),
    logging.StreamHandler()], format="%(asctime)s %(message)s")
    table = main(directory)
    for t in table:
        console.print(t)
    end_time = time()
    logging.info(f"INFO: Workings processes: {processes}")
    logging.info(f"INFO: Workings times: {end_time - start_time} seconds")
