import requests
import json
import re

def get_bible_scripture(task_content: str) -> str:
    try:
        prompt = (
            f"Given the task '{task_content}', provide exactly one relevant Bible scripture, "
            f"including only the verse text and its reference in the format: "
            f"\"<verse text> - <book chapter:verse>\". "
            f"For example: \"Trust in the Lord with all your heart and lean not on your own understanding; "
            f"in all your ways submit to him, and he will make your paths straight. - Proverbs 3:5-6\". "
            f"Do not include any additional text, such as 'Scripture: ' or explanations."
        )
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()
        scripture = result.get("response", "No scripture found")
        
        return scripture
    except Exception as e:
        return f"Error fetching scripture: {str(e)}"