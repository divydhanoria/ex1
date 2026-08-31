# GitHub Command Learning Repo

This project is designed to help you learn Git and GitHub commands through a guided practice workflow and an interactive quiz.

## What is included

- A quick-start command cheat sheet
- An interactive Python learning program
- A simple Git workflow to practice local and remote commands

## Project structure

- `learn_github.py` — interactive learning and command quiz
- `COMMANDS.md` — the main command reference
- `.gitignore` — common files to ignore

## How to use

Run the program:

```bash
python3 learn_github.py
```

Then study the command list in `COMMANDS.md` and practice each one in a sandbox repository.

## Recommended learning flow

1. Read the command reference.
2. Run the quiz.
3. Practice using Git locally.
4. Create a GitHub repository.
5. Push your local repo with `git push origin main`.

## Core GitHub workflow

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

## Important note

This repo is ready to be pushed to your own GitHub account. You must replace the example remote URL with your actual repository URL and authenticate with GitHub before pushing.
