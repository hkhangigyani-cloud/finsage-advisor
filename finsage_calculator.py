# FinSage - Portfolio & Tax Analysis Tool
# Complete working version for Pakistan & Crypto Markets

import math

# ===== PORTFOLIO ANALYZER =====
class PortfolioAnalyzer:
    def calculate_returns(self, initial_investment, final_value, years):
        """Calculate CAGR (Compound Annual Growth Rate)"""
        if years <= 0 or initial_investment <= 0:
            return "Invalid input"
        cagr = ((final_value / initial_investment) ** (1/years) - 1) * 100
        return round(cagr, 2)
    
    def simple_return(self, initial_investment, final_value):
        """Calculate simple percentage return"""
        return round(((final_value - initial_investment) / initial_investment) * 100, 2)
    
    def risk_assessment(self, volatility, sharpe_ratio):
        """Assess risk level based on volatility and Sharpe ratio"""
        if volatility < 10 and sharpe_ratio > 1:
            return "Low Risk - Stable investment"
        elif volatility < 20 and sharpe_ratio > 0.5:
            return "Moderate Risk - Balanced approach"
        else:
            return "High Risk - Volatile investment"
    
    def diversification_score(self, portfolio_weights):
        """Calculate diversification using Herfindahl Index
        portfolio_weights: list of decimal weights (should sum to 1)
        """
        herfindahl = sum([w**2 for w in portfolio_weights])
        diversification = (1 - herfindahl) * 100
        return round(diversification, 2)
    
    def crypto_position_sizing(self, total_portfolio, risk_tolerance):
        """Recommend crypto allocation based on risk tolerance"""
        allocations = {
            "conservative": 0.05,  # 5%
            "moderate": 0.15,      # 15%
            "aggressive": 0.30     # 30%
        }
        allocation = allocations.get(risk_tolerance.lower(), 0.10)
        recommended_amount = total_portfolio * allocation
        return {
            "percentage": allocation * 100,
            "amount": round(recommended_amount, 2)
        }

# ===== PAKISTAN TAX CALCULATOR =====
class PakistanTaxCalculator:
    def capital_gains_tax(self, gain, holding_period_years):
        """Calculate CGT on PSX stocks (Pakistan)"""
        if holding_period_years < 1:
            tax = gain * 0.15  # 15% for <1 year
            return {
                "tax_amount": round(tax, 2),
                "tax_rate": "15%",
                "note": "Short-term holding (less than 1 year)"
            }
        else:
            return {
                "tax_amount": 0,
                "tax_rate": "0%",
                "note": "Tax-free (holding period > 1 year)"
            }
    
    def withholding_tax_stocks(self, transaction_value):
        """Calculate WHT on stock sale in Pakistan"""
        wht = transaction_value * 0.015  # 0.15% WHT
        return round(wht, 2)
    
    def crypto_tax_estimate(self, crypto_gain):
        """Crypto taxation in Pakistan (currently ambiguous)"""
        return {
            "status": "Unclear/Unregulated",
            "recommendation": "Consult tax advisor - crypto taxation not clearly defined in Pakistan",
            "note": "FBR has not issued clear guidelines on crypto gains"
        }

# ===== INVESTMENT CALCULATOR =====
class InvestmentCalculator:
    def future_value_sip(self, monthly_investment, annual_return_rate, years):
        """Calculate future value of SIP/Monthly investment"""
        months = years * 12
        monthly_rate = annual_return_rate / 12 / 100
        
        if monthly_rate == 0:
            fv = monthly_investment * months
        else:
            fv = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
        
        total_invested = monthly_investment * months
        returns = fv - total_invested
        
        return {
            "future_value": round(fv, 2),
            "total_invested": round(total_invested, 2),
            "returns": round(returns, 2),
            "return_percentage": round((returns / total_invested) * 100, 2)
        }
    
    def dca_calculator(self, monthly_amount, avg_price_per_unit, months):
        """Dollar Cost Averaging calculator for crypto/stocks"""
        total_invested = monthly_amount * months
        total_units = (monthly_amount / avg_price_per_unit) * months
        
        return {
            "total_invested": total_invested,
            "total_units_bought": round(total_units, 4),
            "average_cost_per_unit": round(total_invested / total_units, 2)
        }

