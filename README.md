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