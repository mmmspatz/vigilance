import datetime

dbname = '/home/ryanqputz/vigilance/python/vigilance.db'

content_path = "static/ims/"
updateInterval = 3

image_lifetime = datetime.timedelta(days=1)
device_lifetime = datetime.timedelta(hours=1)

#image_urls = {"android":"/shot.jpg", "webcam":"/?action=snapshot"}
image_urls = {"android":"/shot.jpg", "webcam":"/cgi-bin/viewer/video.jpg?streamid=0", "kitchencam":"/jpg/1/image.jpg"}
video_urls = {"android":"/videofeed", "webcam":"/video2.mjpg", "kitchencam":"/mjpg/video.mjpg"}
view_templates = {"android":'android_view.html', "webcam":'webcam_view.html',"kitchencam":"http://eyeinthesky.mit.edu"}

lighton="/enabletorch"
lightoff="/disabletorch"

full_domains = ["http://vigilance.mit.edu/", "http://vigilance/"]
kitchen_domains = ["http://www.collegecoedsgonewildinthekitchen.com/"]
basha_domains = ["http://mitwebcam.com/", "http://webcam.mit.edu/", "http://webcam/"]

ports={"android":8080, "webcam":8090, "kitchencam":80}

headers={"android":"http://", "webcam":"", "kitchencam":""}
