'''Test module for Task 2'''
import cat

WRONG_PATH = "non-existent-file.txt"
TEST_PATH = ["storage/task-02-test-01.txt",
             "storage/task-02-test-02.txt",
             "storage/task-02-test-03.txt"
            ]

for cats_file in TEST_PATH:
    print(cat.get_cats_info(cats_file),"\n")

# cat.get_cats_info(WRONG_PATH)
