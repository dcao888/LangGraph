from IPython.display import Markdown, display

def run_interactive_chat(graph, config):
    print("*** Chatbot started. Type 'quit', 'exit', or 'q' to stop. ***\n")
    
    while True:
        # 1. Capture user input
        user_input = input("User: ")
        
        # 2. Check for exit command
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Chat ended.")
            break

        # 3. Stream the response from your LangGraph
        # We pass the input as a human message to the state
        events = graph.stream(
            {"messages": [("user", user_input)]},
            config,
            stream_mode="values"
        )

        # 4. Process and display the output
        for event in events:
            if "messages" in event:
                # Get the last message (the AI's response)
                last_message = event["messages"][-1]
                
                # Only display if it's an AIMessage to avoid re-printing user input
                if last_message.type == "ai":
                    display(Markdown(f"**Assistant:** {last_message.content}\n\n"))