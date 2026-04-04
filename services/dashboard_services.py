from models import FinancialRecord

def get_summary():
    records = FinancialRecord.query.all()

    total_income = 0
    total_expense = 0

    category_data = {}

    for r in records:
        if r.type == "INCOME":
            total_income += r.amount
        else:
            total_expense += r.amount

        # category-wise
        if r.category:
            category_data[r.category] = category_data.get(r.category, 0) + r.amount

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense,
        "category_summary": category_data
    }