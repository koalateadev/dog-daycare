from datetime import datetime
from pathlib import Path
import requests

cam_ids = {
  "ddl_slu_east": "57d79729b11b0",
  "ddl_slu_west": "57d796dc274ef",
  # "ddl_slu_bed_1": "57d798335d414",
  # "ddl_slu_bed_2": "57d72abdbcbdb",
  # "ddl_slu_central": "5aec9329bc357",
  # "ddl_ballard_heart": "5c3263db7e03e",
  # "ddl_ballard_big_outdoor": "5c32596b65526",
  # "ddl_ballard_small_outdoor": "5c32636731455",
  # "ddl_ballard_indoor_1": "5c32618141523",
  # "ddl_ballard_indoor_2": "5c3265e523e02"
}

def feed_link(cam_id):
  return f"https://g1.ipcamlive.com/player/player.php?alias={cam_id}&autoplay=1"

def photo_link(cam_id):
  return f"https://ipcamlive.com/player/snapshot.php?alias={cam_id}"

def get_timestamp():
  now = datetime.now()
  return now.strftime("%Y%m%d_%H%M%S")

def get_filename(cam_name, timestamp):
  script_dir = Path(__file__).resolve().parent
  return f"{script_dir}/../data/{cam_name}/{timestamp}.jpg"

timestamp = get_timestamp()

for name, id in cam_ids.items():
  print(name)

  url = photo_link(id)
  path = get_filename(name, timestamp)
  file_path = Path(path)
  file_path.parent.mkdir(parents=True, exist_ok=True)

  response = requests.get(url, stream=True)
  response.raise_for_status()

  with open(file_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
      f.write(chunk)