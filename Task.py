from crewai import Task
from Tool_setup import internet_search
from Agent import researcher,News

research_task = Task(
  description=(
    "Analyze the emerging trend in {topic}, focusing on patterns and industry shifts. "
    "Highlight its significance, advantages, drawbacks, market and opportunities."
  ),
  expected_output=(
    "A concise **3-paragraph** report summarizing key insights, opportunities,try to the websit link, and challenges in {topic}."
  ),
  tools=[internet_search],
  agent=researcher
)



write_task = Task(
    description=(
        "Write an engaging article on **{topic}**, covering the latest trends, key developments, and their industry impact. "
        "Ensure the content is insightful, positive, and easy to understand, with relevant examples and expert insights."
    ),
    expected_output=(
        "A **3-paragraph** article on **{topic} advancements**, in Markdown, with clear sections."
    ),
    tools=[internet_search],
    agent=News,
    async_execution=False,
    output_file="new-blog-post.md"
)

