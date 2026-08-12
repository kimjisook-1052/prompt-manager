prompts = []

def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    title = input("제목을 입력하세요: ")
    content = input("내용을 입력하세요: ")
    prompt = {"제목": title, "내용": content}
    prompts.append(prompt)
    print(f"'{title}' 프롬프트가 추가되었습니다!")

def show_prompts():
    print("\n--- 프롬프트 목록 ---")
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다!")
        return
    for i, prompt in enumerate(prompts):
        print(f"\n[{i+1}] 제목: {prompt['제목']}")
        print(f"     내용: {prompt['내용']}")

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
        print("3. 프롬프트 검색")
        print("4. 종료")
        choice = input("\n번호를 입력하세요: ")

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_prompts()
        elif choice == "3":
            search_prompt()
        elif choice == "4":
            print("프로그램을 종료합니다!")
            break
        else:
            print("잘못된 번호예요. 다시 입력해주세요!")

main()