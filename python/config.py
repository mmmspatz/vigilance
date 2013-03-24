import datetime

dbname = 'vigilance.db'

content_path = "ims/"
updateInterval = 3

image_lifetime = datetime.timedelta(days=3)
device_lifetime = datetime.timedelta(hours=1)

image_url="/shot.jpg"
video_url="/videofeed"

lighton="/enabletorch"
lightoff="/disabletorch"

port=8080
