from faster_whisper import WhisperModel
from pathlib import Path

AUDIO_PATHS = [
    # "C:\\Users\\user\\Music\\음성 20250930_05.m4a",

    # "C:\\Users\\user\\Music\\음성 20251001_01.m4a",
    # "C:\\Users\\user\\Music\\음성 20251001_02.m4a",
    # "C:\\Users\\user\\Music\\음성 20251001_03.m4a",

    # "C:\\Users\\user\\Music\\음성 20251002_01.m4a",
    # "C:\\Users\\user\\Music\\음성 20251002_02.m4a",
    # "C:\\Users\\user\\Music\\음성 20251002_03.m4a",
    # r"C:\PythonProject\sound_to_text\유료강의 1_28122405_.mp4"
    # r"C:\PythonProject\sound_to_text\유료 강의\2강\유료강의 2.mp4"
    # r"C:\PythonProject\sound_to_text\유료강의 2.mp4"
    r"C:\PythonProject\sound_to_text\유료강의 3강.mp4"
]

# 모델 크기: tiny / base / small / medium / large-v3
# 한국어면 small~medium 이상 권장, 정확도는 large-v3가 최고
model = WhisperModel("large-v3", "cuda", compute_type="int8")  

# 자막/텍스트 저장
def sec_to_srt_ts(s):
    ms = int(round((s - int(s)) * 1000))
    s = int(s)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)    
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def start():
    for path in AUDIO_PATHS:
        segments, info = model.transcribe(
        path,
        beam_size=5,
        vad_filter=True,                   
        vad_parameters=dict(min_silence_duration_ms=500),
        language="ko"                      
        )
        print(f"Detected language: {info.language} (prob={info.language_probability:.2f})")
        srt_lines = []
        txt_lines = []
        step = 0 
        for i, seg in enumerate(segments, start=1):
            start = sec_to_srt_ts(seg.start)
            end = sec_to_srt_ts(seg.end)
            text = seg.text.strip()
            srt_lines.append(f"{i}\n{start} --> {end}\n{text}\n")
            txt_lines.append(text)    
            step += 1
            print(step)
        OUT_BASENAME = Path(path).with_suffix("")  # 확장자 제거한 경로
        # 파일로 저장
        print("파일저장 시작")
        (OUT_BASENAME.with_suffix(".srt")).write_text("\n".join(srt_lines), encoding="utf-8")
        (OUT_BASENAME.with_suffix(".txt")).write_text("\n".join(txt_lines), encoding="utf-8")
        print("완료")
        



