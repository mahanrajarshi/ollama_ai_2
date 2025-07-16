#!/usr/bin/env python3
"""
LLM Penetration Testing CLI - Architecture Visualization
========================================================
Generate visual architecture diagrams and workflow charts for the presentation.
"""

import json
from datetime import datetime

def create_architecture_diagram():
    """Create detailed architecture diagram"""
    
    architecture = {
        "title": "LLM Penetration Testing CLI - System Architecture",
        "layers": [
            {
                "name": "Presentation Layer",
                "components": [
                    {
                        "name": "CLI Interface",
                        "description": "Command-line interface for user interaction",
                        "functions": ["Argument parsing", "Model selection", "Progress display", "Result output"]
                    },
                    {
                        "name": "Demo Mode",
                        "description": "Simulated testing without Ollama",
                        "functions": ["Realistic scenarios", "Sample responses", "JSON output demonstration"]
                    }
                ]
            },
            {
                "name": "Application Layer",
                "components": [
                    {
                        "name": "LLM Penetration Tester",
                        "description": "Core testing engine",
                        "functions": ["Test orchestration", "Attack generation", "Response analysis", "Evolution logic"]
                    },
                    {
                        "name": "Attack Pattern Engine",
                        "description": "Sophisticated attack pattern library",
                        "functions": ["20+ attack patterns", "OWASP categorization", "Template generation", "Pattern evolution"]
                    },
                    {
                        "name": "Result Handler",
                        "description": "Output processing and formatting",
                        "functions": ["JSON formatting", "File output", "Logging", "Summary generation"]
                    }
                ]
            },
            {
                "name": "Integration Layer",
                "components": [
                    {
                        "name": "Ollama Client",
                        "description": "API communication with Ollama service",
                        "functions": ["HTTP requests", "Model management", "Error handling", "Timeout management"]
                    },
                    {
                        "name": "Model Manager",
                        "description": "Manages tester and target models",
                        "functions": ["Model listing", "Connection handling", "Load balancing", "Health checks"]
                    }
                ]
            },
            {
                "name": "Service Layer",
                "components": [
                    {
                        "name": "Ollama Service",
                        "description": "Local LLM hosting service",
                        "functions": ["Model hosting", "Inference execution", "Memory management", "API endpoints"]
                    },
                    {
                        "name": "Tester Model",
                        "description": "Generates attacks and analyzes responses",
                        "functions": ["Attack generation", "Response analysis", "Vulnerability detection", "Strategy evolution"]
                    },
                    {
                        "name": "Target Model",
                        "description": "Model being tested for vulnerabilities",
                        "functions": ["Response generation", "Vulnerability exhibition", "Safety testing", "Behavior analysis"]
                    }
                ]
            }
        ],
        "data_flow": [
            "CLI → Penetration Tester → Attack Pattern Engine → Attack Generation",
            "Attack Generation → Ollama Client → Target Model → Response",
            "Response → Ollama Client → Tester Model → Analysis",
            "Analysis → Result Handler → JSON Output → CLI Display"
        ]
    }
    
    return architecture

