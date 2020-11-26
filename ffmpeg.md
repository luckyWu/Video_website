# ffmpeg

```
ffmpeg -i 2.mp4 -f segment -segment_time 10 -segment_format mpegts -segment_list /var/www/html/media/720p_qb/index.m3u8 -c copy -vf "scale=480:-1" -bsf:v h264_mp4toannexb -map 0 /var/www/html/media/720p_qb/out-%04d.ts
```

```
ffmpeg -i y1.mp4 -f segment -segment_time 5 -segment_format mpegts -segment_list /root/freemv/public/media/9rIJfX77777X11/index.m3u8 -c copy -bsf:v h264_mp4toannexb -map 0 /root/freemv/public/media/9rIJfX77777X11/out-%03d.ts
```

