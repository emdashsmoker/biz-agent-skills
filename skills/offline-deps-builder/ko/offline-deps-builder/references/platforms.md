# 플랫폼별 제약

이 파일의 수치와 설정 이름은 2026년 9월 기준이다. 플랫폼 정책은 자주 바뀌므로 웹 검색을 쓸 수 있으면 각 항목의 공식 문서에서 현재 값을 확인한다.

## 스킬 업로드 한도

| 플랫폼 | 한도 | 공식 문서 |
|---|---|---|
| Claude API | 모든 파일의 압축 해제 합계 30MB | https://platform.claude.com/docs/en/build-with-claude/skills-guide |
| claude.ai | 공식 문서에 용량 수치 없음. description 1,024자 이하, 폴더 이름과 name 일치 | https://claude.com/docs/skills/how-to |
| OpenAI API | 압축 해제 합계 25MB, zip 50MB, 파일 500개 | https://developers.openai.com/api/docs/guides/tools-skills |
| ChatGPT | 공식 도움말에 용량 수치 없음 | https://help.openai.com/en/articles/20001066-skills-in-chatgpt |

claude.ai에서는 파일이 200개를 넘는 zip의 설치가 거부되었다는 사용자 보고가 있다(https://github.com/Imbad0202/academic-research-skills/discussions/21). 공식 수치가 없는 플랫폼은 가장 작은 공식 수치인 25MB와 보고된 파일 수 200개를 기준으로 삼는다.

## 네트워크 설정

claude.ai의 코드 실행 네트워크 수준은 아래 표와 같다. Team과 Enterprise 조직은 관리자가 정하고 개인 요금제는 사용자가 정한다. Enterprise의 기본값은 차단이고 Team의 기본값은 패키지 관리자 허용이다(https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude).

| 수준 | 접속 범위 |
|---|---|
| 차단 | 사전 설치 패키지만 사용 |
| 패키지 관리자 허용 | npm, PyPI, GitHub, crates.io, Ubuntu 저장소, Yarn |
| 패키지 관리자와 지정 도메인 허용 | 위 목록과 관리자가 추가한 도메인 |
| 전체 허용 | 법적 차단 목록을 제외한 전체 인터넷 |

패키지 관리자 허용 수준에서도 Maven 저장소, 모델 허브, 폰트 배포 사이트, 오피스 확장 사이트, 딥러닝 프레임워크의 CPU판 전용 저장소는 허용 목록에 없다. 이 수준에서도 의존성 스킬이 필요한 경우가 많다.

문서상 허용된 도메인이 실제 환경에서 막혀 있는 경우가 있다. 같은 호스트라도 HTTPS 다운로드는 막히고 git 프로토콜은 통과하는 환경이 있다. 출처마다 직접 요청해 본 결과로 판단한다.

Claude API의 스킬 실행 환경은 네트워크가 없고 실행 중 패키지 설치가 불가능하다. 필요한 파일은 모두 스킬에 담거나 사전 설치 패키지로 해결한다.

ChatGPT와 OpenAI API는 공식 문서에 컨테이너 네트워크의 상세 범위가 없다. 현재 세션의 도구 목록과 직접 요청해 본 결과로 판단한다.

쿠버네티스 같은 에이전트 실행 환경은 조직 정책에 따라 다르다. 조직 내부 패키지 미러나 공유 볼륨이 있는지 사용자에게 묻는다.

## 첨부 한도

| 플랫폼 | 한도 | 공식 문서 |
|---|---|---|
| claude.ai 채팅 | 파일당 500MB, 채팅당 20개 | https://support.claude.com/en/articles/8241126-upload-files-to-claude |
| claude.ai 프로젝트 파일 | 파일당 30MB | 위와 같음 |
| ChatGPT | 파일당 512MB | https://help.openai.com/en/articles/8555545-file-uploads-faq |

첨부 파일이 컨테이너의 어느 경로에 놓이는지는 플랫폼마다 다르다. 파일 이름으로 찾는다.

## 스킬 폴더의 성질

- 스킬 폴더는 읽기 전용으로 마운트되기도 한다. 페이로드는 쓰기 가능한 작업 경로에 푼다
- zip 업로드와 동기화 과정에서 파일의 실행 권한이 사라지기도 한다. 실행 파일은 작업 경로로 복사한 뒤 실행 권한을 준다
- 스킬 폴더의 절대 경로는 플랫폼마다 다르다. 의존성 스킬 안의 파일은 SKILL.md 위치를 기준으로 찾는다

## 실행 환경 확인 명령

리눅스 컨테이너 기준 예시이다. 없는 명령은 건너뛴다.

```
uname -m                          # CPU 아키텍처
ldd --version | head -1           # glibc 버전 (musl 환경은 musl로 표시)
cat /etc/os-release | head -3     # 배포판과 버전
python3 -m pip debug --verbose | grep -A8 "Compatible tags"   # 설치 가능한 휠 태그
node --version; java -version
id -u                             # 0이면 root
df -h /tmp; free -m               # 디스크와 메모리
python3 -m pip list               # 사전 설치 Python 패키지
curl -sS -m 10 -o /dev/null -w "%{http_code}\n" https://pypi.org/simple/   # 출처별 접속 확인
```

## 기본 가정

실행 환경에 접근할 수 없고 사용자 답도 받을 수 없으면 아래 가정을 쓰고 목록 파일에 적는다.

- 리눅스, x86_64, glibc 계열
- glibc 버전은 모르는 상태로 보고 오래된 glibc에서도 도는 빌드를 고른다
- Python과 Node.js 버전은 모르는 상태로 보고 버전과 무관한 형식(순수 Python 휠, abi3 휠, WASM)을 우선한다. 버전별 파일만 있으면 여러 버전을 함께 담을지 용량과 함께 판단한다
- 쓰기 가능한 경로는 /tmp
