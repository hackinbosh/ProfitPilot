import faiss
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.tools.human.tool import HumanInputRun
from langchain.vectorstores import FAISS
from langchain_experimental.autonomous_agents import AutoGPT

from profit.llama2 import LLama2
from profit.tools import (
    ReadFileTool,
    WriteFileTool,
    draft_email,
    process_csv,
    query_website_tool,
    scrape_data,
    zapier_tools,
)

ROOT_DIR = "./data/"

class Agent:
    def __init__(self, 
                 ai_name="Autobot Swarm Worker",
                 ai_role="Worker in a swarm",
                 external_tools = None,
                 human_in_the_loop=False,
                 ):
        self.human_in_the_loop = human_in_the_loop
        self.ai_name = ai_name
        self.ai_role = ai_role
        self.llama = LLama2()

        self.setup_tools(external_tools)
        self.setup_memory()
        self.setup_agent()

    def setup_tools(self, external_tools):
        self.tools = [


class Agent:
    def __init__(self, ...):
        ...
        self.salesforce_username = "your_username"
        self.salesforce_password = "your_password"
        self.salesforce_security_token = "your_security_token"

    def fetch_customers(self):
        return get_salesforce_customers(self.salesforce_username, self.salesforce_password, self.salesforce_security_token)

    def track_prospect(self, prospect_data):
        track_prospect_in_salesforce(self.salesforce_username, self.salesforce_password, self.salesforce_security_token, prospect_data)

            WriteFileTool(root_dir=ROOT_DIR),
            ReadFileTool(root_dir=ROOT_DIR),
            process_csv,

            query_website_tool,
            HumanInputRun(),
            zapier_tools,
            draft_email,
            scrape_data
        ]
        if external_tools is not None:
            self.tools.extend(external_tools)

    def setup_memory(self):
        try:
            embeddings_model = OpenAIEmbeddings()
            embedding_size = 1536
            index = faiss.IndexFlatL2(embedding_size)
            self.vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
        except Exception as error:
            raise RuntimeError(f"Error setting up memory. Maybe try tuning the embedding size: {error}")

    def setup_agent(self):
        try: 
            self.agent = AutoGPT.from_llm_and_tools(
                ai_name=self.ai_name,
                ai_role=self.ai_role,
                tools=self.tools,
                llm=self.llama,
                memory=self.vectorstore.as_retriever(search_kwargs={"k": 8}),
                human_in_the_loop=self.human_in_the_loop
            )
        
        except Exception as error:
            raise RuntimeError(f"Error setting up agent: {error}")

    def run(self, task):
        try:
            result = self.agent.run([task])
            return result
        except Exception as error:
            raise RuntimeError(f"Error while running agent: {error}")

    def __call__(self, task):
        return self.run(task)
