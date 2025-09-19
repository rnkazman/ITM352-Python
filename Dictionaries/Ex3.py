# Define a list of survey response values
survey_responses = [5, 7, 3, 8]

# Define a tuple of respondent ID values
respondent_ids = (1012, 1035, 1021, 1053)

# Create a Dictionary with ID values as the keys and survey responses as the values using zip()
survey_dict = dict(zip(respondent_ids, survey_responses))

# Print the results
print("Survey response values:", survey_responses)
print("Respondent ID values:", respondent_ids)
print("Survey dictionary:", survey_dict)

# Demonstrate accessing individual responses
print(f"\nRespondent {respondent_ids[0]} gave a response of {survey_dict[respondent_ids[0]]}")
print(f"Respondent {respondent_ids[2]} gave a response of {survey_dict[respondent_ids[2]]}")
