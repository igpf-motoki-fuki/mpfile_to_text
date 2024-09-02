import os
from moviepy.editor import VideoFileClip, AudioFileClip
from faster_whisper import WhisperModel

def extract_audio_from_video(video_file, output_audio_file):
    # MP4ファイルから音声を抽出し、WAV形式で保存
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(output_audio_file, codec='pcm_s16le')
    audio.close()
    video.close()

def convert_mp3_to_wav(mp3_file, output_audio_file):
    # MP3ファイルをWAV形式に変換
    audio = AudioFileClip(mp3_file)
    audio.write_audiofile(output_audio_file, codec='pcm_s16le')
    audio.close()

def transcribe_audio_to_text(audio_file):
    # 音声ファイルをテキストに変換
    model_size = "large-v3"
    model = WhisperModel(model_size, device="cpu", compute_type="auto")  # モデルのロード（必要に応じてサイズを変更可能）
    segments, info = model.transcribe(audio_file)
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    text = ""
    for segment in segments:
        text += segment.text + "\n"
    return text

def convert_media_to_text(media_file, output_text_file):
    # MP4またはMP3ファイルをテキストに変換
    # 一時的なWAVファイル名
    wav_file = media_file.replace('.mp4', '.wav').replace('.mp3', '.wav')
    
    # メディアファイルの種類に応じて音声を抽出または変換
    if media_file.endswith('.mp4'):
        extract_audio_from_video(media_file, wav_file)
    elif media_file.endswith('.mp3'):
        convert_mp3_to_wav(media_file, wav_file)
    
    # 音声をテキストに変換
    text = transcribe_audio_to_text(wav_file)
    
    # 結果をテキストファイルに保存
    with open(output_text_file, 'w') as f:
        f.write(text)
    
    # 一時的なWAVファイルを削除
    os.remove(wav_file)

def process_directory(directory):
    # ディレクトリ内のすべてのMP4およびMP3ファイルを処理
    for filename in os.listdir(directory):
        if filename.endswith(".mp4") or filename.endswith(".mp3"):
            media_file = os.path.join(directory, filename)
            output_directory = os.path.join(directory, "output")
            output_filename = filename.rsplit('.', 1)[0] + '.txt'
            pwd_files = os.listdir("./output")
            if not output_filename in pwd_files :
                output_text_file = os.path.join(output_directory, filename.rsplit('.', 1)[0] + '.txt')
                convert_media_to_text(media_file, output_text_file)
                print(f"Processed {filename} to {output_text_file}")
            else :
                print(f"{filename} has already been processed. Please check the output directory.")

if __name__ == "__main__":
    # 処理するディレクトリを指定
    directory = "./"  # 現在のディレクトリ
    process_directory(directory)
