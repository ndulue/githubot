#!/bin/bach

function create(){
    cd
    python create.py $1
    cd xampp/python/git/$1
    git init
    git remote add origin git@github.com:Ndulue/$1.git
    touch README.md
    git add.
    git commit -m "Initial commit"
    git push -u origin master
    code .
}