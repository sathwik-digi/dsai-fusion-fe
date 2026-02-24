from app.models.customer import Customer

def generate_customer_code(db, company_name: str) -> str:
    words = company_name.strip().split()
    code_parts = []

    for word in words:
        if len(word) >= 3:
            code_parts.append(word[:3])
        else:
            code_parts.append(word)

    base_code = "".join(code_parts).upper()

    # Check duplicates
    existing_count = (
        db.query(Customer)
        .filter(Customer.customer_code.like(f"{base_code}%"))
        .count()
    )

    if existing_count == 0:
        return base_code
    else:
        return f"{base_code}{existing_count + 1}"
