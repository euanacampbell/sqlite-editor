INVESTMENT_QUESTIONS = {
    'Q1': {
        'question': 'Find all trades for investor C00003',
        'query': """SELECT i.id,
	   i.fullname,
	   t.shares,
	   t.price
FROM contact i
LEFT JOIN investment inv ON inv.investorid=i.id
LEFT JOIN trade t ON t.investmentid=inv.id
WHERE i.id='C00003'"""
    },
    'Q2': {
        'question': 'Find all clients who have more than 15,000 shares',
        'query': """SELECT i.id,
	   i.fullname,
	   SUM(t.shares) [Total Shares]
FROM contact i
LEFT JOIN investment inv ON inv.investorid=i.id
LEFT JOIN trade t ON t.investmentid=inv.id
GROUP BY i.id, i.fullname
HAVING SUM(t.shares) > 15000"""
    },
    'Q3': {
        'question': 'Calculate how many shares are advised by each of the firms',
        'query': """SELECT f.id,
	   f.firmname,
	   SUM(t.shares) [Total Shares]
FROM investment i
LEFT JOIN firm f ON f.id=i.firmid
LEFT JOIN trade t ON t.investmentid=i.id
GROUP BY f.id,
	   f.firmname"""
    }
}

""",
    'Q4': {
        'question': 'Produce a list of all unique investor names that are advised by Herbert Johanssen (C00004)',
        'query': """SELECT DISTINCT c.fullname
FROM investment i
LEFT JOIN contact c ON c.id=i.investorid
LEFT JOIN contact a ON a.id=i.adviserid
WHERE i.adviserid='C00004'
"""
    },
    'Q5': {
        'question': 'Calculate how much each investor has invested',
        'query': """SELECT c.id, SUM(t.shares*t.price) [Cost]
FROM Trade t
LEFT JOIN investment i ON i.id=t.investmentid
LEFT JOIN contact c ON c.id=i.investorid
GROUP BY c.id"""
    }"""

TRADING_QUESTIONS = {
    'Q1': {
        'question': 'Combine both tables.',
        'query': '''SELECT * FROM Trade t
        LEFT JOIN Customer c ON c.custcode=t.custcode'''
    },
    'Q2': {
        'question': 'Produce the quantity of trades for each customer who has more than 10 shares.',
        'query': '''SELECT t.custcode, c.CustName, SUM(t.qty)
                    FROM Trade t
                    LEFT JOIN Customer c ON c.custcode=t.custcode
                    GROUP BY t.custcode, c.CustName
                    HAVING SUM(t.qty)>10'''
    },
    'Q3': {
        'question': 'Do something',
        'query': '''SELECT t.custcode, c.CustName, SUM(t.qty)
                    FROM Trade t
                    LEFT JOIN Customer c ON c.custcode=t.custcode
                    GROUP BY t.custcode, c.CustName
                    HAVING SUM(t.qty)>10'''
    }
}
