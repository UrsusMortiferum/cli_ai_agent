import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
import sys
from prompts import system_prompt
from call_function import available_functions


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.prompt,
    )
    if not response.usage_metadata:
        raise RuntimeError("Probable failed API request")

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


#
#     verbose = "--verbose" in sys.argv
#     args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
#
#     args = sys.argv[1:]
#
#     # if "verbose" in args[:1]:
#     #     args = args[:-1]
#     # if not args:
#     #     print("AI Code Assistant")
#     #     print('\nUsage: python main.py "your prompt here"')
#     #     print('Example: python main.py "Why are episodes 7-9 so much worse than 1-6"')
#     #     sys.exit(1)
#
#     user_prompt = " ".join(args)
#
#     if verbose:
#         print(f"User prompt: {user_prompt}")
#
#     messages = [
#         types.Content(role="user", parts=[types.Part(text=user_prompt)]),
#     ]
#
#     generate_content(client, messages, verbose)
#
#
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
#     print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#     print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
#     print("Response:")
#     print(response.text)
#
#     if not response.usage_metadata:
#         raise RuntimeError("Probable failed API request")
#     if verbose:
#         print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#         print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
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
#
#     print(response.text)
#
#
if __name__ == "__main__":
    main()
