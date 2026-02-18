from __future__ import annotations
from dataclasses import dataclass
import requests
import httpx


OEMBED_URL = 'https://www.tiktok.com/oembed'


@dataclass
class VideoInfoV2:
    url: str
    caption: str
    comment: str
    like: str
    cover: str
    aweme_id: str
    username: str

    @classmethod
    def get_info(cls, url: str) -> VideoInfoV2:
        """Fetch video info using TikTok's official oEmbed API.

        The oEmbed endpoint is publicly accessible and not protected by
        TikTok's bot-challenge (pumbaa-rule), unlike the regular page HTML.
        """
        res = requests.get(OEMBED_URL, params={'url': url})
        res.raise_for_status()
        data = res.json()

        caption = data.get('title', '')
        username = data.get('author_unique_id', data.get('author_name', ''))
        cover = data.get('thumbnail_url', '')
        aweme_id = data.get('embed_product_id', '')
        # oEmbed does not expose like/comment counts
        like = 'N/A'
        comment = 'N/A'

        return cls(url, caption, comment, like, cover, aweme_id, username)

    @classmethod
    async def get_info_async(cls, url: str) -> VideoInfoV2:
        """Async version of get_info using TikTok's official oEmbed API."""
        async with httpx.AsyncClient() as client:
            res = await client.get(OEMBED_URL, params={'url': url})
            res.raise_for_status()
            data = res.json()

        caption = data.get('title', '')
        username = data.get('author_unique_id', data.get('author_name', ''))
        cover = data.get('thumbnail_url', '')
        aweme_id = data.get('embed_product_id', '')
        like = 'N/A'
        comment = 'N/A'

        return cls(url, caption, comment, like, cover, aweme_id, username)