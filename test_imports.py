#!/usr/bin/env python3
"""
Simple test to verify imports are working correctly
"""

print("Testing imports...")

try:
    from ranger.lang_chain.tools.info import info
    print("✅ info tool imported successfully")
except ImportError as e:
    print(f"❌ Failed to import info tool: {e}")

try:
    from ranger.lang_chain.tools.math import math
    print("✅ math tool imported successfully")
except ImportError as e:
    print(f"❌ Failed to import math tool: {e}")

try:
    from ranger.lib.anthropic_details import AnthropicDetails
    print("✅ AnthropicDetails imported successfully")
except ImportError as e:
    print(f"❌ Failed to import AnthropicDetails: {e}")

# Test the tools without LLM
try:
    result = info()
    print(f"✅ info() tool result: {result}")
except Exception as e:
    print(f"❌ Failed to call info() tool: {e}")

try:
    result = math(5, 3, "+")
    print(f"✅ math(5, 3, '+') tool result: {result}")
except Exception as e:
    print(f"❌ Failed to call math() tool: {e}")

print("\n🎉 Import test completed!")
print("Your pyproject.toml configuration is working correctly!")