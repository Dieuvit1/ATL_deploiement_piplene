import json
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class NewsArticle:
    title: str
    summary: str
    event_date: Optional[str]
    publication_date: Optional[str]
    source: str
    url: str
    verification_status: str = "unverified"
    fake_news_score: Optional[float] = None

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)