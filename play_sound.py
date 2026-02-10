import os
import sys
from pathlib import Path

def main():
    # 현재 스크립트 파일과 같은 디렉토리에서 ring.mp3 찾기
    script_dir = Path(__file__).parent
    audio_file = script_dir / "ring.mp3"

    if not audio_file.exists():
        print(f"Error: {audio_file} not found!")
        sys.exit(1)

    print("Playing ring.mp3...")

    # macOS에서 afplay 명령어를 사용하여 오디오 재생
    try:
        os.system(f'afplay "{audio_file}"')
        print("Sound played successfully!")
    except Exception as e:
        print(f"Error playing sound: {e}")


if __name__ == "__main__":
    main()
