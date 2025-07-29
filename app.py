from sympy import symbols
from sympy.logic.boolalg import SOPform

def qm_simplify(m, num_vars):
    """ساده‌سازی تابع بولی بر اساس مین‌ترم‌ها و تعداد متغیرها."""
    vars = symbols(f'x0:{num_vars}')
    return SOPform(vars, m)

if __name__ == '__main__':
    # دریافت ورودی مین‌ترم‌ها
    m_input = input("لطفاً لیست مین‌ترم‌ها را با کاما جدا وارد کنید (مثال: 0,1,2): ")
    m = [int(x.strip()) for x in m_input.split(',') if x.strip().isdigit()]

    # دریافت تعداد متغیرها
    num_vars = int(input("لطفاً تعداد متغیرها را وارد کنید (مثال: 3): "))

    # ساده‌سازی
    expr = qm_simplify(m, num_vars)

    # نمایش نتیجه نهایی
    print("\n--- نتیجه ساده‌سازی تابع بولی ---")
    print(f"مین‌ترم‌ها (m): {m}")
    print(f"تعداد متغیرها: {num_vars}")
    print(f"تابع ساده‌شده: {expr}")
