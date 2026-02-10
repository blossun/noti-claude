# Noti Claude

Claude Code 사용 시 응답 완료 및 권한 요청 시점에 알림음을 재생




https://github.com/user-attachments/assets/9331f6b2-a2c0-4246-b478-67479fe87096






## 파일 구성

- `play_sound.py`: macOS의 `afplay` 명령어를 사용하여 알림음을 재생하는 스크립트
- `ring.mp3`: 재생할 알림음 파일
- 다른 알림음을 설정하고 싶다면 `ring1.mov`, `ring2.mp3`가 있으며, 직접 음성파일을 준비해서 변경 가능 (`play_sound.py` 파일에서 파일명 수정 필요)

## 사용법

### 1. 프로젝트 복제

```bash
git clone https://github.com/blossun/noti-claude.git
cd noti-claude
```

### 2. 의존성 설치

```bash
uv sync
```

### 3. 테스트 실행

```bash
uv run play_sound.py
```

## Claude Code 훅 설정

Claude Code에서 이 알림 시스템을 사용하려면 `settings.json` 파일에 훅(Hook)을 설정해야 합니다.

### 설정 파일 위치

다음 중 하나의 위치에 설정 파일을 생성/수정하세요:

| 설정 범위 | 파일 위치 | 적용 대상 |
|----------|-----------|-----------|
| **전역 설정** | `~/.claude/settings.json` | 모든 Claude Code 세션 |
| **프로젝트별 설정** | `프로젝트_루트/.claude/settings.json` | 해당 프로젝트만 |

### 설정 내용

선택한 설정 파일에 다음 JSON을 추가하세요:  
**⚠️ 중요**: `hooks` 파일을 복사한 후, 파일 내의 `path/to/noti-claude` 부분을 실제 프로젝트 경로로 수정해야 합니다.


```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "uv run path/to/noti-claude/play_sound.py"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "uv run path/to/noti-claude/play_sound.py"
          }
        ]
      }
    ]
  }
}
```

### 훅 이벤트 타입 설명

- **`Stop`**: Claude Code가 응답을 완료했을 때 실행
- **`PermissionRequest`**: 권한 확인이나 사용자 입력이 필요할 때 실행

### 추가 설정 옵션

다른 유용한 훅 이벤트들도 사용할 수 있습니다:

- `Stop`: 응답 완료 시
- `PermissionRequest`: 권한 요청 시
- `SessionStart`: 세션 시작 시
- `SessionEnd`: 세션 종료 시
- `UserPromptSubmit`: 사용자 입력 제출 시
- `Notification`: 알림 발생 시

각 이벤트에 동일한 형식의 훅을 추가할 수 있습니다.

## 경로 설정 주의사항

- **절대 경로 사용**: 설정에서는 `play_sound.py`의 절대 경로를 사용하세요
- **틸드(~) 확장**: `~/path/to/file` 형식도 지원됩니다
- **uv 사용**: `uv run` 명령어를 사용하여 올바른 Python 환경에서 실행되도록 하세요

## 문제 해결

### 소리가 재생되지 않는 경우

1. 파일 경로가 올바른지 확인
2. `uv`가 설치되어 있는지 확인
3. macOS에서 `afplay` 명령어 사용 가능 여부 확인
4. 음량 설정 확인

### 설정이 적용되지 않는 경우

1. JSON 문법이 올바른지 확인
2. Claude Code 재시작
3. 설정 파일 권한 확인

## Options - Hooks 제어 명령어

편리한 훅 관리를 위해 `hooks` 명령어를 제공합니다.

### hooks 명령어 설정

전역에서 `hooks` 명령어를 사용할 수 있도록 설정:

**⚠️ 중요**: `hooks` 파일을 복사한 후, 파일 내의 `path/to/noti-claude` 부분을 실제 프로젝트 경로로 수정해야 합니다.

```bash
# 1. bin 디렉토리 만들기
mkdir -p ~/bin

# 2. hooks 파일 복사
cp hooks ~/bin/hooks

# 3. hooks 파일의 경로 수정
# 텍스트 에디터로 ~/bin/hooks 파일을 열어서
# 'path/to/noti-claude'를 실제 프로젝트 경로로 변경하세요
# 예: path/to/noti-claude → ~/solar/project/noti-claude

# 4. PATH에 추가 (한 번만 설정)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
# bash 사용자는: echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc

# 5. 현재 터미널에서 즉시 적용
source ~/.zshrc
```

### hooks 명령어 사용법

설정 후 어디서든 다음 명령어로 알림음을 제어할 수 있습니다:

```bash
# 알림음 켜기
hooks on

# 알림음 끄기
hooks off

# 사용법 보기
hooks
```

**⚠️ 중요: hooks on/off 명령어 실행 후에는 반드시 Claude Code를 재시작해야 변경사항이 적용됩니다!**

### 동작 방식

- `hooks on`: `~/.claude/settings.json`에서 주석 처리된 명령어를 활성화
- `hooks off`: `~/.claude/settings.json`에서 명령어를 주석 처리하여 비활성화
- 기존 설정은 그대로 유지되며 command 부분만 토글됩니다

### 예시

```bash
$ hooks off
🔇 Hooks 비활성화됨

$ hooks on
🔊 Hooks 활성화됨

$ hooks
Usage: hooks [on|off]

  hooks on   - Claude 알림음 활성화
  hooks off  - Claude 알림음 비활성화
```

## 요구사항

- macOS (afplay 명령어 사용)
- Python 3.8+
- uv (Python 패키지 관리자)

## 라이선스

이 프로젝트는 개인 사용을 위한 것입니다.
