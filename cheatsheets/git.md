#### git reset locally

`git reset --hard unico arquivo`

`git checkout HEAD -- my-file.txt`


#### delete all branchs exception main
git branch -r | grep -v "main" | xargs | sed -r 's/origin\///g' | xargs git push origin --delete