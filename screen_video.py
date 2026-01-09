import subprocess
import os


from datetime import datetime
time_string = datetime.now().strftime('%d%H%M%S')
output_file = os.path.abspath(f"유료강의_추가_7.RAG용LLM파안튜닝_서빙하기_{time_string}_.mp4")
# "머리에 거는 수화기(2- 롯뽕의 Bud11s2 Pro)"
# "CABLE Output(VB-Audio Virtual Cable)"
audio = "CABLE Output(VB-Audio Virtual Cable)"
def get_comment_wanted_left(audio):
    return [
    "ffmpeg",
    "-y",
    "-f", "gdigrab",
    "-framerate", "30",
    "-offset_x", "-2880", "-offset_y", "-9",  
    "-video_size", "2880x1800",               
    "-i", "desktop",
    "-f", "dshow",
    "-i", f"audio={audio}",
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    output_file
]

def get_comment_home_right(audio):
    return [
    "ffmpeg",
    "-y",
    "-f", "gdigrab",
    "-framerate", "30",
    "-offset_x", "1920", "-offset_y", "0",   # ✅ 보조 모니터 시작 좌표
    "-video_size", "2880x1800",              # ✅ 보조 모니터 해상도
    "-i", "desktop",
    "-f", "dshow",
    "-i", f"audio={audio}",
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    output_file
]

def get_comment_home_solo(audio):
    return [
        "ffmpeg",
        "-y",
        "-f", "gdigrab",
        "-framerate", "30",
        "-offset_x", "0", "-offset_y", "0",   # 메인 모니터 시작 좌표
        "-video_size", "2880x1800",           # 단일 모니터 해상도
        "-i", "desktop",
        "-f", "dshow",
        "-i", f"audio={audio}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        output_file
    ]

def record_audio_only(audio):
    return [
        "ffmpeg",
        "-y",
        "-f", "dshow",
        "-i", f"audio={audio}",
        "-c:a", "aac", "-b:a", "192k",
        output_file
    ]

print("녹화 시작... 'q' 눌러 종료하세요.")
subprocess.call(get_comment_home_solo(audio))
print("저장 완료:", output_file)
