# Makefile for creating a folder with contents based on the day number

# Usage: make day=<day_number>

# Extract the day number from the command line
DAY_NUMBER := $(or $(day), 1)

# Define folder and file names
FOLDER_NAME := day$(DAY_NUMBER)
TEST_FILE := $(FOLDER_NAME)/test.txt
INPUT_FILE := $(FOLDER_NAME)/input.txt
PY_FILE := $(FOLDER_NAME)/d$(DAY_NUMBER).py

# Default target
all: create_folder

# Target to create the folder and files
create_folder:
	mkdir -p $(FOLDER_NAME)
	touch $(TEST_FILE)
	touch $(INPUT_FILE)
	touch $(PY_FILE)

# Target to clean up created files and folder
clean:
	rm -rf $(FOLDER_NAME)

.PHONY: all create_folder clean

