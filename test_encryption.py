"""Test encryption functionality"""
import sys
import os
sys.path.insert(0, '/home/ubuntu/UncensorHub')

from app import EncryptionManager, validate_passphrase
import json

print("=" * 60)
print("ENCRYPTION FUNCTIONALITY TEST")
print("=" * 60)

# Test 1: Passphrase validation
print("\n[Test 1] Passphrase Validation")
valid, msg = validate_passphrase("short")
print(f"  Weak passphrase rejected: {not valid} ✓" if not valid else "  ✗ FAILED")

valid, msg = validate_passphrase("strong_password_123")
print(f"  Strong passphrase accepted: {valid} ✓" if valid else "  ✗ FAILED")

# Test 2: Encryption/Decryption
print("\n[Test 2] Encryption/Decryption")
em = EncryptionManager("test_passphrase_secure")
test_message = "This is a classified message for testing"
encrypted = em.encrypt(test_message)
decrypted = em.decrypt(encrypted)

print(f"  Original: {test_message}")
print(f"  Encrypted: {encrypted[:50]}...")
print(f"  Decrypted: {decrypted}")
print(f"  Match: {test_message == decrypted} ✓" if test_message == decrypted else "  ✗ FAILED")

# Test 3: Encrypted data is not plaintext
print("\n[Test 3] Encrypted Data Security")
plaintext_found = test_message in encrypted
print(f"  Plaintext not in encrypted: {not plaintext_found} ✓" if not plaintext_found else "  ✗ FAILED")

# Test 4: Wrong passphrase fails
print("\n[Test 4] Wrong Passphrase Protection")
em2 = EncryptionManager("different_passphrase")
try:
    em2.decrypt(encrypted)
    print("  ✗ FAILED: Wrong passphrase should fail")
except:
    print("  Wrong passphrase rejected: True ✓")

# Test 5: Multiple messages
print("\n[Test 5] Multiple Message Encryption")
messages = [
    {"role": "user", "content": "Hello AI", "timestamp": "2025-01-01 12:00:00"},
    {"role": "assistant", "content": "Hello! How can I help?", "timestamp": "2025-01-01 12:00:05"},
    {"role": "user", "content": "Tell me a secret", "timestamp": "2025-01-01 12:00:10"}
]

encrypted_messages = []
for msg in messages:
    encrypted_msg = {
        "role": msg["role"],
        "content": em.encrypt(msg["content"]),
        "timestamp": msg["timestamp"]
    }
    encrypted_messages.append(encrypted_msg)

# Save to file
with open("test_encrypted_history.json", "w") as f:
    json.dump(encrypted_messages, f, indent=2)

# Verify file doesn't contain plaintext
with open("test_encrypted_history.json", "r") as f:
    file_content = f.read()
    plaintext_in_file = any(msg["content"] in file_content for msg in messages)
    print(f"  No plaintext in file: {not plaintext_in_file} ✓" if not plaintext_in_file else "  ✗ FAILED")

# Decrypt and verify
decrypted_messages = []
for enc_msg in encrypted_messages:
    dec_msg = {
        "role": enc_msg["role"],
        "content": em.decrypt(enc_msg["content"]),
        "timestamp": enc_msg["timestamp"]
    }
    decrypted_messages.append(dec_msg)

all_match = all(decrypted_messages[i]["content"] == messages[i]["content"] for i in range(len(messages)))
print(f"  All messages decrypted correctly: {all_match} ✓" if all_match else "  ✗ FAILED")

# Cleanup
os.remove("test_encrypted_history.json")
if os.path.exists(".salt"):
    os.remove(".salt")

print("\n" + "=" * 60)
print("ENCRYPTION TESTS COMPLETED")
print("=" * 60)
