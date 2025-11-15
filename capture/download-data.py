# ddl_slu_east = "https://g1.ipcamlive.com/player/player.php?alias=57d79729b11b0&autoplay=1"
# ddl_slu_west = "https://g1.ipcamlive.com/player/player.php?alias=57d796dc274ef&autoplay=1"
# ddl_slu_bed_1 = "https://g1.ipcamlive.com/player/player.php?alias=57d798335d414&autoplay=1"
# ddl_slu_bed_2 = "https://g1.ipcamlive.com/player/player.php?alias=57d72abdbcbdb&autoplay=1"
# ddl_slu_central = "https://g1.ipcamlive.com/player/player.php?alias=5aec9329bc357&autoplay=1"
#
# ddl_ballard_heart="https://g1.ipcamlive.com/player/player.php?alias=5c3263db7e03e&autoplay=1"
# ddl_ballard_big_outdoor="https://g1.ipcamlive.com/player/player.php?alias=5c32596b65526&autoplay=1"
# ddl_ballard_small_outdoor="https://g1.ipcamlive.com/player/player.php?alias=5c32636731455&autoplay=1"
# ddl_ballard_indoor_1="https://g1.ipcamlive.com/player/player.php?alias=5c32618141523&autoplay=1"
# ddl_ballard_indoor_2="https://g1.ipcamlive.com/player/player.php?alias=5c3265e523e02&autoplay=1"

cam_ids = {
  "ddl_slu_east": "57d79729b11b0",
  "ddl_slu_west": "57d796dc274ef",
  "ddl_slu_bed_1": "57d798335d414",
  "ddl_slu_bed_2": "57d72abdbcbdb",
  "ddl_slu_central": "5aec9329bc357",
  "ddl_ballard_heart": "5c3263db7e03e",
  "ddl_ballard_big_outdoor": "5c32596b65526",
  "ddl_ballard_small_outdoor": "5c32636731455",
  "ddl_ballard_indoor_1": "5c32618141523",
  "ddl_ballard_indoor_2": "5c3265e523e02"
}

def feed_link(cam_id):
  return f"https://g1.ipcamlive.com/player/player.php?alias={cam_id}&autoplay=1"

def photo_link(cam_id):
  return f"https://ipcamlive.com/player/snapshot.php?alias={cam_id}"

def file_name(cam_name):
  return f"{cam_name}.jpg"