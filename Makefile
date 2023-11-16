# Makefile

# Define the name of your git commit message
GIT_COMMIT_MSG = "10-solved(217-Contains-Duplicate problem) easy!"

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
	git push origin master
	git status
	sleep 2
	clear
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	echo "Done to push a commit to the repository"
	echo "Yahoo everything is working"
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	sleep 2
	clear
