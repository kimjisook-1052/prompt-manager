prompts = []

while True:
    print("\n--- 메뉴 ---")
    print("1.등록 2.목록 3.검색 4.종료")
    
    menu = input("번호 선택: ")

    if menu == '1':
        t = input("등록할 제목:")
        c = input("등록할 내용: ")
        prompts.append({"title": t, "content": c})
        print("저장 완료!")

    elif menu == '2':
        print(f"총 {len(prompts)}개가 있습니다.")
        for p in prompts:
            print(f"- {p['title']}")

    elif menu == '3':
        search = input("검색할 단어를 입력하세요:")
        found = False  # <- 이 줄의 앞 간격이 21번 줄과 똑같아야 해요!
        
        for p in prompts:
            if search in p['title']:
                print(f"결과: {p['title']} / {p['content']}")
                found = True
        
        if found == False:
            print("❌ 검색 결과가 없습니다.")
