import json
import os

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
