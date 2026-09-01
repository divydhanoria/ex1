# Git and GitHub Command Reference

 1. Repository setup

 `git init` — initialize a new Git repository in the current folder.
 `git clone <url>` — download a repository from GitHub or another remote.
 `git config --global user.name "Your Name"` — set your Git username.
 `git config --global user.email "you@example.com"` — set your Git email.

2. Tracking files and staging

 `git status` — show changed, staged, and untracked files.
 `git add <file>` — stage a specific file.
`git add .` — stage all tracked and new files in the current directory.
 `git restore --staged <file>` — unstage a file without discarding changes.
 `git restore <file>` — discard local edits to a file.

 3. Commit history

 `git commit -m "message"` — save staged changes with a message.
 `git log` — view commit history.
 `git log --oneline` — compact commit summary.
 `git diff` — show differences between working tree and index.
 `git diff --cached` — show staged changes.

 4. Branching

`git branch` — list branches.
 `git branch <name>` — create a new branch.
 `git checkout <name>` — switch to a branch.
 `git switch <name>` — modern branch switching command.
`git checkout -b <name>` — create and switch to a new branch.
 `git merge <branch>` — merge another branch into the current one.
 `git branch -d <name>` — delete a branch after merging.
 5. Remote repository commands

 `git remote -v` — view configured remotes.
`git remote add origin <url>` — link a repo to the origin remote.
 `git remote set-url origin <url>` — update the remote URL.
`git fetch origin` — download remote changes without merging them.
 `git pull origin <branch>` — fetch and merge the latest remote branch.
 `git push origin <branch>` — upload local commits to GitHub.
 `git push -u origin main` — set upstream tracking for the first push.

 6. GitHub-specific workflow

`gh auth login` — log in to GitHub CLI.
`gh repo create` — create a new GitHub repo from the terminal.
 `gh pr create` — create a pull request.
 `gh issue create` — create an issue.
 `gh workflow list` — list GitHub Actions workflows.

 7. Undo and recovery

 `git reset --soft HEAD~1` — undo the last commit but keep the changes staged.
 `git reset --mixed HEAD~1` — undo the last commit and unstage changes.
 `git reset --hard HEAD~1` — permanently remove the last commit and all changes.
 `git revert <commit>` — create a new commit that reverses a previous one.

 8. Tags and release workflow

 `git tag` — list tags.
 `git tag v1.0.0` — create a lightweight tag.
 `git push origin v1.0.0` — push a tag to GitHub.

 9. Common GitHub practices

 Keep commit messages clear and specific.
  Commit small logical changes.
 Use branches for features and bug fixes.
 Pull before pushing to avoid conflicts.
 Review PRs before merging.

10. Typical workflow example

```bash
git init
git add .
git commit -m "Add project files"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```
 Study tip

Use this repo as a practice project. Repeat the commands in a sandbox repository until the syntax becomes automatic.
