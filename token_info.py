def create_token_meta(symbol, name, total_supply):
    return {
        "symbol": symbol,
        "name": name,
        "totalSupply": total_supply,
        "type": "ERC-20"
    }

print(create_token_meta("MTK", "MyTestToken", 1000000))
