import os
import random

subjects = {}

class Subject:
	def __init__(self, folder_path):
		self.name = folder_path.split("/")[-1]
		self.complete_file = "~/rendu/" + self.name + ".c"
		self.subject_file = "~/subject/" + self.name + ".txt"
		self.subject = open(folder_path + "/subject.txt", "r").read()
		self.main = open(folder_path + "/main.c", "r").read()
		self.function = open(folder_path + "/function.c", "r").read()

	def to_dict(self):
		return {
			"name": self.name,
			"subject": self.subject,
			"complete_file": self.complete_file,
			"subject_file": self.subject_file
		}

def load_subjects():
	global subjects

	if os.path.isdir("subjects") == False:
		print("Error: no subjects folder found")
		exit(1)
	
	for folder in os.listdir("subjects"):
		if folder.startswith("level"):
			level = int(folder[5:-1])
			subjects[level] = []
			for subject in os.listdir("subjects/" + folder):
				subjects[level].append(Subject("subjects/" + folder + "/" + subject))
				print("Loaded subject " + subject + " for level " + str(level))

def is_subject_for_level(level):
	return level in subjects.keys()

def get_subject_for_level(level):
	return subjects[level][random.randint(0, len(subjects[level]) - 1)]