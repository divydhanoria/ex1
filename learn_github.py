#!/usr/bin/env python3
"""Interactive Git and GitHub command trainer."""

from __future__ import annotations

QUIZ = [
    {
        "question": "What command initializes a new Git repository in the current folder?",
        "answer": "git init",
    },
    {
        "question": "What command shows the status of your repository?",
        "answer": "git status",
    },
    {
        "question": "What command stages all changes in the working directory?",
        "answer": "git add .",
    },
    {
        "question": "What command creates a snapshot of staged changes with a message?",
        "answer": "git commit -m \"message\"",
    },
    {
        "question": "What command creates a connection to a remote repository named origin?",
        "answer": "git remote add origin <url>",
    },
    {
        "question": "What command uploads local commits to GitHub?",
        "answer": "git push origin <branch>",
    },
    {
        "question": "What command downloads changes from a remote branch without merging?",
        "answer": "git fetch origin",
    },
    {
        "question": "What command creates a new branch?",
        "answer": "git branch <name>",
    },
    {
        "question": "What command switches to another branch?",
        "answer": "git switch <name>",
    },
    {
        "question": "What command merges another branch into the current branch?",
        "answer": "git merge <branch>",
    },
]

COMMAND_CARDS = {
    "Setup": [
        "git init",
        "git clone <url>",
        "git config --global user.name \"Your Name\"",
        "git config --global user.email \"you@example.com\"",
    ],
    "Stage and Commit": [
        "git status",
        "git add <file>",
        "git add .",
        "git commit -m \"message\"",
    ],
    "Branching": [
        "git branch",
        "git branch <name>",
        "git switch <name>",
        "git merge <branch>",
    ],
    "Remote and GitHub": [
        "git remote -v",
        "git remote add origin <url>",
        "git push origin main",
        "git pull origin main",
        "gh auth login",
        "gh pr create",
    ],
    "Recovery": [
        "git restore <file>",
        "git reset --hard HEAD~1",
        "git revert <commit>",
    ],
}


def print_title():
    print("\n=== GitHub Command Learning Lab ===")
    print("Learn the most important Git and GitHub commands by repetition and practice.\n")


def show_command_cards():
    for category, commands in COMMAND_CARDS.items():
        print(f"{category}:")
        for command in commands:
            print(f"  - {command}")
        print()


def run_quiz():
    score = 0
    print("=== Quick Quiz ===")
    for index, item in enumerate(QUIZ, start=1):
        user_answer = input(f"{index}. {item['question']}\nYour answer: ").strip()
        if user_answer.lower() == item["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct command is: {item['answer']}\n")

    print(f"Your score: {score}/{len(QUIZ)}")
    if score == len(QUIZ):
        print("Excellent! You know the basics well.")
    elif score >= len(QUIZ) * 0.7:
        print("Very good. Review the missed commands and try again.")
    else:
        print("Keep practicing. Repeat the quiz until the commands become automatic.")


def main():
    print_title()
    show_command_cards()
    run_quiz()

    print("\nSuggested practice workflow:")
    print("1. git init")
    print("2. git add .")
    print("3. git commit -m \"Add project files\"")
    print("4. git branch -M main")
    print("5. git remote add origin <your-github-url>")
    print("6. git push -u origin main")
    print("\nTip: use GitHub Desktop or the GitHub website to visualize the workflow.")


if __name__ == "__main__":
    main()
