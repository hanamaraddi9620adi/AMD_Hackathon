from openai import OpenAI

from app.core.config import settings


class FireworksService:
    """
    Fireworks AI Service
    Generates the final executive summary.
    """

    def __init__(self):

        self.client = OpenAI(

            api_key=settings.FIREWORKS_API_KEY,

            base_url="https://api.fireworks.ai/inference/v1",
        )

    def generate_summary(
        self,
        symbol: str,
        market: dict,
        technical: dict,
        fundamentals: dict,
        news: dict,
        risk: dict,
    ) -> str:

        prompt = f"""
You are a Senior Equity Research Analyst.

Analyze the following stock.

Stock:
{symbol}

Market Data:
{market}

Technical Analysis:
{technical}

Fundamental Analysis:
{fundamentals}

Latest News:
{news}

Risk Analysis:
{risk}

Rules:

1. Never recommend BUY or SELL.

2. Never hallucinate.

3. Mention uncertainty.

4. Explain WHY.

5. Mention risks.

6. Mention opportunities.

Return a professional executive summary.
"""

        response = self.client.chat.completions.create(

            model="accounts/fireworks/models/glm-5p2",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional financial research analyst.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],

            temperature=0.2,

            max_tokens=700,
        )

        return response.choices[0].message.content


fireworks_service = FireworksService()