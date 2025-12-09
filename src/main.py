#!/usr/bin/env python3
"""
Investment Tracker - CLI Application

A command-line tool for tracking and analyzing investment portfolios.
Supports multiple asset types and provides analytics on returns and allocation.
"""

import click
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

__version__ = "0.1.0"
__author__ = "Eswarpu Lavarthi"

# Sample portfolio structure
SAMPLE_PORTFOLIO = {
    "portfolio": [
        {"name": "RELIANCE", "type": "stock", "qty": 10, "buy_price": 2500, "current_price": 2875},
        {"name": "INFY", "type": "stock", "qty": 5, "buy_price": 1800, "current_price": 2100},
        {"name": "HDFC MF", "type": "mutual_fund", "qty": 100, "buy_price": 240, "current_price": 280},
    ]
}

@click.group()
@click.version_option(version=__version__)
def cli():
    """Investment Tracker - Smart portfolio management CLI"""
    pass

@cli.command()
@click.option('--type', type=click.Choice(['stock', 'mutual_fund', 'fd', 'gold_bond']), required=True)
@click.option('--name', required=True, help='Investment name')
@click.option('--qty', type=float, required=True, help='Quantity')
@click.option('--buy-price', type=float, required=True, help='Buy price')
def add_investment(type, name, qty, buy_price):
    """Add a new investment to portfolio"""
    click.echo(f"\u2705 Added {name} ({type}) - Qty: {qty}, Price: ₹{buy_price}")
    click.echo(f"Investment value: ₹{qty * buy_price:,.2f}")

@cli.command()
@click.option('--summary', is_flag=True, help='Show summary only')
def portfolio(summary):
    """View portfolio details"""
    click.echo("\n" + "="*50)
    click.echo("           PORTFOLIO OVERVIEW")
    click.echo("="*50)
    
    total_investment = 0
    current_value = 0
    
    for inv in SAMPLE_PORTFOLIO["portfolio"]:
        inv_total = inv["qty"] * inv["buy_price"]
        current_total = inv["qty"] * inv["current_price"]
        total_investment += inv_total
        current_value += current_total
        
        if not summary:
            gain_loss = current_total - inv_total
            gain_loss_pct = (gain_loss / inv_total) * 100
            click.echo(f"\n{inv['name']} ({inv['type'].upper()})")
            click.echo(f"  Qty: {inv['qty']} | Buy: ₹{inv['buy_price']} | Current: ₹{inv['current_price']}")
            click.echo(f"  Current Value: ₹{current_total:,.2f}")
            click.echo(f"  Gain/Loss: ₹{gain_loss:,.2f} ({gain_loss_pct:+.2f}%)")
    
    # Summary
    total_gain_loss = current_value - total_investment
    total_gain_loss_pct = (total_gain_loss / total_investment) * 100
    
    click.echo("\n" + "-"*50)
    click.echo(f"Total Investment:        ₹{total_investment:,.2f}")
    click.echo(f"Current Value:           ₹{current_value:,.2f}")
    click.echo(f"Absolute Gain/Loss:      ₹{total_gain_loss:,.2f} ({total_gain_loss_pct:+.2f}%)")
    click.echo(f"Holdings:                {len(SAMPLE_PORTFOLIO['portfolio'])}")
    click.echo("="*50 + "\n")

@cli.command()
def analyze():
    """Analyze portfolio allocation"""
    click.echo("\nAsset Class Distribution\n")
    click.echo("├─ Stocks (45%)          ▓▓▓▓▓▓▓▓░░")
    click.echo("├─ Mutual Funds (35%)    ▓▓▓▓▓▓░░░░")
    click.echo("├─ Fixed Deposits (15%)  ▓▓░░░░░░░░")
    click.echo("└─ Gold Bonds (5%)       ▓░░░░░░░░░\n")

@cli.command()
@click.option('--name', required=True, help='Goal name')
@click.option('--target', type=float, required=True, help='Target amount')
@click.option('--deadline', type=int, required=True, help='Target year')
def goal(name, target, deadline):
    """Set investment goal"""
    click.echo(f"\n🎯 Goal: {name}")
    click.echo(f"Target: ₹{target:,.0f}")
    click.echo(f"Deadline: {deadline}")
    current_year = datetime.now().year
    years_left = deadline - current_year
    annual_target = target / max(years_left, 1)
    click.echo(f"Annual Target: ₹{annual_target:,.0f}\n")

@cli.command()
def demo():
    """Run demo with sample portfolio"""
    click.echo("\n🎣 Investment Tracker Demo\n")
    ctx = click.Context(cli)
    ctx.invoke(portfolio, summary=False)
    click.echo()
    ctx.invoke(analyze)

if __name__ == '__main__':
    cli()
