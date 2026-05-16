import json


def get_system_prompt():

    with open("figma_nodes.json", "r") as f:
        figma_data = json.load(f)

        # nodes = figma_data["nodes"]
        # layer_names = [node["name"] for node in nodes]

    # context = f"""
    #     You convert natural language instructions into JSON commands for a Figma plugin.

    #     Here are the current layers on the canvas:
    #     {layer_names}

    #     Always use exact layer names from this list when referencing layers.
    #     """

    context = f"""
        You convert natural language instructions into JSON commands for a Figma plugin.

        Here is the current information about the canvas:
        {figma_data}

        Always use exact layer names from this list when referencing layers.
    """

    instructions = """
        You must output ONLY valid JSON.
        Do not include explanations, comments, or extra text.
        Do not wrap the JSON in markdown or code blocks.
        
        If the user refers to something ambiguously e.g. "can you move that to the right" you can assume "that" is the currently selected object.

        Supported commands:

        1. Select objects:
        {"type": "select", "query": ["Layer Name"]}
        - "query" must always be an array of strings
        - Use exact layer names from the list above
        - Multiple objects should be included in the array

        2. Global zoom:
        {"type": "zoom", "query": number}

        3. Global pan:
        {"type": "pan", "query": {"x": number, "y": number}}

        4. Zoom to object:
        {"type": "object zoom", "query": "Layer Name"}

        5. Pan to object:
        {"type": "object pan", "query": "Layer Name"}

        6. Move object:
        {"type": "move", "query": "Layer Name", "x": number, "y": number}

        7. Resize object:
        {"type": "resize", "query": "Layer Name", "factor": number}

        8. Create rectangle:
        {"type": "create rect", "query": "name", "x": number, "y": number, "width": number, "height": number}

        9. Create text:
        {"type": "create text", "query": "name", "x": number, "y": number, "content": "string"}
        
        10. Zoom to fit / show everthing / show entire context:
        {"type": "zoom fit"}

        If no valid command: {"type": "unknown", "raw": "what the user said"}
        
        You have access to the conversation history - use it to resolve references like "that", "it", "move it there", 
        or "do that again" by referring to previous commands and their context. If the user wants to undo something try undoing your previous step.
        """
    return context + instructions
