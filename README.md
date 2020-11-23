# Video_website







**ffmpeg压缩视频**

`FFmpeg`项目由以下几部分组成：

-  `FFmpeg`视频文件转换命令行工具,也支持经过实时电视卡抓取和编码成视频文件；
-  `ffserver`基于`HTTP`、`RTSP`用于实时广播的多媒体服务器.也支持时间平移；
-  `ffplay`用 `SDL`和`FFmpeg`库开发的一个简单的媒体播放器；
-  `libavcodec`一个包含了所有`FFmpeg`音视频编解码器的库。为了保证最优性能和高可复用性，大多数编解码器从头开发的；
-  `libavformat`一个包含了所有的普通音视格式的解析器和产生器的库

```
-i 设定输入流 
-f 设定输出格式 
-ss 开始时间 
#视频
-b 设定视频流量(码率)，默认为200Kbit/s 
-r 设定帧速率，默认为25 
-s 设定画面的宽与高 
-aspect 设定画面的比例 
-vn 不处理视频 
-vcodec 设定视频编解码器，未设定时则使用与输入流相同的编解码器 
#音频
-ar 设定采样率 
-ac 设定声音的Channel数 
-acodec 设定声音编解码器，未设定时则使用与输入流相同的编解码器 
-an 不处理音频
```



视频压缩

```
ffmpeg -i jun2.mp4 -vcodec h264 -vf "scale=480:-1" -f mp4 -y jun2_480.mp4
```



```
ffmpeg -i input.mkv -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 output.mp4

hd720 分辨下降到720P

-crf 23 是设置质量等级的 23 越高表示质量越差，越模糊

ffmpeg -i 1.mp4 -vcodec h264 -vf "scale='max(480,iw*0.5)':-1" -r 15 -acodec libmp3lame -ac 2 -ar 22050 -f mp4 -y 3.mp4
```

批量压缩

```
import os
labelFile_path=r"F:\SDDR\datasets\surveillance\label"
x264File_path=r"F:\SDDR\datasets\surveillance\x264"

os.chdir(labelFile_path)
x264File_list=os.listdir(x264File_path)
for x264File in x264File_list: #qpxx
    labelFile_list=os.listdir(labelFile_path)
    for label in labelFile_list:    #xxx.mp4
        cmd_x264="ffmpeg -i "+label+" -c:v libx264 -preset medium -qp "\
                 +x264File[2:]+" "+x264File_path+"/"+x264File+"/"+label
        os.system(cmd_x264)
```

字幕提取

```
ffmpeg -i jun.mkv -vcodec copy –an video.mp4

https://www.cnblogs.com/wainiwann/p/4128154.html
```



mkv转MP4

```
ffmpeg -i jun2.mkv -c:v copy -c:a copy jun2.mp4
```



转m3u8格式

```
ffmpeg -i jun.mp4 -f segment -segment_time 10 -segment_format mpegts -segment_list /media/index.m3u8 -c copy -bsf:v h264_mp4toannexb -map 0 /media/out-%03d.ts

这个是把xxx.mp4视频切成功每10秒一个小的ts视频的m3u8文件  %03d指的是从000开始计数
```

Access to XMLHttpRequest at 'http://47.104.165.92:8000/download/test/media/index.m3u8' from origin 'http://47.104.165.92' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. 



剪切视频

```
ffmpeg -ss 00:10:00 -to 00:20:00 -i jun.mkv -vcodec copy -acodec copy jun2.mkv
剪切10分钟到20分钟的视频，需要注意的是:-ss在-i之前 有助于提高搜索速度，因此建议：-ss在-i之前
```

