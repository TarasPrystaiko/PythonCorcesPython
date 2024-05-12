# Define lists of testers for each group
test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

# All testers in the team
all_testers = sorted(set(test_design_writers + test_scripters + reviewers))

# Testers who can only write scripts
scripters_only = sorted(set(test_scripters) - set(test_design_writers) - set(reviewers))

# Testers who are at work today
working_today = sorted(set(all_testers) - set(out_of_office_today))

# Testers who could write and review scripts, and are at work today
write_and_review_today = sorted(set(test_scripters) & set(reviewers) & set(working_today))

# Print the results
print("All testers in the team:")
print(all_testers)
print("\nTesters who can only write scripts:")
print(scripters_only)
print("\nTesters who are at work today:")
print(working_today)
print("\nTesters who could write and review scripts, and are at work today:")
print(write_and_review_today)
