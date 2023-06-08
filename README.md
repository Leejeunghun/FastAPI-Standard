# FastApi 기초

# 서론
--------------

이 저장소의 설립 목적은 작성자는 웹 개발에 관심이 많다.
왜냐하면 작성자는 웹 개발 관련해서 앞으로 할 수 있는 일이 많아질 것으로 예상된다. 모든 회사들이 자기들의 개인 웹을가지고 고객들과 소통하는 것은 요새는 기본이다. 
 작성자는 자바 및 자바 스크립트 같은 기존의 웹개발의 필수적인 언어 기초가 없습니다. 물론 해당 언어를 공부하여 웹개발을 진행하면 좋지만 기존의 언어 지식이 있는 Python을 기반으로한 웹프레임워크인 FastApi 공부하는것이 효율적으로 판단하였습니다. 

# 공부 자료 링크

모든 자료는 에서 참고하여 공부하였습니다.

https://wikidocs.net/175035

https://github.com/pahkey/fastapi-book


# 공부 계획
1. 기본 구조 생성하기 (목표 일정 05월 03일) 2-02장
- DB 설정을 해보자
2. 목록 API 만들기 (목표 일정 05월 05일)    2-10장
3. 파이보 서비스 만들기 (목표 일정 05월 06일) 3장 마무리
4. 공공 데이터 이용하여 데이터 표시 (목표 일정 05월 7일) --> 무한대기


* 4장은 직접 테스트 안하고 문서 보면서 참고 할 예정

# 기초 명령어
 uvicorn main:app --reload


가상환경 만들기
``` bash
mkdir venvs
cd venvs
python -m venv myapi
```

가상환경 진입하기
```bash
C:\venvs> cd C:\venvs\myapi\Scripts
C:\venvs\myapi\Scripts> activate
(myapi) C:\venvs\myapi\Scripts>
```

가상 환경에서 FastAPI 설치하기
```bash
 pip install fastapi
 python -m pip install --upgrade pip

```


svelte 설치하기
>
```bash
 npm create vite@latest frontend -- --template svelte

  cd frontend
  npm install
  npm run dev
```


# 설치 모듈

``` bash
 pip install "uvicorn[standard]"

pip install "pydantic[email]"
pip install "passlib[bcrypt]"
pip install python-multipart
pip install "python-jose[cryptography]"


npm install svelte-spa-router
npm install bootstrap
npm install moment # 시간 기록 하기 위해 사용
npm install qs
```

# DB 관련 업데이트
``` bash
alembic revision --autogenerate
alembic upgrade head
```
-> 이것 유용한지 모르겠음

# 공부 저장소 링크

https://github.com/Leejeunghun/FastAPI-Standard


curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&sudo apt-get install -y nodejs
