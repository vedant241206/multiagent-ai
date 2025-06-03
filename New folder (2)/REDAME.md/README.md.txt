FlowBit Multi-Agent AI System
=============================

✅ Overview
-----------
This project uses a multi-agent architecture to:
- Detect the format of an incoming input (Email / JSON)
- Classify its intent (RFQ, Invoice, Complaint, etc.)
- Route it to a specialized agent
- Extract structured data and save context to shared memory

🔧 Structure
------------
- agents/: Contains classifier, email, and JSON agents
- memory/: Lightweight memory store
- utils.py: AI-enhanced format & intent detection
- main.py: Driver script for running flow
- data/: Input files (e.g., email samples)

----------------------
- Add PDF parser agent
- Integrate OpenAI/Gemini for LLM-based classification
- Convert to FastAPI for real-time service
- Add Docker support for deployment
