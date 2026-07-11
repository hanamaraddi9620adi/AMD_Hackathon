import re


class QueryUnderstandingAgent:
    """
    Understands the user's query and extracts
    stock symbols and intent.
    """

    BUY_KEYWORDS = [
        "buy",
        "purchase",
        "invest",
        "enter",
    ]

    SELL_KEYWORDS = [
        "sell",
        "exit",
        "book profit",
    ]

    ANALYZE_KEYWORDS = [
        "analyze",
        "analysis",
        "review",
        "check",
    ]

    def understand(self, query: str):

        query_lower = query.lower()

        intent = "general"

        if any(word in query_lower for word in self.BUY_KEYWORDS):
            intent = "buy"

        elif any(word in query_lower for word in self.SELL_KEYWORDS):
            intent = "sell"

        elif any(word in query_lower for word in self.ANALYZE_KEYWORDS):
            intent = "analyze"

        symbol = self.extract_symbol(query)

        return {
            "query": query,
            "intent": intent,
            "symbol": symbol,
        }

    def extract_symbol(self, query: str):

        words = re.findall(r"[A-Za-z]+", query)

        ignore = {
            "can",
            "i",
            "buy",
            "sell",
            "should",
            "analyze",
            "analysis",
            "today",
            "tomorrow",
            "stock",
            "share",
            "of",
            "the",
            "is",
            "my",
            "please",
            "review",
            "check",
        }

        for word in words:
            if word.lower() not in ignore:
                return word.upper()

        return None


query_understanding_agent = QueryUnderstandingAgent()