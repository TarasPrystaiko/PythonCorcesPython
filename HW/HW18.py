test_designers = ["Alice", "Bob", "Charlie", "David"]
test_script_writers = ["Bob", "Charlie", "Eve", "Frank"]
script_reviewers = ["Alice", "Charlie", "Grace"]
out_of_work_today = ["David", "Eve", "Frank"]

all_testers = sorted(set(test_designers + test_script_writers + script_reviewers))

script_writers_only = sorted(set(test_script_writers) - set(test_designers + script_reviewers))

working_today = sorted(set(all_testers) - set(out_of_work_today))

write_and_review_today = sorted(set(test_script_writers) & set(script_reviewers) & set(working_today))

# Print the results
print("All testers in the team:", all_testers)
print("Testers who can only write scripts:", script_writers_only)
print("Testers who are at work today:", working_today)
print("Testers who could write and review scripts, and are at work today:", write_and_review_today)
