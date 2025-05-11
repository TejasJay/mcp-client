from mcp.client import MCPClient
import asyncio
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = MCPClient()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
async def search():
    query = request.json.get('query')
    library = request.json.get('library')
    
    if not query or not library:
        return jsonify({'error': 'Please provide both query and library'}), 400
    
    try:
        # Use the MCP client to call the get_docs tool
        result = await client.call_tool('get_docs', {
            'query': query,
            'library': library
        })
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000) 