@echo off
REM Cloning the repository with sparse checkout
git clone --filter=blob:none --sparse https://github.com/skills-cogrammar/C12-Lecture-Backpack.git

REM Changing directory to the cloned repository
cd C12-Lecture-Backpack

REM Adding the specific folders to sparse checkout
git sparse-checkout add "Data Science (DS)"
git sparse-checkout add "StarterPack"

@echo on
