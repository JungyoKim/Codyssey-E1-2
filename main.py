import json
import os
import sys

STATE_FILE = "state.json"

DEFAULT_QUIZZES = [
    {
        "question": "다음 중 Python에서 변수 이름(식별자)으로 사용할 수 없는 것은?",
        "choices": ["my_var", "user2", "for", "_score"],
        "answer": 3
    },
    {
        "question": "다음 중 Python에서 한 줄 주석을 작성할 때 사용하는 기호는?",
        "choices": ["//", "#", "/*", "--"],
        "answer": 2
    },
    {
        "question": "다음 중 Python에서 리스트의 맨 뒤에 새 요소를 추가할 때 사용하는 메서드는?",
        "choices": ["add()", "append()", "push()", "insert()"],
        "answer": 2
    },
    {
        "question": "다음 중 Python 조건문에서 사용하는 키워드로 올바른 것은?",
        "choices": ["else if", "elseif", "elif", "then"],
        "answer": 3
    },
    {
        "question": "다음 중 Python에서 문자를 출력할 때 사용하는 기본 내장 함수는?",
        "choices": ["console.log()", "print()", "printf()", "System.out.println()"],
        "answer": 2
    }
]

class Quiz:
    def __init__(self, question:str, choices:list[str], answer:int):
        self.question = question
        self.choices = choices
        self.answer = answer

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
            "answer": self.answer
        }

class QuizManager:
    def __init__(self):
        self.quizzes = []
        for q in DEFAULT_QUIZZES:
            self.quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))
        self.best_score = 0

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

        print(f"\n퀴즈를 시작합니다. (총 {len(self.quizzes)}문제)")
        print("-" * 40)

        score = 0

        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            user_answer = self.get_valid_input("정답 번호를 입력하세요: ", 1, len(quiz.choices))
            if quiz.is_correct(user_answer):
                print("정답입니다.")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번 입니다.")

        total = len(self.quizzes)
        print(f"결과: {total}문제 중 {score}문제 정답.")

if __name__ == "__main__":
    manager = QuizManager()
    manager.play()