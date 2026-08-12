STATE_FILE = "state.json"

DEFAULT_QUIZZES = [
    {
        "question": "다음 중 Python에서 변수 이름(식별자)으로 사용할 수 없는 것은?",
        "choices": ["my_var", "user2", "for", "_score"],
        "answer": 3,
        "hint": "파이썬 예약어(keyword)는 식별자로 사용할 수 없습니다."
    },
    {
        "question": "다음 중 Python에서 한 줄 주석을 작성할 때 사용하는 기호는?",
        "choices": ["//", "#", "/*", "--"],
        "answer": 2,
        "hint": "파이썬 한 줄 주석은 특수 기호 하나로 시작합니다."
    },
    {
        "question": "다음 중 Python에서 리스트의 맨 뒤에 새 요소를 추가할 때 사용하는 메서드는?",
        "choices": ["add()", "append()", "push()", "insert()"],
        "answer": 2,
        "hint": "'덧붙이다'라는 뜻의 영단어로 시작하는 메서드입니다."
    },
    {
        "question": "다음 중 Python 조건문에서 사용하는 키워드로 올바른 것은?",
        "choices": ["else if", "elseif", "elif", "then"],
        "answer": 3,
        "hint": "else와 if를 합쳐 줄인 표현입니다."
    },
    {
        "question": "다음 중 Python에서 문자를 출력할 때 사용하는 기본 내장 함수는?",
        "choices": ["console.log()", "print()", "printf()", "System.out.println()"],
        "answer": 2,
        "hint": "괄호 안의 값을 화면에 표시하는 함수입니다."
    }
]

MENU_TEXT = """
========================================
        🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 퀴즈 삭제
6. 점수 기록 히스토리
7. 종료
========================================"""
