# 确认当前目录
pwd

# 检查工作区状态
git status

# 如果工作区是干净的，创建一个新的提交
echo "Initial commit" > README.md
git add README.md
git commit -m "Initial commit"

# 创建新的分支
git checkout -b basic-python