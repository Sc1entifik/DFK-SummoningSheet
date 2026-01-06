from secrets import token_urlsafe

generate_secret_key = lambda : token_urlsafe(32)
print(generate_secret_key())