def create_workflow_diagram():
    """Create detailed workflow diagram"""
    
    workflow = {
        "title": "LLM Penetration Testing - Detailed Workflow",
        "phases": [
            {
                "phase": "1. INITIALIZATION",
                "steps": [
                    {
                        "step": "1.1 Environment Setup",
                        "actions": ["Start Ollama service", "Verify model availability", "Initialize logging"],
                        "outputs": ["Service status", "Model list", "Log files"]
                    },
                    {
                        "step": "1.2 Model Configuration",
                        "actions": ["Load tester model", "Load target model", "Validate connections"],
                        "outputs": ["Model instances", "Connection status", "Configuration validation"]
                    },
                    {
                        "step": "1.3 Attack Pattern Loading",
                        "actions": ["Load attack patterns", "Initialize OWASP categories", "Setup evolution context"],
                        "outputs": ["Pattern library", "Category mapping", "Context state"]
                    }
                ]
            },
            {
                "phase": "2. ATTACK GENERATION",
                "steps": [
                    {
                        "step": "2.1 Pattern Selection",
                        "actions": ["Select OWASP category", "Choose attack vector", "Load pattern template"],
                        "outputs": ["Selected category", "Attack vector", "Template"]
                    },
                    {
                        "step": "2.2 Prompt Generation",
                        "actions": ["Apply context", "Generate attack prompt", "Validate payload"],
                        "outputs": ["Attack prompt", "Payload validation", "Test metadata"]
                    },
                    {
                        "step": "2.3 Attack Preparation",
                        "actions": ["Format test structure", "Generate test ID", "Set timestamp"],
                        "outputs": ["Test structure", "Unique ID", "Timestamp"]
                    }
                ]
            },
            {
                "phase": "3. ATTACK EXECUTION",
                "steps": [
                    {
                        "step": "3.1 Payload Delivery",
                        "actions": ["Send prompt to target", "Monitor response time", "Handle timeouts"],
                        "outputs": ["Target response", "Response time", "Error status"]
                    },
                    {
                        "step": "3.2 Response Capture",
                        "actions": ["Capture full response", "Extract metadata", "Log interaction"],
                        "outputs": ["Response text", "Metadata", "Interaction log"]
                    },
                    {
                        "step": "3.3 Error Handling",
                        "actions": ["Check for errors", "Retry if needed", "Log failures"],
                        "outputs": ["Error status", "Retry attempts", "Failure logs"]
                    }
                ]
            },
            {
                "phase": "4. RESPONSE ANALYSIS",
                "steps": [
                    {
                        "step": "4.1 Vulnerability Detection",
                        "actions": ["Send to tester model", "Analyze response", "Detect indicators"],
                        "outputs": ["Analysis result", "Vulnerability status", "Indicators"]
                    },
                    {
                        "step": "4.2 Severity Assessment",
                        "actions": ["Evaluate severity", "Assess impact", "Generate score"],
                        "outputs": ["Severity level", "Impact assessment", "Risk score"]
                    },
                    {
                        "step": "4.3 Remediation Guidance",
                        "actions": ["Generate recommendations", "Suggest fixes", "Provide guidance"],
                        "outputs": ["Remediation steps", "Fix suggestions", "Security guidance"]
                    }
                ]
            },
            {
                "phase": "5. EVOLUTION & ITERATION",
                "steps": [
                    {
                        "step": "5.1 Context Update",
                        "actions": ["Update test context", "Store results", "Track patterns"],
                        "outputs": ["Updated context", "Result storage", "Pattern tracking"]
                    },
                    {
                        "step": "5.2 Strategy Evolution",
                        "actions": ["Analyze success rate", "Evolve strategy", "Plan next attack"],
                        "outputs": ["Evolution strategy", "Next attack plan", "Success metrics"]
                    },
                    {
                        "step": "5.3 Loop Control",
                        "actions": ["Check test limits", "Manage delays", "Control iteration"],
                        "outputs": ["Loop status", "Delay timing", "Iteration count"]
                    }
                ]
            },
            {
                "phase": "6. OUTPUT GENERATION",
                "steps": [
                    {
                        "step": "6.1 JSON Formatting",
                        "actions": ["Structure JSON", "Validate format", "Add metadata"],
                        "outputs": ["Structured JSON", "Format validation", "Complete metadata"]
                    },
                    {
                        "step": "6.2 File Output",
                        "actions": ["Save individual results", "Update logs", "Generate summary"],
                        "outputs": ["Result files", "Log updates", "Summary report"]
                    },
                    {
                        "step": "6.3 Display Results",
                        "actions": ["Format for display", "Show progress", "Present summary"],
                        "outputs": ["Formatted display", "Progress indicators", "Final summary"]
                    }
                ]
            }
        ]
    }
    
    return workflow

