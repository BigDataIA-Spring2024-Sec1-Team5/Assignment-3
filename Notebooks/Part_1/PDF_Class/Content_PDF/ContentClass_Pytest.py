from pydantic import BaseModel, Field, ValidationError

# Pydantic model for row validation
class RowModel(BaseModel):
    Level: int = Field(..., ge=1, le=3)  # Must be an integer between 1 and 3
    Category: str
    Topic: str
    LearningOutcomes: str

# 10 Test Cases
import pytest


def test_valid_row_model_level_1():
    # This should pass as all conditions meet the model's requirements
    RowModel(Level=1, Category="Economics", Topic="Supply and Demand", LearningOutcomes="Understand the basics of market economy")

def test_valid_row_model_level_2():
    RowModel(Level=2, Category="Quantitative Methods", Topic="Statistics", LearningOutcomes="Descriptive statistics, distributions, and sampling")

def test_valid_row_model_level_3():
    RowModel(Level=3, Category="Fixed Income", Topic="Bond Valuation", LearningOutcomes="Calculate present value of cash flows, understand yield")

def test_valid_row_model_min_level():
    RowModel(Level=1, Category="Derivatives", Topic="Options", LearningOutcomes="Basics of call and put options")

def test_valid_row_model_max_level():
    RowModel(Level=3, Category="Alternative Investments", Topic="Real Estate", LearningOutcomes="Introduction to real estate investment")



def test_invalid_row_model_level_below_min():
    with pytest.raises(ValidationError):
        RowModel(Level=0, Category="Economics", Topic="Microeconomics", LearningOutcomes="Basic principles")

def test_invalid_row_model_level_above_max():
    with pytest.raises(ValidationError):
        RowModel(Level=4, Category="Portfolio Management", Topic="Risk Management", LearningOutcomes="Risk assessment and management strategies")

def test_invalid_row_model_missing_category():
    with pytest.raises(ValidationError):
        RowModel(Level=2, Category="", Topic="Fiscal Policy", LearningOutcomes="Government spending and taxation")

def test_invalid_row_model_missing_topic():
    with pytest.raises(ValidationError):
        RowModel(Level=1, Category="Economics", Topic="", LearningOutcomes="Inflation rates and impacts on economy")

def test_invalid_row_model_non_integer_level():
    with pytest.raises(ValidationError):
        RowModel(Level="Two", Category="Quantitative Methods", Topic="Probability", LearningOutcomes="Understanding of basic probability concepts")

