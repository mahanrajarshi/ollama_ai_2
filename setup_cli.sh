#!/bin/bash
# LLM Penetration Testing CLI Setup Script

set -e

echo "🚀 LLM Penetration Testing CLI Setup"
echo "===================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama is not installed. Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
    
    echo "✅ Ollama installed successfully"
    echo "🔧 Starting Ollama service..."
    ollama serve > ollama_service.log 2>&1 &
    
    # Wait for Ollama to start
    echo "⏳ Waiting for Ollama service to start..."
    sleep 10
    
    echo "📦 Pulling recommended models..."
    echo "   - Pulling llama3.2:latest (recommended for tester model)"
    ollama pull llama3.2:latest
    
    echo "   - Pulling llama3.2:1b (recommended for target model)"
    ollama pull llama3.2:1b
    
    echo "✅ Default models pulled successfully"
else
    echo "✅ Ollama is already installed"
    
    # Check if service is running
    if ! pgrep -f "ollama serve" > /dev/null; then
        echo "🔧 Starting Ollama service..."
        ollama serve > ollama_service.log 2>&1 &
        sleep 5
    fi
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements_cli.txt

# Make CLI executable
chmod +x llm_pentest_cli.py

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "📋 Quick Start Guide:"
echo "===================="
echo "1. List available models:"
echo "   python3 llm_pentest_cli.py --list-models"
echo ""
echo "2. Run penetration testing:"
echo "   python3 llm_pentest_cli.py --tester-model llama3.2:latest --target-model llama3.2:1b"
echo ""
echo "3. Run with custom parameters:"
echo "   python3 llm_pentest_cli.py --tester-model MODEL1 --target-model MODEL2 --max-tests 5 --delay 1.0"
echo ""
echo "📖 For more options:"
echo "   python3 llm_pentest_cli.py --help"
echo ""
echo "🔍 OWASP Categories Tested:"
echo "   • LLM01: Prompt Injection"
echo "   • LLM02: Insecure Output Handling"
echo "   • LLM06: Sensitive Information Disclosure"
echo "   • LLM04: Model Denial of Service"
echo ""
echo "📊 Results will be saved as individual JSON files and logged to llm_pentest.log"