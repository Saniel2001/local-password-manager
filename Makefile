# Makefile to run git add, commit, and push

# Define a default target
.PHONY: push

# Run the git_push.sh script with a commit message argument
push:
	@if [ -z "$(msg)" ]; then \
		echo "Error: Please provide a commit message using 'make push msg=\"Your message\"'"; \
		exit 1; \
	fi
	./git-push.sh "$(msg)"
