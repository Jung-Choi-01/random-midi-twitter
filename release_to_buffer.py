import argparse
import requests
from hashlib import sha256


def main(api_token: str, channel_id: str, post_time: str, media_url: str, text: str) -> None:
    url = "https://api.buffer.com"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
    }

    payload = {
        "query": """
mutation CreatePost($channelId: ChannelId!, $postTime: DateTime, $url: String!, $text: String!) {
    createPost(input: {
        text: $text,
        channelId: $channelId,
        schedulingType: automatic,
        mode: customScheduled,
        dueAt: $postTime,
        assets: {
        videos:[
            {
            url: $url
            }
        ]
        }
    }) {
        ... on PostActionSuccess {
        post {
            id
            text
            assets {
            id
            mimeType
            }
        }
        }
        ... on MutationError {
        message
        }
    }
}
            """,
        "variables": {
            "channelId": channel_id,
            "postTime": post_time,
            "url": media_url,
            "text": text,
        },
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post a scheduled Buffer video update")
    parser.add_argument("api_token", help="Buffer API token")
    parser.add_argument("channel_id", help="Buffer channel id")
    parser.add_argument("post_time", help="Scheduled post time in ISO 8601 format")
    parser.add_argument("media_url", help="URL of video asset")
    parser.add_argument("text", help="Plaintext string for post text")
    
    args = parser.parse_args()
    main(args.api_token.strip(), args.channel_id.strip(), args.post_time.strip(), args.media_url.strip(), args.text.strip())