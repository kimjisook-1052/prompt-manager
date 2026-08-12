# 나만의 프롬프트 관리 프로그램

터미널에서 메뉴 번호를 입력해 프롬프트를 관리하는 콘솔 기반 프로그램입니다.
프롬프트를 카테고리별로 등록하고, 검색하고, 즐겨찾기로 관리할 수 있습니다.

## 실행 방법

```bash
python main.py
```

프로그램 실행 후 화면에 나오는 메뉴 번호를 입력하면 원하는 기능을 사용할 수 있습니다.

## 기능 목록

1. **프롬프트 추가** — 제목, 내용, 카테고리를 입력해 새 프롬프트를 등록합니다. 제목/내용은 빈 값으로 등록할 수 없습니다.
2. **프롬프트 목록 보기** — 등록된 모든 프롬프트를 카테고리와 즐겨찾기 표시(⭐)와 함께 보여줍니다.
3. **카테고리별 조회** — 카테고리를 선택하면 해당 카테고리의 프롬프트만 보여줍니다.
4. **프롬프트 검색** — 키워드로 제목/내용을 검색합니다.
5. **프롬프트 상세 보기** — 번호를 선택하면 해당 프롬프트의 전체 내용을 보여줍니다.
6. **즐겨찾기 관리** — 번호를 선택해 즐겨찾기를 추가하거나 해제합니다.
7. **즐겨찾기 목록** — 즐겨찾기로 등록된 프롬프트만 모아서 보여줍니다.
8. **종료** — 프로그램을 종료합니다.

## 카테고리 종류

텍스트 생성, 이미지 생성, 영상 생성, 페르소나, 자동화, 기타

## 기본 등록 프롬프트

프로그램 실행 시 아래 3개의 프롬프트가 기본으로 등록되어 있습니다.

- 블로그 글쓰기 (텍스트 생성)
- 영어 번역 (텍스트 생성)
- 이미지 프롬프트 (이미지 생성)

## 개발 환경

- Python 3.10 이상
- VSCode
- Git / GitHub


제출물 정리

GitHub 저장소 URL: https://github.com/kimjisook-1052/prompt-manager

1. 스크린샷 모으기

 개발 환경: python --version, git --version 결과

 <img width="557" height="69" alt="image" src="https://github.com/user-attachments/assets/2823a646-aaf4-4acf-afda-d8b66f2c7819" />


 Git 설정: git config --list (이름/이메일 확인)

 <img width="552" height="310" alt="image" src="https://github.com/user-attachments/assets/2ac8cb85-8ab8-4a08-b20f-862d36a01c3f" />


 메뉴 화면
 
 <img width="436" height="202" alt="image" src="https://github.com/user-attachments/assets/3584afcf-b589-4485-aea6-9212b0ea2580" />


 프롬프트 추가 과정

<img width="553" height="231" alt="image" src="https://github.com/user-attachments/assets/27039586-fb1b-41ec-a856-89aa98739622" />

 
 목록 보기

<img width="547" height="139" alt="image" src="https://github.com/user-attachments/assets/aacabcbe-d376-4979-ac82-e1225e93381e" />


 
 카테고리별 조회

<img width="471" height="242" alt="image" src="https://github.com/user-attachments/assets/b9d76947-03cf-459d-b1c9-870eb636abbe" />

 
 검색 결과

<img width="428" height="138" alt="image" src="https://github.com/user-attachments/assets/7e430055-c2a2-41f6-ae0f-d68b7e728290" />

 
 상세 보기

 
 <img width="406" height="151" alt="image" src="https://github.com/user-attachments/assets/54476c40-d61b-4b92-885b-7093f7debe59" />

 즐겨찾기 관리/목록

<img width="520" height="92" alt="image" src="https://github.com/user-attachments/assets/11b7ade7-2da3-4ced-a724-7b9e01eea0ae" />

 
 git log --oneline --graph
 
 <img width="564" height="241" alt="image" src="https://github.com/user-attachments/assets/1bc4cf59-1d5d-4943-a79d-39be54fceb4b" />

