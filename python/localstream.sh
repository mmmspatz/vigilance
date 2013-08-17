PORT=8080
vlcstream='cvlc -v v4l2:///dev/video0:width=320:height=240 --v4l2-chroma=UYVY --v4l2-fps=5 --sout "#transcode{vcodec=theo,vb=256,scale=1,acodec=none,fps=25}:standard{access=http,mux=ogg,dst=:8080/videofeed}"'

export LD_LIBRARY_PATH=/usr/local/lib

mjpg_streamer -i "input_uvc.so -y -d /dev/video0" -o "output_http.so -w /home/ryanqputz/mjpg-streamer/mjpg-streamer/www"


