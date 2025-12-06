import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
import sys
from call_function import available_functions


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print("User prompt:", args.user_prompt)
    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )
    if not response.usage_metadata:
        raise RuntimeError("Probable failed API request")

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print("Response:")
    print(response.text)


# def generate_content(client, messages, verbose):
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         # contents=messages,
#         contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
#         # config=types.GenerateContentConfig(
#         #     tools=[available_functions], system_instruction=system_prompt
#         # ),
#     )
#
#     if not response.function_calls:
#         return response.text
#     for function_call_part in response.function_calls:
#         print(f"Calling function: {function_call_part.name}({function_call_part.args})")
#
#     # function_call_part = response.function_calls
#     # if function_call_part:
#     # print(response.function_calls)
#     # if response.function_calls != []:
#     # if response.function_calls:
#     #     for function_call_part in response.function_calls:
#     #         print(
#     #             f"Calling function: {function_call_part.name}({function_call_part.args})"
#     #         )
if __name__ == "__main__":
    main()