def create_owasp_mapping():
    """Create OWASP category mapping"""
    
    owasp_mapping = {
        "title": "OWASP LLM Top 10 - Implementation Coverage",
        "categories": [
            {
                "code": "LLM01",
                "name": "Prompt Injection",
                "description": "Manipulating LLM via crafted inputs",
                "attack_vectors": [
                    "Authority Impersonation",
                    "DAN (Do Anything Now)",
                    "Hypothetical Scenarios",
                    "Emergency Manipulation",
                    "System Prompt Injection"
                ],
                "severity": "High",
                "implementation_status": "✅ Implemented"
            },
            {
                "code": "LLM02",
                "name": "Insecure Output Handling",
                "description": "Insufficient validation of LLM outputs",
                "attack_vectors": [
                    "Script Tag Injection",
                    "Command Injection",
                    "Template Injection",
                    "Data Exfiltration"
                ],
                "severity": "High",
                "implementation_status": "✅ Implemented"
            },
            {
                "code": "LLM06",
                "name": "Sensitive Information Disclosure",
                "description": "Unintended revelation of sensitive data",
                "attack_vectors": [
                    "System Prompt Extraction",
                    "Training Data Extraction",
                    "Technical Specification Leakage",
                    "Context Bleeding"
                ],
                "severity": "High",
                "implementation_status": "✅ Implemented"
            },
            {
                "code": "LLM04",
                "name": "Model Denial of Service",
                "description": "Resource exhaustion attacks",
                "attack_vectors": [
                    "Resource Exhaustion",
                    "Complex Processing",
                    "Memory Exhaustion",
                    "Output Flooding"
                ],
                "severity": "Medium",
                "implementation_status": "✅ Implemented"
            }
        ]
    }
    
    return owasp_mapping

def create_technical_specifications():
    """Create technical specifications"""
    
    specs = {
        "title": "Technical Specifications",
        "components": {
            "Programming Language": "Python 3.7+",
            "Dependencies": ["requests>=2.31.0"],
            "Architecture": "Modular, object-oriented",
            "API Communication": "REST API with Ollama",
            "Output Format": "Structured JSON",
            "Logging": "Comprehensive file and console logging",
            "Error Handling": "Robust exception handling with retry logic",
            "Testing": "Unit tests and integration tests included"
        },
        "performance": {
            "Concurrent Tests": "Sequential execution with configurable delays",
            "Memory Usage": "Optimized for large model responses",
            "Timeout Handling": "Configurable timeouts for model responses",
            "Scalability": "Designed for extensibility and pattern addition"
        },
        "security": {
            "Local Deployment": "Runs entirely on local machine",
            "Data Privacy": "No external API calls, full data control",
            "Audit Trail": "Complete logging of all interactions",
            "Reproducibility": "Deterministic test execution"
        }
    }
    
    return specs

def main():
    """Generate all visualization components"""
    
    print("🎨 Generating Architecture Diagrams and Workflow Visualizations...")
    
    # Generate architecture diagram
    architecture = create_architecture_diagram()
    with open("architecture_diagram.json", "w") as f:
        json.dump(architecture, f, indent=2)
    print("✅ Architecture diagram generated: architecture_diagram.json")
    
    # Generate workflow diagram
    workflow = create_workflow_diagram()
    with open("workflow_diagram.json", "w") as f:
        json.dump(workflow, f, indent=2)
    print("✅ Workflow diagram generated: workflow_diagram.json")
    
    # Generate OWASP mapping
    owasp_mapping = create_owasp_mapping()
    with open("owasp_mapping.json", "w") as f:
        json.dump(owasp_mapping, f, indent=2)
    print("✅ OWASP mapping generated: owasp_mapping.json")
    
    # Generate technical specifications
    specs = create_technical_specifications()
    with open("technical_specs.json", "w") as f:
        json.dump(specs, f, indent=2)
    print("✅ Technical specifications generated: technical_specs.json")
    
    print("\n🎯 All visualization components generated successfully!")
    print("📊 These files complement the presentation slides with detailed technical information.")

if __name__ == "__main__":
    main()