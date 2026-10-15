# --- Homework 1 + 2 Review ---
'''
Vocab Review
1. Git vs Github: Git is a software that tracks changes to your code, whereas GitHub is an online platform that hosts your Git repositories.
2. Terminal vs. Command Line: The terminal the window that allows to speak directly to your computer without a GUI, the command line is where 
you type in commands into the terminal.
3. Local vs. Remote Repository: A local repository is a repository stored directly on your computer, a remote repository is a repository
that is stored on a server.
4. Version Control: refers to tracking changes to your code, collaborating with other people on your code, and keeping a historical record
of your code.
5. Staging Area: The staging area is the intermediate between your local repository and a git/remote repository.
6. git add: moves your changes from your working directory into the staging area.
7. git commit: saves your changes to the local repository.
8. git push: uploads your commits to the remote repository.
9. git status: shows you the status of your git working directory and staging area.
10. git pull: pulls your changes from a remote repository into your current branch
11. pwd: prints your working directory.
12. ls: lists the directories/files in your current directory.
13. cd: allows you to change directories.
14. nano: allows you to edit files.
15. touch: allows you to create files.
16. mv: lets you move files.
17. rm: lets you remove directories.
18. cat: displays the contents of a file.
'''

'''
A Directory Tree
1) pwd
2) ls
3) cd ..
cd brianna_repo
git pull
4) mv homework.py ../judy_decal/homework/homework.py
5) cd ..
cd judy_decal
cd homework
cat homework.py
6) git add .
git commit -m "finished homework yay!"
git push origin main
7) git pull and git status help resolve the issue, Judy most likely didn't do git add, git commit, and git push in the right order
8) From the home directory:
cd Recent
'''

# --- Homework 3 Review ---
def checkDataType(x):
    print(type(x))

y = 12
checkDataType(y)
checkDataType(True)

# Conditionals
def evenOrOdd(input):
    if input % 2 == 0:
        return "Even"
    else:
        return "Odd"

a = 3
b = 4

print(evenOrOdd(a))
print(evenOrOdd(b))

# --- Loops ---
def sumWithLoop(numbers):
    value = 0
    for i in numbers:
        value += i
    return value

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# --- Homework 4 Review ---

def duplicateList(lst1):
    newList= []
    for i in lst1:
        newList.append(i)
        newList.append(i)
    return newList

lst1 = [5, 6, 7, 8]
print(duplicateList(lst1))


# Debugging
def square(num):
    return num ** 2

print(square(3))

# Fav Function
print(duplicateList(lst1))

