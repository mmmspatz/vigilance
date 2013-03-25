PORT=8080
vlcstream='cvlc -v v4l2:///dev/video0:width=320:height=240 --v4l2-chroma=UYVY --v4l2-fps=5 --sout "#transcode{vcodec=theo,vb=256,scale=1,acodec=none,fps=25}:standard{access=http,mux=ogg,dst=:$PORT/videofeed}"'

$vlcstream&

curl -d "webcam" http://vigilance.mit.edu/android


