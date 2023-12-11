# Makefile

# Define the name of your git commit message
GIT_COMMIT_MSG = "23-unsolved(160-Intersection-of-Two-Linked-Lists) easy! :("
# GIT_COMMIT_MSG = "16-learning (Linkedlist: Node, append, insert, search) !"

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
	git pull origin master
	git push origin $(BRANCH_NAME)
	git status
	sleep 2
	clear
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	echo "Done to push a commit to the repository"
	echo "Yahoo everything is working"
	echo "# # # # # # # # # # # # # # # # # # # # # # # # #"
	sleep 2
	clear
