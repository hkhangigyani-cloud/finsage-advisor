# 🚀 FinSage - AI Financial Advisor for Pakistan & Crypto

A comprehensive financial calculator and analysis tool designed for Pakistani investors and global cryptocurrency traders.

## 📋 Overview

**FinSage** is a Python-based financial calculator that provides:
- Portfolio analysis and return calculations
- Risk assessment tools
- Pakistan-specific tax calculations (PSX stocks)
- Crypto position sizing recommendations
- SIP (Systematic Investment Plan) calculators
- Dollar-Cost Averaging (DCA) tools

## ✨ Features

### 📊 Portfolio Analysis
- **CAGR Calculator**: Calculate Compound Annual Growth Rate
- **Simple Returns**: Quick percentage return calculations
- **Risk Assessment**: Evaluate investments based on volatility and Sharpe ratio
- **Diversification Score**: Measure portfolio diversification using Herfindahl Index

### 💰 Investment Calculators
- **SIP Calculator**: Project future value of monthly investments
- **DCA Calculator**: Analyze dollar-cost averaging strategies
- **Position Sizing**: Recommended crypto allocation by risk tolerance

### 🇵🇰 Pakistan Tax Tools
- **Capital Gains Tax**: PSX stock tax calculator (15% <1 year, 0% >1 year)
- **Withholding Tax**: Calculate 0.15% WHT on stock sales
- **Crypto Tax Status**: Current regulatory landscape in Pakistan

### 🌐 Crypto Position Sizing
- **Conservative**: 5% allocation
- **Moderate**: 15% allocation  
- **Aggressive**: 30% allocation

## 🔧 Installation

### Option 1: Download Directly
1. Download `finsage_calculator.py`
2. Run with Python 3.6+:
```bash
python finsage_calculator.py
```

### Option 2: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/finsage-advisor.git
cd finsage-advisor
python finsage_calculator.py
```

## 📖 Usage Examples

### Basic Usage
```python
from finsage_calculator import PortfolioAnalyzer, PakistanTaxCalculator, InvestmentCalculator

# Initialize
portfolio = PortfolioAnalyzer()
tax_calc = PakistanTaxCalculator()
investment = InvestmentCalculator()

# Calculate CAGR
cagr = portfolio.calculate_returns(
    initial_investment=100000,
    final_value=150000,
    years=3
)
print(f"CAGR: {cagr}%")

# Calculate Pakistan CGT
tax_info = tax_calc.capital_gains_tax(
    gain=50000,
    holding_period_years=0.5
)
print(f"Tax: PKR {tax_info['tax_amount']}")

# SIP Calculation
sip = investment.future_value_sip(
    monthly_investment=10000,
    annual_return_rate=12,
    years=5
)
print(f"Future Value: PKR {sip['future_value']}")
```

### Run All Examples
Simply run the file to see all 9 examples:
```bash
python finsage_calculator.py
```

## 📊 Example Output

```
📊 EXAMPLE 1: Portfolio Return Analysis
------------------------------------------------------------
Initial Investment: PKR 100,000
Final Value: PKR 150,000
Time Period: 3 years
CAGR: 14.47% per year
Simple Return: 50.0%

🇵🇰 EXAMPLE 5: Pakistan Capital Gains Tax (PSX)
------------------------------------------------------------
Gain: PKR 50,000 (Holding: 0.5 years)
Tax: PKR 7,500 at 15%
Note: Short-term holding (less than 1 year)
```

## 🎯 Use Cases

1. **Portfolio Management**
   - Track investment returns
   - Assess risk levels
   - Measure diversification

2. **Tax Planning (Pakistan)**
   - Calculate CGT before selling PSX stocks
   - Estimate withholding tax on transactions
   - Understand crypto tax implications

3. **Investment Planning**
   - Project SIP returns
   - Plan DCA strategies for crypto
   - Determine optimal crypto allocation

4. **Crypto Trading**
   - Position sizing based on risk tolerance
   - DCA analysis for volatile assets
   - Portfolio balance recommendations

## ⚠️ Important Disclaimers

1. **Not Financial Advice**: This tool provides calculations and analysis only. Always consult licensed financial advisors for investment decisions.

2. **Tax Laws Change**: Pakistan tax regulations may change. Verify current rates with FBR or tax professionals.

3. **Crypto Regulations**: Cryptocurrency taxation in Pakistan is currently unclear. Consult tax advisors.

4. **Market Risk**: Past performance does not guarantee future results. All investments carry risk.

## 🛠️ Technical Details

- **Language**: Python 3.6+
- **Dependencies**: None (uses only built-in libraries)
- **License**: MIT License
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 📚 Key Functions

### PortfolioAnalyzer Class
- `calculate_returns()` - CAGR calculation
- `simple_return()` - Basic percentage return
- `risk_assessment()` - Risk level evaluation
- `diversification_score()` - Portfolio diversity metric
- `crypto_position_sizing()` - Recommended crypto allocation

### PakistanTaxCalculator Class
- `capital_gains_tax()` - PSX CGT calculator
- `withholding_tax_stocks()` - WHT on stock sales
- `crypto_tax_estimate()` - Crypto tax status

### InvestmentCalculator Class
- `future_value_sip()` - SIP projections
- `dca_calculator()` - DCA analysis

## 🔗 Integration with AI Advisor

This code can be imported as knowledge for AI financial advisors:

```python
# Use in custom GPT or Claude Projects
# Upload this file as knowledge base
# Reference functions in prompts
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Add more Pakistani investment vehicles (NSS, PIBs, Sukuks)
- Integrate real-time PSX data APIs
- Add more crypto metrics (RSI, MACD, etc.)
- Create web interface

## 📞 Support

For issues or questions:
1. Open a GitHub issue
2. Check existing documentation
3. Review example code

## 📄 License

MIT License - Free to use and modify

## 🌟 Acknowledgments

Built for Pakistani investors and crypto traders seeking data-driven financial analysis tools.

---

**Remember**: Always do your own research (DYOR) and consult professionals before making investment decisions.

**Disclaimer**: This software is provided "as is" without warranty. Use at your own risk.
