import yfinance as yf


class MarketAgent:
    """
    Fetch live market data from Yahoo Finance.
    """

    def analyze(
        self,
        symbol: str,
    ) -> dict:

        ticker_symbol = (
            symbol
            if "." in symbol
            else f"{symbol}.NS"
        )

        ticker = yf.Ticker(ticker_symbol)

        info = ticker.info

        history = ticker.history(period="1y")

        current_price = (
            info.get("currentPrice")
            or info.get("regularMarketPrice")
            or 0
        )

        previous_close = (
            info.get("previousClose")
            or 0
        )

        if previous_close:
            change = (
                (current_price - previous_close)
                / previous_close
            ) * 100
        else:
            change = 0

        history_records = []

        if not history.empty:

            for date, row in history.iterrows():

                history_records.append(
                    {
                        "date": str(date.date()),
                        "open": float(row["Open"]),
                        "high": float(row["High"]),
                        "low": float(row["Low"]),
                        "close": float(row["Close"]),
                        "volume": int(row["Volume"]),
                    }
                )

        return {

            "symbol": symbol.upper(),

            "company_name": info.get(
                "longName",
                symbol.upper(),
            ),

            "exchange": info.get(
                "exchange",
                "NSE",
            ),

            "sector": info.get(
                "sector",
                "Unknown",
            ),

            "industry": info.get(
                "industry",
                "Unknown",
            ),

            "price": current_price,

            "previous_close": previous_close,

            "change_percent": round(change, 2),

            "open": info.get("open"),

            "day_high": info.get("dayHigh"),

            "day_low": info.get("dayLow"),

            "volume": info.get("volume"),

            "average_volume": info.get("averageVolume"),

            "market_cap": info.get("marketCap"),

            "pe_ratio": info.get("trailingPE"),

            "eps": info.get("trailingEps"),

            "beta": info.get("beta"),

            "dividend_yield": info.get("dividendYield"),

            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),

            "fifty_two_week_low": info.get("fiftyTwoWeekLow"),

            "currency": info.get("currency", "INR"),

            "history": history_records,
        }


market_agent = MarketAgent()