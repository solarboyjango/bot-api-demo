import requests
from config import BOT_SECRET


def generate_token():
    """Step 1: Generate access token using Bot Secret"""
    print("Step 1: Generating access token...")

    url = "https://directline.botframework.com/v3/directline/tokens/generate"
    headers = {
        "Authorization": f"Bearer {BOT_SECRET}",
        "Content-Type": "application/json",
    }

    # Send request to generate token
    response = requests.post(url, headers=headers, json={})

    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        conversation_id = data.get("conversationId")

        print(f"✅ Token generated successfully!")
        print(f"   Conversation ID: {conversation_id}")
        print(f"   Token expires in: {data.get('expires_in')} seconds")

        # Save token and conversation ID for next steps
        with open("token.txt", "w") as f:
            f.write(token)
        with open("conversation_id.txt", "w") as f:
            f.write(conversation_id)

        return token, conversation_id
    else:
        print(f"❌ Failed to generate token: {response.text}")
        return None, None


if __name__ == "__main__":
    generate_token()
