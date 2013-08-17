import datetime

dbname = '/home/ryanqputz/vigilance/python/vigilance.db'

content_path = "static/ims/"
updateInterval = 3

image_lifetime = datetime.timedelta(days=3)
device_lifetime = datetime.timedelta(hours=1)

image_urls = {"android":"/shot.jpg", "webcam":"/?action=snapshot"}
video_urls = {"android":"/videofeed", "webcam":"/?action=stream"}
view_templates = {"android":'android_view.html', "webcam":'webcam_view.html'}

lighton="/enabletorch"
lightoff="/disabletorch"

full_domains = ["http://vigilance.mit.edu/", "http://vigilance/"]
kitchen_domains = ["http://www.collegecoedsgonewildinthekitchen.com/"]
basha_domains = ["http://mitwebcam.com/", "http://webcam.mit.edu/", "http://webcam/"]

port=8080
