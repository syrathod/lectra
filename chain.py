from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser

class chain:
    def summarize(datetime, log_file):
        llm = OllamaLLM(model = "gemma2:9b")
        output_parser = StrOutputParser()

        prompt = PromptTemplate.from_template(
            """
            You are an AI assistant. You will be receiving an online lecture audio transcript as an input and your job is to summarize it in a concise yet comprehensive manner for the students' ease of understanding and future reference. Format the output in a point-wise manner while highlighting different sub topics covered in the lecture.
            Transcript: {input}
            """
        )

        with open(log_file.name, "r") as input_file:
            input = input_file.readlines()
            # print(f"Input: {input}")

        # print(input)

        chain = prompt | llm | output_parser

        output = ""

        for chunk in chain.stream(input):
            print(chunk, end="", flush=True)
            output += chunk

        output_file = f"./milestones/output_{datetime}"
        with open(f"{output_file}.txt", "w+") as output_file:
            output_file.write(output)
        
        print("\n\n[+] Notes saved to this pc.")

