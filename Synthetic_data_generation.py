"""
============================================================================
Synthetic Homeowners Insurance Claims Data Generation
Author: J. M. Garcia
Date: February 2026
Purpose: Generate theoretically-grounded synthetic claims data for 
         inflation-frequency correlation analysis
============================================================================
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducible results
np.random.seed(42)
random.seed(42)

print("🏠 HOMEOWNERS INSURANCE SYNTHETIC DATA GENERATOR")
print("=" * 60)

# Load the original Kaggle dataset template
print("📂 Loading original dataset...")
df_original = pd.read_csv('Insurance_claims_data.csv')
print(f"   Original records: {len(df_original):,}")

# Extract relevant variables for homeowners context
df_base = df_original[['policy_id', 'subscription_length', 'customer_age', 
                       'region_code', 'region_density', 'claim_status']].copy()

# Add homeowners-specific variables
print("🏡 Adding homeowners-specific variables...")

# Property characteristics
df_base['property_age'] = np.random.normal(25, 15, len(df_base))
df_base['property_age'] = np.clip(df_base['property_age'], 1, 100).round().astype(int)

# Property values with regional adjustments
base_value = 300000
density_factor = df_base['region_density'] / df_base['region_density'].max()
age_factor = 1 - (df_base['property_age'] / 100) * 0.3

df_base['property_value'] = (base_value * (1 + density_factor) * age_factor * 
                           np.random.normal(1, 0.3, len(df_base)))
df_base['property_value'] = np.clip(df_base['property_value'], 100000, 2000000).round(-3).astype(int)

# Generate claims with economic sensitivity factors
# [Include the key claims generation logic here]

# Save synthetic dataset
df_synthetic.to_csv('synthetic_homeowners_claims.csv', index=False)
print(f"💾 Saved synthetic dataset with {len(df_synthetic):,} claims")
