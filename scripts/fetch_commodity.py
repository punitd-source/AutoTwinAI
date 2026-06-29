import yfinance as yf

symbols = {

"Oil":"CL=F",
"Copper":"HG=F",
"Gold":"GC=F"

}

for name,ticker in symbols.items():

    df=yf.download(
        ticker,
        period="1y"
    )

    print(name)

    print(df.head())

    df.to_csv(
        f"data/raw/{name.lower()}.csv"
    )