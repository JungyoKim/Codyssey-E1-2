PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git add .
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git commit -m ""
                                         omp -r^C        
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> ^C
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git commit -m "초기화"       
[main (root-commit) 8954771] 초기화
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 .gitignore
 create mode 100644 README.md
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git branch -M main
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git remote add origin git@git@github.com:JungyoKim/Codyssey-E1-2.git
error: remote origin already exists.
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 236 bytes | 236.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/JungyoKim/Codyssey-E1-2
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 


PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git add .
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git commit -m "Quiz 클래스 추가"
[main 17b8e85] Quiz 클래스 추가
 2 files changed, 23 insertions(+)
 create mode 100644 main.py
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 796 bytes | 796.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/JungyoKim/Codyssey-E1-2
   8954771..17b8e85  main -> main
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 

PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git add .      
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git commit -m "기본 퀴즈 데이터 추가"
[main 195076f] 기본 퀴즈 데이터 추가
 3 files changed, 68 insertions(+)
 create mode 100644 state.json
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.28 KiB | 1.28 MiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/JungyoKim/Codyssey-E1-2
   17b8e85..195076f  main -> main
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 

PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> python main.py

퀴즈를 시작합니다. (총 5문제)
----------------------------------------

[문제 1] 다음 중 Python에서 변수 이름(식별자)으로 사용할 수 없는 것은?
  1. my_var
  2. user2
  3. for
  4. _score
정답 번호를 입력하세요: 3
정답입니다.

[문제 2] 다음 중 Python에서 한 줄 주석을 작성할 때 사용하는 기호는?
  1. //
  2. #
  3. /*
  4. --
정답 번호를 입력하세요: 2
정답입니다.

[문제 3] 다음 중 Python에서 리스트의 맨 뒤에 새 요소를 추가할 때 사용하는 메서드는?
  1. add()
  2. append()
  3. push()
  4. insert()
정답 번호를 입력하세요: 2
정답입니다.

[문제 4] 다음 중 Python 조건문에서 사용하는 키워드로 올바른 것은?
  1. else if
  2. elseif
  3. elif
  4. then
정답 번호를 입력하세요: 3
정답입니다.

[문제 5] 다음 중 Python에서 문자를 출력할 때 사용하는 기본 내장 함수는?
  1. console.log()
  2. print()
  3. printf()
  4. System.out.println()
정답 번호를 입력하세요: 2
정답입니다.
결과: 5문제 중 5문제 정답.
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> python main.py

퀴즈를 시작합니다. (총 5문제)
----------------------------------------

[문제 1] 다음 중 Python에서 변수 이름(식별자)으로 사용할 수 없는 것은?
  1. my_var
  2. user2
  3. for
  4. _score
정답 번호를 입력하세요:  
빈 입력입니다. 다시 입력해주세요.
정답 번호를 입력하세요:  
빈 입력입니다. 다시 입력해주세요.
정답 번호를 입력하세요:  
빈 입력입니다. 다시 입력해주세요.
정답 번호를 입력하세요:  
빈 입력입니다. 다시 입력해주세요.
정답 번호를 입력하세요:  
빈 입력입니다. 다시 입력해주세요.
정답 번호를 입력하세요: ㅇㄹㄴㅇㄹ
유효하지 않은 입력입니다. 정수를 입력해주세요.
정답 번호를 입력하세요: 1q2
유효하지 않은 입력입니다. 정수를 입력해주세요.
정답 번호를 입력하세요: 12
입력 값은 1에서 4 사이의 정수여야 합니다.
정답 번호를 입력하세요: 12
입력 값은 1에서 4 사이의 정수여야 합니다.
정답 번호를 입력하세요: "1"
유효하지 않은 입력입니다. 정수를 입력해주세요.
정답 번호를 입력하세요: "1"1
유효하지 않은 입력입니다. 정수를 입력해주세요.
정답 번호를 입력하세요: 1
오답입니다. 정답은 '3'입니다.

[문제 2] 다음 중 Python에서 한 줄 주석을 작성할 때 사용하는 기호는?
  1. //
  2. #
  3. /*
  4. --
정답 번호를 입력하세요: ^ZTraceback (most recent call last):
  File "C:\Users\kimjungyo\Dev\Codyssey-E1-2\main.py", line 102, in <module>
    manager.play()
  File "C:\Users\kimjungyo\Dev\Codyssey-E1-2\main.py", line 90, in play
    user_answer = self.get_valid_input("정답 번호를 입력하세요: ", 1, len(quiz.choices))
  File "C:\Users\kimjungyo\Dev\Codyssey-E1-2\main.py", line 66, in get_valid_input
    raw_input = input(prompt).strip()
KeyboardInterrupt
^CTerminate batch job (Y/N)? 
^C
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> python main.py
퀴즈가 없습니다.
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> python main.py
퀴즈가 없습니다.
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> python main.py

퀴즈를 시작합니다. (총 5문제)
----------------------------------------

[문제 1] 다음 중 Python에서 변수 이름(식별자)으로 사용할 수 없는 것은?
  1. my_var
  2. user2
  3. for
  4. _score
정답 번호를 입력하세요: Traceback (most recent call last):
  File "C:\Users\kimjungyo\Dev\Codyssey-E1-2\main.py", line 102, in <module>
    manager.play()
  File "C:\Users\kimjungyo\Dev\Codyssey-E1-2\main.py", line 90, in play
    user_answer = self.get_valid_input("정답 번호를 입력하세요: ", 1, len(quiz.choices))
  File "C:\Users\kimjungyo\Dev\Codyssey-E1-2\main.py", line 66, in get_valid_input
    raw_input = input(prompt).strip()
KeyboardInterrupt
^CTerminate batch job (Y/N)? 
^C
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> ^C
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> ^C
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> ^C
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> ^C
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git add . 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git commit -m "퀴즈 풀기 기능 및 예외 처리 구현" 
[quizmanager ff03b2c] 퀴즈 풀기 기능 및 예외 처리 구현
 2 files changed, 68 insertions(+)
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git branch
* main
  quizmanager
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git push origin branch
error: src refspec branch does not match any
error: failed to push some refs to 'https://github.com/JungyoKim/Codyssey-E1-2'
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git push origin quizmanager
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.96 KiB | 1.96 MiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'quizmanager' on GitHub by visiting:
remote:      https://github.com/JungyoKim/Codyssey-E1-2/pull/new/quizmanager
remote: 
To https://github.com/JungyoKim/Codyssey-E1-2
 * [new branch]      quizmanager -> quizmanager
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> git merge quizmanager      
Updating 195076f..ff03b2c
Fast-forward
 README.md | 17 +++++++++++++++++
 main.py   | 51 +++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 68 insertions(+)
PS C:\Users\kimjungyo\Dev\Codyssey-E1-2> 