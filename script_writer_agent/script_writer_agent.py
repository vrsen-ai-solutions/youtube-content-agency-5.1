from agency_swarm import Agent
import litellm
from agents import ModelSettings
from openai.types.shared import Reasoning

litellm.modify_params = True

script_writer_agent = Agent(
    name="ScriptWriter",
    description="Expert script writer for YouTube content.",
    instructions="./instructions.md",
    tools_folder="./tools",
    model="gpt-5.1",
    model_settings=ModelSettings(
        reasoning=Reasoning(
            effort="none",
        ),
    ),
)

