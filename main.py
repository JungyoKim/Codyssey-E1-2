from src.constants import MENU_TEXT
from src.game import QuizGame, get_valid_input


def main():
    """메뉴를 반복 출력하며 사용자가 선택한 기능을 실행하고, 종료 시(또는 Ctrl+C/EOF 발생 시) 저장 후 안전하게 마친다."""
    manager = QuizGame()

    while True:
        try:
            print(MENU_TEXT)
            choice = get_valid_input("선택: ", 1, 7)

            if choice == 1:
                manager.play()
            elif choice == 2:
                manager.add_quiz()
            elif choice == 3:
                manager.show_quiz_list()
            elif choice == 4:
                manager.show_best_score()
            elif choice == 5:
                manager.delete_quiz()
            elif choice == 6:
                manager.show_history()
            elif choice == 7:
                print("\n프로그램을 종료합니다.")
                break
        except (KeyboardInterrupt, EOFError):
            print("\n\n입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
            break

    manager.save_state()


if __name__ == "__main__":
    main()