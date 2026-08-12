prompts = [
    {
        "제목": "블로그 글쓰기",
        "내용": "블로그 글을 써줘",
        "카테고리": "텍스트 생성",
        "즐겨찾기": False
    },
    {
        "제목": "영어 번역",
        "내용": "다음 문장을 영어로 번역해줘",
        "카테고리": "텍스트 생성",
        "즐겨찾기": False
    },
    {
        "제목": "이미지 프롬프트",
        "내용": "귀여운 고양이 그림을 그려줘",
        "카테고리": "이미지 생성",
        "즐겨찾기": False
    }
]

def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    title = input("제목을 입력하세요: ")
    while title.strip() == "":
        title = input("제목은 비어있을 수 없습니다. 다시 입력하세요: ")
    content = input("내용을 입력하세요: ")
    while content.strip() == "":
        content = input("내용은 비어있을 수 없습니다. 다시 입력하세요: ")

    print("카테고리 선택:")
    default_categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    for i, c in enumerate(default_categories):
        print(f"{i+1}. {c}")
    cat_choice = input("번호 선택 (직접 입력하려면 텍스트 입력): ")
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(default_categories):
        category = default_categories[int(cat_choice) - 1]
    else:
        category = cat_choice

    prompt = {"제목": title, "내용": content, "카테고리": category, "즐겨찾기": False}
    prompts.append(prompt)
    print(f"'{title}' 프롬프트가 추가되었습니다!")

def show_prompts():
    print("\n--- 프롬프트 목록 ---")
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다!")
        return
    for i, prompt in enumerate(prompts):
        star = " ⭐" if prompt["즐겨찾기"] else ""
        print(f"{i+1}. [{prompt['카테고리']}] {prompt['제목']}{star}")
    print(f"\n총 {len(prompts)}개의 프롬프트")
    
def search_by_category():
    print("\n--- 카테고리별 조회 ---")
    categories = []
    for prompt in prompts:
        if prompt["카테고리"] not in categories:
            categories.append(prompt["카테고리"])

    print("카테고리 목록:")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

    choice = input("\n카테고리 번호를 입력하세요: ")
    selected = categories[int(choice) - 1]

    print(f"\n[{selected}] 카테고리 프롬프트:")
    for i, prompt in enumerate(prompts):
        if prompt["카테고리"] == selected:
            print(f"\n[{i+1}. [{prompt['카테고리']}] {prompt['제목']}{star}")
    print(f"\n총 {len(prompts)}개의 프롬프트") 

                
def search_prompt():
    print("\n--- 프롬프트 검색 ---")
    keyword = input("검색어를 입력하세요: ")
    results = []
    for prompt in prompts:
        if keyword in prompt["제목"] or keyword in prompt["내용"]:
            results.append(prompt)
    if len(results) == 0:
        print("검색 결과가 없습니다!")
        return
    print(f"\n'{keyword}' 검색 결과: {len(results)}개")
    for i, prompt in enumerate(results):
        print(f"\n[{i+1}] 제목: {prompt['제목']}")
        print(f"     내용: {prompt['내용']}")

def main():
    print("=== 프롬프트 관리 프로그램 ===")
    while True:
        print("\n--- 메뉴 ---")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 목록 보기")
        print("3. 카테고리별 조회")
        print("4. 프롬프트 검색")
        print("5. 프롬프트 상세 보기")
        print("6. 종료")
        choice = input("\n번호를 입력하세요: ")

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_prompts()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            print("프로그램을 종료합니다!")
            break
        else:
            print("잘못된 번호예요. 다시 입력해주세요!")

def show_detail():
    print("\n--- 프롬프트 상세 보기 ---")
    show_prompts()
    choice = input("\n번호를 입력하세요: ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다!")
        return
    p = prompts[int(choice) - 1]
    star = "⭐" if p["즐겨찾기"] else "없음"
    print("─" * 20)
    print(f"제목: {p['제목']}")
    print(f"카테고리: {p['카테고리']}")
    print(f"즐겨찾기: {star}")
    print("─" * 20)
    print(f"내용:\n{p['내용']}")


main()