prompts = []

while True:
    print("\n--- 메뉴 ---")
    print("1.등록 2.목록 3.검색 4.종료")
    
    menu = input("번호 선택: ")

    if menu == '1':
        t = input("제목: ")
        c = input("내용: ")
        prompts.append({"title": t, "content": c})
        print("저장 완료!")

    elif menu == '2':
        print(f"총 {len(prompts)}개가 있습니다.")
        for p in prompts:
            print(f"- {p['title']}")

    elif menu == '3':
        search = input("사과 ")
        for p in prompts:
            if search in p['title']: # 제목에 검색어가 있으면 출력
                print(f"결과: {p['title']} / {p['content']}")

    elif menu == '4':
        print("종료합니다.")
        break
