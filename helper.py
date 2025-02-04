import openai
import json
import pandas as pd

openai.api_key = "my API key"


def extract_financial_data(text):
    prompt = get_prompt_financial() + text
    response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  store=True,
                  messages=[
                    {"role": "user", "content": prompt}
                  ]
                )
    content = response.choices[0].message["content"]  # Fixed attribute access

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(), columns=["Measure", "Value"])
    except (json.decoder.JSONDecodeError, KeyError):
        pass

    return pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })

def get_prompt_financial():
    return '''Please retrieve company name, revenue, net income, and earnings per share (EPS)
    from the following news article. If you can't find the information, return an empty string.
    Then retrieve a stock symbol for that company (using your general knowledge if needed).
    Always return your response as a valid JSON string in this format:

    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }

    News Article:
    ============
    '''

if __name__ == "__main__":
    text = '''
    Tesla's Earning news in text format: Tesla's earnings this quarter blew all the estimates. 
    They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 
    '''

    df = extract_financial_data(text)
    print(df)
