import os

commands = [
    'git init',
    'git add .',
    'git commit -m "firstcommit"',
    'git branch -M main',
    'git remote add origin https://github.com/bruteforcerxx/django-http-shell-access-emulator.git',
    'git push -f origin main'
]

commands2 = [
    'git add .',
    'git commit -m "firstcommit"',
    'git push -f origin main'
]

for c in commands2:
    cmm = os.popen(c)
    cmm = cmm.read()
    print(cmm)
