import finnhub

from app.core.config import settings


class NewsAgent:
    """
    Fetches verified company news from Finnhub.
    """

    def __init__(self):

        self.client = finnhub.Client(
            api_key=settings.FINNHUB_API_KEY
        )

    def analyze(
        self,
        symbol: str,
    ) -> dict:

        try:

            news = self.client.company_news(
                symbol.upper(),
                _from="2026-07-01",
                to="2026-07-31",
            )

            headlines = []

            sources = []

            sentiment = "Neutral"

            confidence = 70

            for article in news[:5]:

                headlines.append(
                    {
                        "headline": article.get("headline"),
                        "source": article.get("source"),
                        "url": article.get("url"),
                        "datetime": article.get("datetime"),
                    }
                )

                sources.append(
                    article.get("source")
                )

            if len(headlines) >= 3:
                confidence = 90

            return {

                "symbol": symbol.upper(),

                "sentiment": sentiment,

                "confidence": confidence,

                "headlines": headlines,

                "sources": list(set(sources)),
            }

        except Exception as e:

            return {

                "symbol": symbol.upper(),

                "sentiment": "Unknown",

                "confidence": 0,

                "headlines": [],

                "sources": [],

                "error": str(e),
            }


news_agent = NewsAgent()