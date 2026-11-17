import numpy as np
import pandas as pd
from faker import Faker
import random

fake = Faker()
random.seed(42)
np.random.seed(42)

def generate_synthetic_data(num_rows: int = 1000) -> pd.DataFrame:
    """Generate a DataFrame with synthetic credit‑risk records."""
    ids = np.arange(1, num_rows + 1)

    # Age: 21‑75, normal distribution centered at 40
    ages = np.clip(np.random.normal(loc=40, scale=12, size=num_rows), 21, 75).astype(int)

    # Annual income: log‑normal distribution
    incomes = np.round(np.random.lognormal(mean=10, sigma=0.5, size=num_rows)).astype(int)

    # Employment length in years: 0‑40
    employment_lengths = np.random.randint(0, 41, size=num_rows)

    # Credit score: 300‑850, normal distribution
    credit_scores = np.clip(np.random.normal(loc=680, scale=50, size=num_rows), 300, 850).astype(int)

    # Loan amount: 1k‑100k, correlated with income
    loan_amounts = np.round(incomes * np.random.uniform(0.1, 0.5, size=num_rows)).astype(int)

    # Purpose: categorical
    purposes = np.random.choice(
        ["car", "home_improvement", "debt_consolidation", "education", "medical", "vacation", "other"],
        size=num_rows,
    )

    # Default flag: probability increases with higher loan‑to‑income and lower credit score
    prob_default = (
        0.05
        + 0.15 * (loan_amounts / incomes)
        + 0.2 * (700 - credit_scores) / 400
    )
    prob_default = np.clip(prob_default, 0, 1)
    defaults = np.random.binomial(1, prob_default)

    df = pd.DataFrame({
        "id": ids,
        "age": ages,
        "income": incomes,
        "employment_length": employment_lengths,
        "credit_score": credit_scores,
        "loan_amount": loan_amounts,
        "purpose": purposes,
        "default": defaults,
    })
    return df
