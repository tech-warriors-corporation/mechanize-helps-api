import re
import bleach

def sanitize(text: str) -> str:
    pattern = re.compile("["
                         u"\U0001F600-\U0001F64F"
                         u"\U0001F300-\U0001F5FF"
                         u"\U0001F680-\U0001F6FF"
                         u"\U0001F700-\U0001F77F"
                         u"\U0001F780-\U0001F7FF"
                         u"\U0001F800-\U0001F8FF"
                         u"\U0001F900-\U0001F9FF"
                         u"\U0001FA00-\U0001FA6F"
                         u"\U0001FA70-\U0001FAFF"
                         u"\U00002702-\U000027B0"
                         u"\U000024C2-\U0001F251"
                         "]+",
                         flags=re.UNICODE
    )

    text = pattern.sub(r'', text)
    text = bleach.clean(text, strip=True).replace("\n", "")

    return text.strip()
