# Makefile

# Define the name of your git commit message
GIT_COMMIT_MSG = "13-solved(434-Number-of-Segments-in-a-String) easy!"

# Define the name of your git brach name
BRANCH_NAME = master

# Command to push a commit to the repository
push:
	git status
	sleep 2
	clear
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	echo "Running to push a commit to the repository"
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	git add .
	git commit -m $(GIT_COMMIT_MSG)
	git push origin $(BRANCH_NAME)
	git pull origin master
	git status
	sleep 2
	clear
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	echo "Done to push a commit to the repository"
	echo "Yahoo everything is working"
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	sleep 2
	clear
