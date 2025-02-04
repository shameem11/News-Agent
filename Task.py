from crewai import Task
from Tool_setup import internet_search
from Agent import researcher,News

research_task = Task(
  description=(
    "Conduct an in-depth analysis to identify the next big trend in {topic}. "
    "Your research should focus on emerging patterns, technological breakthroughs, and industry shifts. "
    "Ensure your findings cover: "
    "- The significance of this trend and why it is gaining attention. "
    "- Key advantages and potential drawbacks associated with it. "
    "- The market opportunities it presents, including industries and stakeholders that may benefit. "
    "- Possible risks, ethical concerns, or regulatory challenges. "
    "Your final report should be well-structured, providing a balanced perspective on the trend."
  ),
  expected_output=(
    "A well-structured, **3-paragraph** report summarizing the latest trends in {topic}. "
    "Each paragraph should highlight key insights, opportunities, and challenges."
  ),
  tools=[internet_search],
  agent=researcher
)



write_task = Task(
    description=(
        "Write a well-researched, engaging article on **{topic}**. "
        "Highlight the **latest trends**, key developments, and their impact on the industry. "
        "Ensure the article is **insightful, easy to understand, and maintains a positive tone**. "
        "Use compelling storytelling, expert insights, and relevant examples to keep readers engaged."
    ),
    expected_output=(
        "A **3-paragraph** article on **{topic} advancements**, formatted in Markdown, "
        "with clear sections and engaging content."
    ),
    tools=[internet_search],
    agent=News,
    async_execution=False,
    output_file="new-blog-post.md"  # Ensures structured output storage
)