# ===== EXAMPLE USAGE =====
def run_examples():
    print("=" * 60)
    print("FINSAGE - FINANCIAL CALCULATOR FOR PAKISTAN & CRYPTO")
    print("=" * 60)
    
    # Initialize calculators
    portfolio = PortfolioAnalyzer()
    pak_tax = PakistanTaxCalculator()
    investment = InvestmentCalculator()
    
    # Example 1: Portfolio Returns
    print("\n📊 EXAMPLE 1: Portfolio Return Analysis")
    print("-" * 60)
    initial = 100000  # PKR
    final = 150000    # PKR
    years = 3
    
    cagr = portfolio.calculate_returns(initial, final, years)
    simple_ret = portfolio.simple_return(initial, final)
    
    print(f"Initial Investment: PKR {initial:,}")
    print(f"Final Value: PKR {final:,}")
    print(f"Time Period: {years} years")
    print(f"CAGR: {cagr}% per year")
    print(f"Simple Return: {simple_ret}%")
    
    # Example 2: Risk Assessment
    print("\n⚠️ EXAMPLE 2: Risk Assessment")
    print("-" * 60)
    risk_result = portfolio.risk_assessment(volatility=25, sharpe_ratio=0.4)
    print(f"Volatility: 25%")
    print(f"Sharpe Ratio: 0.4")
    print(f"Assessment: {risk_result}")
    
    # Example 3: Portfolio Diversification
    print("\n🎯 EXAMPLE 3: Portfolio Diversification Score")
    print("-" * 60)
    # Portfolio: 40% stocks, 30% bonds, 20% real estate, 10% crypto
    weights = [0.40, 0.30, 0.20, 0.10]
    div_score = portfolio.diversification_score(weights)
    print(f"Portfolio Allocation: {[f'{w*100}%' for w in weights]}")
    print(f"Diversification Score: {div_score}/100")
    print(f"Interpretation: Higher score = Better diversification")
    
    # Example 4: Crypto Position Sizing
    print("\n💰 EXAMPLE 4: Crypto Position Sizing")
    print("-" * 60)
    total_portfolio = 500000  # PKR
    
    for risk_level in ["conservative", "moderate", "aggressive"]:
        result = portfolio.crypto_position_sizing(total_portfolio, risk_level)
        print(f"{risk_level.capitalize()}: {result['percentage']}% = PKR {result['amount']:,}")
    
    # Example 5: Pakistan Capital Gains Tax
    print("\n🇵🇰 EXAMPLE 5: Pakistan Capital Gains Tax (PSX)")
    print("-" * 60)
    
    # Short-term gain
    gain_short = 50000
    holding_short = 0.5
    tax_short = pak_tax.capital_gains_tax(gain_short, holding_short)
    print(f"Gain: PKR {gain_short:,} (Holding: {holding_short} years)")
    print(f"Tax: PKR {tax_short['tax_amount']:,} at {tax_short['tax_rate']}")
    print(f"Note: {tax_short['note']}")
    
    print()
    
    # Long-term gain
    gain_long = 50000
    holding_long = 2
    tax_long = pak_tax.capital_gains_tax(gain_long, holding_long)
    print(f"Gain: PKR {gain_long:,} (Holding: {holding_long} years)")
    print(f"Tax: PKR {tax_long['tax_amount']:,} at {tax_long['tax_rate']}")
    print(f"Note: {tax_long['note']}")
    
    # Example 6: Withholding Tax
    print("\n💵 EXAMPLE 6: Withholding Tax on Stock Sale")
    print("-" * 60)
    sale_value = 200000
    wht = pak_tax.withholding_tax_stocks(sale_value)
    print(f"Stock Sale Value: PKR {sale_value:,}")
    print(f"WHT (0.15%): PKR {wht:,}")
    
    # Example 7: Crypto Tax Status
    print("\n₿ EXAMPLE 7: Crypto Tax in Pakistan")
    print("-" * 60)
    crypto_tax = pak_tax.crypto_tax_estimate(100000)
    print(f"Status: {crypto_tax['status']}")
    print(f"Recommendation: {crypto_tax['recommendation']}")
    
    # Example 8: SIP Calculator
    print("\n📈 EXAMPLE 8: SIP/Monthly Investment Calculator")
    print("-" * 60)
    monthly = 10000  # PKR per month
    annual_return = 12  # 12% annual return
    period = 5  # years
    
    sip_result = investment.future_value_sip(monthly, annual_return, period)
    print(f"Monthly Investment: PKR {monthly:,}")
    print(f"Expected Annual Return: {annual_return}%")
    print(f"Time Period: {period} years")
    print(f"Total Invested: PKR {sip_result['total_invested']:,}")
    print(f"Future Value: PKR {sip_result['future_value']:,}")
    print(f"Returns: PKR {sip_result['returns']:,} ({sip_result['return_percentage']}%)")
    
    # Example 9: DCA Calculator
    print("\n💱 EXAMPLE 9: Dollar-Cost Averaging (Crypto/Stocks)")
    print("-" * 60)
    monthly_dca = 5000  # PKR
    avg_price = 100  # PKR per unit
    months_dca = 12
    
    dca_result = investment.dca_calculator(monthly_dca, avg_price, months_dca)
    print(f"Monthly Investment: PKR {monthly_dca:,}")
    print(f"Average Price per Unit: PKR {avg_price}")
    print(f"Period: {months_dca} months")
    print(f"Total Invested: PKR {dca_result['total_invested']:,}")
    print(f"Total Units Acquired: {dca_result['total_units_bought']}")
    print(f"Average Cost per Unit: PKR {dca_result['average_cost_per_unit']}")
    
    print("\n" + "=" * 60)
    print("Analysis Complete! Use these tools for informed decisions.")
    print("Remember: This is not financial advice. Consult professionals.")
    print("=" * 60)

# Run all examples
if __name__ == "__main__":
    run_examples()
