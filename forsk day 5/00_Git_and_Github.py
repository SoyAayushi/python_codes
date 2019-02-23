01. Why git and what git can do
02. Install git locally and Goto Github and create an account
03. Create an empty remote repo on Github with some-name
04. git clone <url> on the desktop  as local repo
05. create a test.py file on desktop/some-name and run command in the new directory
06. git add <filename>
07. git commit -m "Added new file"
08. git status whether it is nothing to commit
09. git push

10. git add --all
11. git commit -m "Adding all files"
12. git status
13. git push


10. Goto Github, edit and commit changes
11. git pull
12. Edit locally and git add test.py and git commit -m "Did some changes"
13. git push


14. Goto Github, edit and commit changes 
15. Edit locally and git add test.py and git commit -m "Did some more changes"
16. git pull
17. Merge Conflicts needs to be solved
18. Open Locally and edit, remove all <<<<<, ====== and >>>>>> and solve the error
19. git add <filename>
20. git commit -m "Fix Merge Conflict"
21. git push

22. git log ( history of commit )
23. git reset --hard <commit>   ( to have a copy of the commit number )
24. git reset --hard origin/master ( to have a fresh copy as you started )  


25. Messed working but NOT staged git checkout HEAD path/to/file
26. Messed working (but staged) git reset HEAD path/to/file and then git checkout HEAD path/to/file
27. Messed working (staged and commit)  git checkout HEAD^ path/to/file
