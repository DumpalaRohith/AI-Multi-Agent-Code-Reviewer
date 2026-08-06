from agents.reviewer import review_code

sample_code = """
numbers = [1,2]

print(numbers[5])
"""

review = review_code(sample_code)

print(review)