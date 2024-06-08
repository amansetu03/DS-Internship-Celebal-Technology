# Define the survey results
survey_results = {
    'Baseball': {'Female': 34, 'Male': 34, 'All': 68},
    'Basketball': {'Female': 52, 'Male': 40, 'All': 92},
    'Football': {'Female': 20, 'Male': 58, 'All': 78},
    'Soccer': {'Female': 44, 'Male': 18, 'All': 62},
    'All': {'Female': 150, 'Male': 150, 'All': 300}
}

# 1. Probability that an individual is male, given that they prefer baseball
prob_male_given_baseball = survey_results['Baseball']['Male'] / survey_results['Baseball']['All']

# 2. Probability that an individual prefers basketball, given that they're female
prob_basketball_given_female = survey_results['Basketball']['Female'] / survey_results['All']['Female']

print(f"Probability that an individual is male, given that they prefer baseball --> {prob_male_given_baseball}")

print(f"\nProbability that an individual prefers basketball, given that they're female--> {prob_basketball_given_female}")
