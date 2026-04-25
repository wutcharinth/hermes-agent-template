# Skill: Code & Data Engineering

## When to use
Any request involving: code, scripts, automation, data pipelines, SQL, APIs, debugging, architecture, review.

## Approach
1. Write complete, runnable code — never pseudocode unless asked
2. Default languages: Python (data/automation), SQL (analytics), Bash (scripting)
3. For data tasks: use pandas, polars, or SQL depending on scale
4. For APIs: use httpx or requests, always handle errors
5. For automation: prefer simple scripts over heavy frameworks
6. Always include example usage or test cases

## Oui's Stack Context (Agoda FinTech)
- Data warehouse: likely BigQuery or similar cloud DW
- Orchestration: Airflow / n8n style workflows
- AI/ML: Python-first, familiar with LLM APIs and agent frameworks
- Write production-quality code with proper error handling
- Prefer readability over cleverness

## Output Format
- Code in proper fenced blocks with language tag
- Brief explanation of what it does and how to run it
- Highlight any dependencies to install
- For complex systems: include a simple architecture note

## Examples Oui might ask
- "Write a Python script to pull data from X API and load to BigQuery"
- "Review this SQL query for performance"
- "Build an n8n workflow for Y"
- "Debug this Python error: ..."
- "Write a data pipeline for Z"
