from langchain_groq import ChatGroq
import re

from config import (
    LLM_MODEL,
    TEMPERATURE
)

# ==========================================================
# LLM
# ==========================================================

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=TEMPERATURE
)

# ==========================================================
# CLEANER
# ==========================================================


def clean_response(text: str) -> str:

    # Remove marcações Markdown inválidas
    text = re.sub(r"\*+", "", text)

    # Remove linhas em branco excessivas
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove espaços duplicados
    text = re.sub(r" {2,}", " ", text)

    return text
# ==========================================================
# BUSINESS ANALYST
# ==========================================================

def analyze_result(question, result):

    prompt = f"""
You are a Senior Business Intelligence Consultant.

Your mission is to transform business data into strategic insights for executives.

The user's question has already been validated as a legitimate Business Intelligence request related to the uploaded dataset.

Your responsibility is to interpret the execution result and provide executive-level insights.

Use ONLY the provided execution result.

Never invent numbers.

Never fabricate information.

If information is unavailable, explicitly state what data is missing.

Focus on actionable business insights rather than merely describing the data..


====================================================================
WRITING STYLE
====================================================================

Write as if presenting to a company's executive board.

Be concise, professional and objective.

Prefer short paragraphs.

Use bullet points whenever appropriate.

Avoid repetition.

Focus on decision making rather than describing the data.

Formatting Rules

Formatting Rules

- Return clean Markdown only.
- Use headings and bullet lists.
- Do not use italic text.
- Never print the response with "**" caracter
- Always close Markdown formatting symbols properly.

====================================================================
ANALYSIS GUIDELINES
====================================================================

Whenever possible:

- quantify observations
- compare values
- identify rankings
- identify trends
- identify concentration
- identify opportunities
- identify business risks
- mention limitations of the available data

====================================================================
USER QUESTION
====================================================================

{question}

====================================================================
EXECUTION RESULT
====================================================================

{result}

====================================================================
RESPONSE FORMAT
====================================================================

# Executive Summary

The company generated **$2.37M** during the first four months of 2026.

--------------------------------------------------

# Key Findings

- Revenue peaked in April 2026 ($681.6K).
- February recorded the lowest revenue ($493.8K).
- The difference between the highest and lowest months was approximately 31%

--------------------------------------------------

# Business Impact

Explain what these findings mean for the business.

--------------------------------------------------

# Risks

Identify possible risks based only on the available data.

If no risks can be inferred, explicitly state that.

--------------------------------------------------

# Recommendations

Provide practical recommendations that management could implement.

--------------------------------------------------

# Additional Data That Would Improve The Analysis

List the missing information that would allow a deeper analysis.

"""


    response = llm.invoke(prompt)

    analysis = clean_response(response.content)



    return analysis

