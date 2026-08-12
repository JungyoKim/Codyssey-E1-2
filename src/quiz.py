class Quiz:
    """개별 퀴즈 1개(문제, 선택지, 정답, 힌트)를 표현하는 클래스."""
    def __init__(self, question: str, choices: list[str], answer: int, hint: str = ""):
        """퀴즈를 초기화한다: 문제, 선택지 목록, 정답 번호, 힌트를 저장한다."""
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def is_correct(self, user_answer: int) -> bool:
        """입력한 답이 정답 번호와 일치하는지 확인한다."""
        return self.answer == user_answer

    def display(self, index: int):
        """문제와 선택지를 번호(1부터)와 함께 화면에 출력한다."""
        print(f"\n[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def to_dict(self) -> dict:
        """퀴즈를 state.json에 저장할 수 있도록 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }
