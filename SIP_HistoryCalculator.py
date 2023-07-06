import yfinance as fin
import matplotlib.pyplot as plot
import pandas as pn

fund_name = input("Enter the name of the mutual fund \n")
start_date = input("Enter the start date (YYYY-MM-DD) \n")
end_date = input("Enter the end date (YYYY-MM-DD) \n")


fund_data = fin.download(fund_name, start=start_date, end=end_date)

investment_amount = float(input("Enter the Principle \n"))
sip_frequency = int(input("Enter the frequency(month(s)) \n"))
investment_duration = int(input("Enter the Duration \n"))

total_investment = investment_amount * investment_duration
num_sip_payments = investment_duration // sip_frequency


sip_returns = []
for i in range(num_sip_payments):
    investment_value = fund_data['Close'].iloc[i * sip_frequency]
    sip_returns.append(investment_amount * (i + 1) + (investment_amount * (i + 1) * investment_value / fund_data['Close'].iloc[0]))

print("SIP Returns \n")
for i, value in enumerate(list(sip_returns)):
    print(f"Value after {i + 1} SIPs: {value:.2f}")


output_format = input("Choose the output format. Chart / Report? \n")

if output_format.lower() == "chart":
    chart_type = input("Choose chart type 'line', 'bar', 'pie', 'area', or 'histogram': ")
    if chart_type == "line":
        x_values = list(range(1, num_sip_payments + 1))
        plot.plot(x_values, sip_returns)
        plot.xlabel("Number of SIPs")
        plot.ylabel("Investment Value")
        plot.title("SIP Returns")
        plot.show()
    elif chart_type == "bar":
        x_values = list(range(1, num_sip_payments + 1))
        plot.bar(x_values, sip_returns)
        plot.xlabel("Number of SIPs")
        plot.ylabel("Investment Value")
        plot.title("SIP Returns")
        plot.show()
    elif chart_type == "pie":
        labels = [f"SIP {i + 1}" for i in range(num_sip_payments)]
        plot.pie(sip_returns, labels=labels, autopct='%1.1f%%')
        plot.title("Allocation of Funds")
        plot.show()
    elif chart_type == "area":

        plot.fill_between(range(len(sip_returns)), sip_returns)
        plot.xlabel("SIP Installments")
        plot.ylabel("Investment Value")
        plot.title("SIP Investment Growth")
        plot.show()
    elif chart_type == "histogram":

        plot.hist(sip_returns, bins=10)
        plot.xlabel("Investment Value")
        plot.ylabel("Frequency")
        plot.title("Distribution of Investment Returns")
        plot.show()
    else:
        print("Invalid chart type \n")

elif output_format.lower() == "report":
    report_data = {'Number of SIPs': list(range(1, num_sip_payments + 1)), 'Investment Value': sip_returns}
    df = pn.DataFrame(report_data)
    print("\nSIP Returns Report")
    print(df)

