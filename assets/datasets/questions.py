INVESTMENT_QUESTIONS = {
    'Q1': {
        'question': 'Find all trades for customer with an ID of C00003',
        'query': """SELECT i.id,
        t.*
FROM contact i
LEFT JOIN investment inv ON inv.investorid=i.id
LEFT JOIN trade t ON t.investmentid=inv.id
WHERE i.id='C00003'"""
    },
    'Q2': {
        'question': 'Produce the quantity of trades for each customer who has more than 10 shares.',
        'query': '''SELECT * FROM trade'''
    },
    'Q3': {
        'question': 'Do something',
        'query': '''SELECT * FROM contact'''
    }
}

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
