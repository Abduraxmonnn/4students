async def get_faculty_name(short_name: str, obj) -> dict:
    print(short_name)
    data = {
        'ACC': {
            'direction': obj.BUSINESS_FINANCE,
            'faculty': 'ACCOUNTING'
        },
        'AUD': {
            'direction': obj.BUSINESS_FINANCE,
            'faculty': 'ARCHITECTURE AND URBAN DESIGN'
        },
        'BAN': {
            'direction': 'BUSINESS_FINANCE',
        },
        'ISE': {
            'direction': obj.ENGINEERING,
            'faculty': 'INFORMATION SYSTEM ENGINEERING'
        }
    }

    return data[short_name]

