import datetime

dbname = '/home/ryanqputz/vigilance/python/vigilance.db'

content_path = "ims/"
updateInterval = 3

image_lifetime = datetime.timedelta(days=3)
device_lifetime = datetime.timedelta(hours=1)

image_urls = {"android":"/shot.jpg", "webcam":"/?action=snapshot"}
video_urls = {"android":"/videofeed", "webcam":"/?action=stream"}

lighton="/enabletorch"
lightoff="/disabletorch"

port=8080
