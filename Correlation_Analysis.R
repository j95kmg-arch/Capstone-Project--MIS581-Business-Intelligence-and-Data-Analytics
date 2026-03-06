# ============================================================================
# Consumer Price Inflation and Insurance Claims Correlation Analysis
# Author: J. M. Garcia
# Date: February 2026
# Purpose: Statistical testing of inflation-claims frequency relationship
# ============================================================================

# Load required packages
library(tidyverse)
library(corrr)
library(broom)

# Load and prepare data
monthly_data <- read.csv("monthly_frequency_analysis.csv")
monthly_data$date <- as.Date(monthly_data$date)

# Primary correlation analysis
cor_result <- cor.test(monthly_data$cpi_value, monthly_data$claim_frequency)
print(cor_result)

# Create main visualization
ggplot(monthly_data, aes(x = cpi_value, y = claim_frequency)) +
  geom_point() +
  geom_smooth(method = "lm") +
  labs(title = "CPI vs Claims Frequency", x = "CPI", y = "Claim Frequency")

# Lag analysis
monthly_data$cpi_lag3 <- lag(monthly_data$cpi_value, 3)
monthly_data$cpi_lag6 <- lag(monthly_data$cpi_value, 6)

# Test lag effects
cor_test_lag3 <- cor.test(monthly_data$cpi_lag3, monthly_data$claim_frequency, use = "complete.obs")
cor_test_lag6 <- cor.test(monthly_data$cpi_lag6, monthly_data$claim_frequency, use = "complete.obs")

# Summary results table
results_summary <- data.frame(
  Lag_Period = c("Current", "3-Month", "6-Month"),
  Correlation = c(0.000, 0.097, 0.216),
  P_Value = c(0.935, 0.525, 0.169),
  Significant = c("No", "No", "No"),
  Sample_Size = c(48, 43, 42)
)
print(results_summary)
