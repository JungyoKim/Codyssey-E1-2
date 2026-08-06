import json
import os
import random
from datetime import datetime

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

class Quiz:
    def __init__(self, question:str, choices:list[str], answer:int, hint:str = ""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def is_correct(self, user_answer: int) -> bool:
        return self.answer == user_answer

    def display(self, index: int):
        print(f"\n[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

class QuizGame:
    def __init__(self, filepath=STATE_FILE):
        self.filepath = filepath
        self.quizzes = []
        self.best_score = 0
        self.total_questions_at_best = 0
        self.history = []
        self.load_state()

    def _load_defaults(self):
        self.quizzes = [Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "")) for q in DEFAULT_QUIZZES]
        self.best_score = 0
        self.total_questions_at_best = 0
        self.history = []

    def load_state(self):
        if not os.path.exists(self.filepath):
            self._load_defaults()
            print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            loaded_quizzes = [
                Quiz(q["question"], q["choices"], q["answer"], q.get("hint", ""))
                for q in data["quizzes"]
            ]
            if not loaded_quizzes:
                raise ValueError("저장된 퀴즈 목록이 비어 있습니다.")

            self.quizzes = loaded_quizzes
            self.best_score = data.get("best_score", 0)
            self.total_questions_at_best = int(data.get("total_questions_at_best", 0))
            self.history = data.get("history", []) if isinstance(data.get("history", []), list) else []
            print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고 점수 {self.best_score}점)")
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
            print(f"데이터 파일이 손상되어 기본 퀴즈 데이터로 초기화합니다. ({e})")
            self._load_defaults()

    def get_valid_input(self, prompt: str, min_value: int, max_value: int) -> int:
        while True:
            try:
                raw_input = input(prompt).strip()
                if not raw_input:
                    print("빈 입력입니다. 다시 입력해주세요.")
                    continue
                value = int(raw_input)
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"입력 값은 {min_value}에서 {max_value} 사이의 정수여야 합니다.")
            except ValueError:
                print("유효하지 않은 입력입니다. 정수를 입력해주세요.")

    def play(self):
        if not self.quizzes:
            print("퀴즈가 없습니다.")
            return

        num_questions = self.get_valid_input(
            f"몇 문제를 풀지 선택하세요 (1-{len(self.quizzes)}): ", 1, len(self.quizzes)
        )

        print(f"\n퀴즈를 시작합니다. (총 {num_questions}문제)")
        print("-" * 40)

        score = 0

        quiz_order = self.quizzes[:]
        random.shuffle(quiz_order)
        quiz_order = quiz_order[:num_questions]

        for i, quiz in enumerate(quiz_order, 1):
            quiz.display(i)
            user_answer = self.get_valid_input(
                f"정답 번호를 입력하세요 (힌트 보기: 0, 1-{len(quiz.choices)}): ", 0, len(quiz.choices)
            )

            hint_used = False
            if user_answer == 0:
                hint_used = True
                print(f"힌트: {quiz.hint}" if quiz.hint else "이 문제에는 힌트가 없습니다.")
                user_answer = self.get_valid_input(
                    f"정답 번호를 입력하세요 (1-{len(quiz.choices)}): ", 1, len(quiz.choices)
                )

            if quiz.is_correct(user_answer):
                points = 0.5 if hint_used else 1
                score += points
                print(f"정답입니다! (힌트 사용, +{points}점)" if hint_used else "정답입니다!")
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번 입니다.")

        total = len(quiz_order)
        score_display = int(score) if score == int(score) else score
        print("\n" + "=" * 40)
        print(f"결과: {total}문제 중 {score_display}점 획득.")

        self.history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total": total,
            "score": score
        })

        if score > self.best_score:
            self.best_score = score
            self.total_questions_at_best = total
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

        self.save_state()

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        while True:
            question = input("문제: ").strip()
            if question:
                break
            print("문제는 빈 값일 수 없습니다. 다시 입력해주세요.")

        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print("선택지는 빈 값일 수 없습니다. 다시 입력해주세요.")

        answer = self.get_valid_input("정답 번호를 입력하세요. (1-4): ", 1, 4)
        hint = input("힌트 (선택 사항, 없으면 Enter): ").strip()

        self.quizzes.append(Quiz(question, choices, answer, hint))

        self.save_state()
        print("퀴즈가 추가되었습니다.")

    def save_state(self):
        try:
            quiz_dicts = []
            for q in self.quizzes:
                quiz_dicts.append(q.to_dict())

            data = {
                "quizzes": quiz_dicts,
                "best_score": self.best_score,
                "total_questions_at_best": self.total_questions_at_best,
                "history": self.history
            }

            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"데이터 저장 실패: {e}")

    def show_quiz_list(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        # 2. 퀴즈 목록 출력
        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)

    def delete_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        self.show_quiz_list()
        index = self.get_valid_input(
            f"삭제할 퀴즈 번호를 입력하세요 (1-{len(self.quizzes)}): ", 1, len(self.quizzes)
        )
        removed = self.quizzes.pop(index - 1)
        self.save_state()
        print(f"'{removed.question}' 퀴즈를 삭제했습니다.")

    def show_best_score(self):
        print("\n" + "=" * 40)
        if self.best_score == 0 and self.total_questions_at_best == 0:
            print("아직 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}문제 정답 (총 {self.total_questions_at_best}문제 중)")
        print("=" * 40)

    def show_history(self):
        if not self.history:
            print("\n아직 플레이 기록이 없습니다.")
            return

        print(f"\n게임 기록 히스토리 (총 {len(self.history)}회)")
        print("-" * 40)
        for i, record in enumerate(self.history, 1):
            score = record.get("score", 0)
            score_display = int(score) if score == int(score) else score
            print(f"[{i}] {record.get('timestamp', '알 수 없음')} - {record.get('total', 0)}문제 중 {score_display}점")
        print("-" * 40)

    def run(self):
        while True:
            try:
                print(MENU_TEXT)
                choice = self.get_valid_input("선택: ", 1, 7)

                if choice == 1:
                    self.play()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    self.delete_quiz()
                elif choice == 6:
                    self.show_history()
                elif choice == 7:
                    print("\n프로그램을 종료합니다.")
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n\n입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
                break

        self.save_state()


if __name__ == "__main__":
    manager = QuizGame()
    manager.run()