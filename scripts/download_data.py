import os
import requests
from tqdm import tqdm
from hic2cool.hic2cool_utils import hic2cool_convert

# URLs for Hi-C maps
URLS = [
    "https://genedev.bionet.nsc.ru/ftp/by_User/DashaPanchenko/hepatocytes/merged_hic_maps/Control_inter_30.hic",
    "https://genedev.bionet.nsc.ru/ftp/by_User/DashaPanchenko/hepatocytes/merged_hic_maps/Treated_inter_30.hic",
    "https://genedev.bionet.nsc.ru/ftp/by_User/DashaPanchenko/hepatocytes/merged_hic_maps/Prime_inter_30.hic"
]

DATA_DIR = "data"

def download_file(url, dest_folder):
    """Downloads a file from a URL to a output folder"""
    os.makedirs(dest_folder, exist_ok=True)
    filename = url.split("/")[-1]
    filepath = os.path.join(dest_folder, filename)

    if os.path.exists(filepath):
        print(f"{filename} already exists. Skipping download.")
        return filepath

    print(f"Downloading {filename}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    with open(filepath, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            bar.update(len(data))
            file.write(data)
            
    return filepath

if __name__ == "__main__":
    print("Starting data download...")
    for url in URLS:
        hic_path = download_file(url, DATA_DIR)
        
        cool_path = hic_path.replace(".hic", ".mcool")
        if not os.path.exists(cool_path):
            print(f"Converting {hic_path} to {cool_path}...")
            # You could change resolution to 2500000, 1000000, 500000, 250000, 100000, 50000, 25000, 10000, 5000
            hic2cool_convert(hic_path, cool_path, resolution=10000)
            
    print("All files downloaded and converted successfully!")
